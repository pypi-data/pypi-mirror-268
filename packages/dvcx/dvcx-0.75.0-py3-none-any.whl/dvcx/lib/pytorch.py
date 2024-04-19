import logging
from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, Optional

from torch import float32
from torch.distributed import get_rank, get_world_size
from torch.utils.data import IterableDataset, get_worker_info

from dvcx.asyn import ASYNC_WORKERS
from dvcx.catalog import Catalog, get_catalog
from dvcx.query import DatasetQuery

if TYPE_CHECKING:
    from torchvision.transforms.v2 import Transform

    from dvcx.query.schema import UDFParamSpec


logger = logging.getLogger("dvcx")


try:
    from torchvision.transforms import v2

    DEFAULT_TRANSFORM = v2.Compose([v2.ToImage(), v2.ToDtype(float32, scale=True)])
except ImportError:
    logger.warning("Missing dependency torchvision for computer vision transforms.")
    DEFAULT_TRANSFORM = None


class PytorchDataset(IterableDataset):
    def __init__(
        self,
        params: Sequence["UDFParamSpec"],
        name: str,
        version: Optional[int] = None,
        catalog: Optional["Catalog"] = None,
        transform: Optional["Transform"] = DEFAULT_TRANSFORM,
        workers: int = ASYNC_WORKERS,
        cache: bool = False,
        num_samples: int = 0,
    ):
        """
        Pytorch IterableDataset that streams DVCx datasets.

        Args:
            params (UDFParamSpec): Fields from DVCx dataset to stream.
            name (str): Name of DVCx dataset to stream.
            version (int): Version of DVCx dataset to stream.
            catalog (Catalog): DVCx catalog to which dataset belongs.
            transform (Transform): Torchvision v2 transforms to apply to the dataset.
            workers (int): Number of async workers per process.
            cache (bool): Whether to download and cache objects locally.
            num_samples (int): Number of random samples to draw for each epoch.
                This argument is ignored if `num_samples=0` (the default).
        """
        self.params = params
        self.name = name
        self.version = version
        self.transform = transform
        self.workers = workers
        self.cache = cache
        self.num_samples = num_samples
        if catalog is None:
            catalog = get_catalog()
        self._init_catalog(catalog)

    def _init_catalog(self, catalog: "Catalog"):
        # For compatibility with multiprocessing,
        # we can only store params in __init__(), as Catalog isn't picklable
        # see https://github.com/iterative/dvcx/issues/954
        self._idgen_params = catalog.id_generator.clone_params()
        self._ms_params = catalog.metastore.clone_params()
        self._wh_params = catalog.warehouse.clone_params()
        self._catalog_params = catalog.get_init_params()
        self.catalog: Optional[Catalog] = None

    def _get_catalog(self) -> "Catalog":
        idgen_cls, idgen_args, idgen_kwargs = self._idgen_params
        idgen = idgen_cls(*idgen_args, **idgen_kwargs)
        ms_cls, ms_args, ms_kwargs = self._ms_params
        ms = ms_cls(*ms_args, **ms_kwargs)
        wh_cls, wh_args, wh_kwargs = self._wh_params
        wh = wh_cls(*wh_args, **wh_kwargs)
        return Catalog(idgen, ms, wh, **self._catalog_params)

    def __iter__(self) -> Iterator[Any]:
        if self.catalog is None:
            self.catalog = self._get_catalog()
        total_rank, total_workers = self.get_rank_and_workers()
        q = DatasetQuery(name=self.name, version=self.version, catalog=self.catalog)
        if self.num_samples > 0:
            q = q.sample(self.num_samples)
        q = q.chunk(total_rank, total_workers)
        stream = q.extract(*self.params, workers=self.workers, cache=self.cache)
        for row in stream:
            # Apply transforms
            if self.transform:
                try:
                    row = self.transform(row)
                except ValueError:
                    logger.warning("Skipping transform due to unsupported data types.")
                    self.transform = None
            yield row

    @staticmethod
    def get_rank_and_workers() -> tuple[int, int]:
        """Get combined rank and number of workers across all nodes."""
        try:
            world_rank = get_rank()
            world_size = get_world_size()
        except (RuntimeError, ValueError):
            world_rank = 0
            world_size = 1
        worker_info = get_worker_info()
        if worker_info:
            worker_rank = worker_info.id
            num_workers = worker_info.num_workers
        else:
            worker_rank = 0
            num_workers = 1
        total_workers = world_size * num_workers
        total_rank = world_rank * num_workers + worker_rank
        return total_rank, total_workers
