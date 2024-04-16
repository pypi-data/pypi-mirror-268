import open_clip
import torch
from torch.nn.functional import cosine_similarity
from torch.utils.data import DataLoader

from dvcx.error import DatasetNotFoundError
from dvcx.lib.param import Image, Text
from dvcx.query import C, DatasetQuery, udf
from dvcx.query.schema import Object
from dvcx.sql.types import String

source = "gcs://dvcx-50k-laion-files/000000/"


def load_text(raw):
    return raw.read().decode("utf-8")


@udf(params=("name",), output={"stem": String})
def get_stem(name):
    return (name.split(".")[0],)


@udf(params=(Object(load_text),), output={"caption": String})
def get_caption(text):
    return (text,)


def create_dataset():
    imgs = DatasetQuery(source).filter(C.name.glob("*.jpg")).add_signals(get_stem)
    captions = (
        DatasetQuery(source)
        .filter(C.name.glob("*.txt"))
        .add_signals(get_stem)
        .add_signals(get_caption)
    )
    return imgs.join(captions.select("stem", "caption"), "stem").save("laion-50k")


if __name__ == "__main__":
    try:
        q = DatasetQuery(name="laion-50k")
    except DatasetNotFoundError:
        q = create_dataset()

    model, _, preprocess = open_clip.create_model_and_transforms(
        "ViT-B-32", pretrained="laion2b_s34b_b79k"
    )
    tokenizer = open_clip.get_tokenizer("ViT-B-32")

    ds = q.to_pytorch(Image(transform=preprocess), Text("caption", tokenizer=tokenizer))
    loader = DataLoader(ds, batch_size=16)

    similarity_sum = 0
    row_count = 0
    with torch.no_grad(), torch.cuda.amp.autocast():
        for image, text in loader:
            image_features = model.encode_image(image)
            text_features = model.encode_text(text)

            similarity_sum += (
                cosine_similarity(image_features, text_features).sum().item()
            )
            row_count += len(image_features)

    print("Average cosine similarity:", similarity_sum / row_count)
