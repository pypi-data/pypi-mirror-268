import re

import pytest

from dvcx.catalog import Catalog
from dvcx.catalog.loader import get_id_generator, get_metastore, get_warehouse
from dvcx.error import DatasetNotFoundError
from dvcx.query import DatasetQuery, Session


@pytest.fixture
def catalog(tmp_path):
    id_generator = get_id_generator()
    return Catalog(
        id_generator,
        get_metastore(id_generator),
        get_warehouse(id_generator),
        str(tmp_path / "cache"),
        str(tmp_path / "tmp"),
    )


def test_ephemeral_dataset_naming(catalog):
    session_name = "qwer45"

    with pytest.raises(ValueError):
        Session("wrong-ds_name", catalog=catalog)

    with Session(session_name, catalog=catalog) as session:
        ds_name = "my_test_ds12"
        session.catalog.create_dataset(ds_name)
        ds_tmp = DatasetQuery(name=ds_name, session=session).save()
        session_uuid = f"[0-9a-fA-F]{{{Session.SESSION_UUID_LEN}}}"
        table_uuid = f"[0-9a-fA-F]{{{Session.TEMP_TABLE_UUID_LEN}}}"

        name_prefix = f"{Session.DATASET_PREFIX}{session_name}"
        pattern = rf"^{name_prefix}_{session_uuid}_{table_uuid}$"

        assert re.match(pattern, ds_tmp.name) is not None


def test_global_session_naming(catalog):
    session_uuid = f"[0-9a-fA-F]{{{Session.SESSION_UUID_LEN}}}"
    table_uuid = f"[0-9a-fA-F]{{{Session.TEMP_TABLE_UUID_LEN}}}"

    ds_name = "qwsd"
    catalog.create_dataset(ds_name)
    ds_tmp = DatasetQuery(name=ds_name).save()
    global_prefix = f"{Session.DATASET_PREFIX}{Session.GLOBAL_SESSION_NAME}"
    pattern = rf"^{global_prefix}_{session_uuid}_{table_uuid}$"
    assert re.match(pattern, ds_tmp.name) is not None


def test_ephemeral_dataset_lifecycle(catalog):
    session_name = "asd3d4"
    with Session(session_name, catalog=catalog) as session:
        ds_name = "my_test_ds12"
        session.catalog.create_dataset(ds_name)
        ds_tmp = DatasetQuery(name=ds_name, session=session).save()

        assert isinstance(ds_tmp, DatasetQuery)
        assert ds_tmp.name != ds_name
        assert ds_tmp.name.startswith(Session.DATASET_PREFIX)
        assert session_name in ds_tmp.name

        ds = catalog.get_dataset(ds_tmp.name)
        assert ds is not None

    with pytest.raises(DatasetNotFoundError):
        catalog.get_dataset(ds_tmp.name)
