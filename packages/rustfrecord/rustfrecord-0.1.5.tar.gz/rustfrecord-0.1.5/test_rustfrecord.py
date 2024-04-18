import torch
from rustfrecord import Reader
from torch import Tensor


class TFRecordDataset(torch.utils.data.IterableDataset):
    def __init__(self, filename: str, compressed: bool = True, features: list = None):
        super().__init__()
        self.filename = filename
        self.compressed = compressed
        self.features = features

    def __iter__(self):
        reader = Reader(
            self.filename,
            compressed=self.compressed,
            features=self.features,
        )
        return iter(reader)


def test_dataset():
    filename = "data/002scattered.training_examples.tfrecord.gz"
    ds = TFRecordDataset(
        filename,
        compressed=True,
        features=[
            "label",
            "image/encoded",
            "image/shape",
        ],
    )
    print()

    loader = torch.utils.data.DataLoader(ds, batch_size=100)

    for batch in enumerate(loader):
        print(batch)

        # if i % 1000 == 0:
        #     print(i)

        # break # Exit after a single batch


def test_reader():
    filename = "data/002scattered.training_examples.tfrecord.gz"
    r = Reader(filename, compressed=True)

    for i, features in enumerate(r):
        """
        >>> print(i, features.keys())
        [
            "variant_type",
            "image/encoded",
            "image/shape",
            "variant/encoded",
            "label",
            "alt_allele_indices/encoded",
            "locus",
            "sequencing_type",
        ]
        """

        label: Tensor = features["label"]
        shape = torch.Size(tuple(features["image/shape"]))
        image: Tensor = features["image/encoded"][0].reshape(shape)

        print(i, label, image.shape)

        if i >= 3:
            break
