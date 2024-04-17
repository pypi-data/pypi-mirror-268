use std::{collections::HashMap, fs, io::Read, path::Path};

use anyhow::{Context, Result};
use flate2::read::GzDecoder;
use tch::Tensor;
use tfrecord::{Example, ExampleIter, FeatureKind, RecordReaderConfig};

pub struct Reader {
    example_iter: ExampleIter<Box<dyn Read + Send>>,
}

impl Reader {
    pub fn new(filename: &str, compressed: bool) -> Result<Self> {
        let path = Path::new(filename);

        let conf = RecordReaderConfig {
            check_integrity: false,
        };

        let file = fs::File::open(path).with_context(|| format!("failed to open {path:?}"))?;

        let reader: Box<dyn Read + Send> = if compressed {
            Box::new(GzDecoder::new(file))
        } else {
            Box::new(file)
        };

        let example_iter = ExampleIter::from_reader(reader, conf);

        Ok(Self { example_iter })
    }
}

impl Iterator for Reader {
    // Iterate over Examples.
    //
    // Comment from example.proto:
    //
    // An Example is a mostly-normalized data format for storing data for training and inference.
    // It contains a key-value store (features); where each key (string) maps to a Feature message
    // (which is one of packed BytesList, FloatList, or Int64List).

    type Item = tfrecord::Result<HashMap<String, Tensor>>;

    fn next(&mut self) -> Option<Self::Item> {
        self.example_iter.next().map(|e| e.map(example_to_hashmap))
    }
}

fn example_to_hashmap(example: Example) -> HashMap<String, Tensor> {
    example
        .into_iter()
        .map(|(name, feature)| {
            let tensor = match feature.into_kinds() {
                Some(FeatureKind::F32(value)) => Tensor::from_slice(&value),
                Some(FeatureKind::I64(value)) => Tensor::from_slice(&value),
                Some(FeatureKind::Bytes(value)) => Tensor::from_slice2(&value),
                None => Tensor::new(),
            };
            (name, tensor)
        })
        .collect()
}
