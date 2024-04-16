from typing import TYPE_CHECKING, Any

import attrs

from dvcx.query.schema import Object, UDFParameter

if TYPE_CHECKING:
    from dvcx.catalog import Catalog
    from dvcx.dataset import DatasetRow as Row


def Image(formats=None, mode="RGB", size=None, transform=None):  # noqa: N802
    try:
        import PIL.Image
    except ImportError as exc:
        raise ImportError(
            "Missing dependency Pillow for computer vision:\n"
            "To install run:\n\n"
            "  pip install 'dvcx[cv]'\n"
        ) from exc

    def load_img(raw):
        img = PIL.Image.open(raw, formats=formats).convert(mode)
        if size:
            img = img.resize(size)
        if transform:
            img = transform(img)
        return img

    return Object(load_img)


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
    """
    Tokenize and otherwise transform text column.

    Args:
        column (str): Name of column containing text.
        tokenizer (Any): Tokenizer to use to tokenize objects.
        kwargs (dict): Additional kwargs to pass when calling tokenizer.
    """

    def __init__(self, column: str, tokenizer: Any, **kwargs):
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
