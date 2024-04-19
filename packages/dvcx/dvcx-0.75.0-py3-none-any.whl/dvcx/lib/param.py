from collections.abc import Iterable
from typing import TYPE_CHECKING, Callable, Optional

import attrs

from dvcx.query.schema import Object, UDFParameter

if TYPE_CHECKING:
    from dvcx.catalog import Catalog
    from dvcx.dataset import DatasetRow as Row


class Image(Object):
    def __init__(
        self,
        formats: Optional[Iterable[str]] = None,
        mode: str = "RGB",
        size: Optional[tuple[int, int]] = None,
        transform: Optional[Callable] = None,
    ):
        """
        Return image from file object, optionally resized/transformed.

        Args:
            formats (Iterable[str]): PIL.Image formats.
            mode (str): PIL.Image mode.
            size (tuple[int, int]): Size in (width, height) pixels for resizing.
            transform (Callable): Torchvision v1 or other transform to apply.
        """
        self.formats = formats
        self.mode = mode
        self.size = size
        self.transform = transform
        super().__init__(reader=self.load_img)

    def load_img(self, raw):
        try:
            import PIL.Image
        except ImportError as exc:
            raise ImportError(
                "Missing dependency Pillow for computer vision:\n"
                "To install run:\n\n"
                "  pip install 'dvcx[cv]'\n"
            ) from exc

        img = PIL.Image.open(raw, formats=self.formats).convert(self.mode)
        if self.size:
            img = img.resize(self.size)
        if self.transform:
            img = self.transform(img)
        return img


@attrs.define(slots=False)
class Label(UDFParameter):
    """
    Encode column value as an index into the provided list of labels.
    """

    column: str
    classes: list

    def get_value(self, catalog: "Catalog", row: "Row", **kwargs) -> int:
        label = row[self.column]
        return self.classes.index(label)


class Text(UDFParameter):
    def __init__(self, column: str, tokenizer: Callable, **kwargs):
        """
        Tokenize and otherwise transform text column.

        Args:
            column (str): Name of column containing text.
            tokenizer (Callable): Tokenizer to use to tokenize objects.
            kwargs (dict): Additional kwargs to pass when calling tokenizer.
        """
        self.column = column
        self.tokenizer = tokenizer
        self.kwargs = kwargs

        self.hf = False
        try:
            from transformers.tokenization_utils_base import PreTrainedTokenizerBase

            if isinstance(tokenizer, PreTrainedTokenizerBase):
                self.hf = True
        except ImportError:
            pass

    def get_value(self, catalog: "Catalog", row: "Row", **kwargs) -> int:
        text = row[self.column]
        if self.hf:
            return self.tokenizer([text], **self.kwargs).input_ids[0]
        return self.tokenizer([text], **self.kwargs)[0]
