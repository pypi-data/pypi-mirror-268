# rustfrecord

The [TFRecord format](https://www.tensorflow.org/tutorials/load_data/tfrecord) is a simple format for storing a sequence of binary records.

This package implements a high-performance reader for  `Example` records stored in TFRecord files.

Examples are loaded into native PyTorch `Tensor`s.

## Installation

The wheel can be installed on any Linux system with Python 3.8 or higher:

    pip3 install rustfrecord

## Getting Started

The `Reader` class reads TFRecord files and yields `Dict[str, Tensor]` objects.

```python
import torch
from torch import Tensor
from rustfrecord import Reader

filename = "data/002scattered.training_examples.tfrecord.gz"
r = Reader(filename, compressed=True)

for i, features in enumerate(r):
    print(features.keys())
    # ['variant_type', 'image/encoded', 'image/shape',
    #  'variant/encoded', 'label', 'alt_allele_indices/encoded',
    #  'locus', 'sequencing_type']

    label: Tensor = features['label']
    shape = torch.Size(tuple(features['image/shape']))
    image: Tensor = features['image/encoded'][0].reshape(shape)

    print(i, label, image.shape)
```

## Development

To develop this package (not just use it), you need to install the Rust compiler and the Python development headers.

    pip install uv
    uv venv
    source .venv/bin/activate

    uv pip compile pyproject.toml -o requirements.txt
    uv pip install -r requirements.txt

    export LIBTORCH_USE_PYTORCH=1
    CARGO_TARGET_DIR=target_maturin maturin develop

    python main.py