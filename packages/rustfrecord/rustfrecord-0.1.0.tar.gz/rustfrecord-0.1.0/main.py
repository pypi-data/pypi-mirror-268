import torch
from torch import Tensor

from rustfrecord import Reader

filename = "data/002scattered.training_examples.tfrecord.gz"
r = Reader(filename, compressed=True)


for (i, features) in enumerate(r):
    # print(i, features.keys())
    # ['variant_type',
    #  'image/encoded',
    #  'image/shape',
    #  'variant/encoded',
    #  'label',
    #  'alt_allele_indices/encoded',
    #  'locus',
    #  'sequencing_type']

    label: Tensor = features['label']
    shape = torch.Size(tuple(features['image/shape']))
    image: Tensor = features['image/encoded'][0].reshape(shape)

    print(i, label, image.shape)

    # break
