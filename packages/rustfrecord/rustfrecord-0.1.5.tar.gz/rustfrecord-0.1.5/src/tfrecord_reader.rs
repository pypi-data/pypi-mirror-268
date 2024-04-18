use std::{
    collections::{HashMap, HashSet},
    fs,
    io::Read,
    path::Path,
};

use anyhow::{Context, Result};
use flate2::read::GzDecoder;
use tch::Tensor;
use tfrecord::{Example, ExampleIter, FeatureKind, RecordReaderConfig};

pub struct Reader {
    example_iter: ExampleIter<Box<dyn Read + Send>>,
    features: HashSet<String>,
}

impl Reader {
    pub fn new(filename: &str, compressed: bool, features: &[impl AsRef<str>]) -> Result<Self> {
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

        Ok(Self {
            example_iter,
            features: features.iter().map(|s| s.as_ref().to_string()).collect(),
        })
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
        self.example_iter
            .next()
            .map(|e| e.map(|e| example_to_hashmap(e, &self.features)))
    }
}

fn example_to_hashmap(example: Example, features: &HashSet<String>) -> HashMap<String, Tensor> {
    example
        .into_iter()
        .filter(|(name, _)| features.is_empty() || features.contains(name))
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
