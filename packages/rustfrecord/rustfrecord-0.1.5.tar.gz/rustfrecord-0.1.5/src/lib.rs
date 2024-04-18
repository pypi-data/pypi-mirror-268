use std::collections::HashMap;

use pyo3::exceptions::{PyOSError, PyValueError};
use pyo3::prelude::*;
use pyo3_tch::PyTensor;

mod pyo3_tch;
mod tfrecord_reader;

#[pyclass]
struct Reader {
    inner: tfrecord_reader::Reader,
}

#[pymethods]
impl Reader {
    #[new]
    fn new(filename: &str, compressed: bool, features: Option<Vec<String>>) -> PyResult<Self> {
        let features = features.unwrap_or_default();
        tfrecord_reader::Reader::new(filename, compressed, &features)
            .map(|r| Reader { inner: r })
            .map_err(|e| PyOSError::new_err(format!("{e:?}")))
    }

    fn __iter__(slf: PyRef<'_, Self>) -> PyRef<'_, Self> {
        slf
    }

    fn __next__(mut slf: PyRefMut<'_, Self>) -> PyResult<Option<HashMap<String, PyTensor>>> {
        let wrap_pytensor =
            |hm: HashMap<_, _>| hm.into_iter().map(|(k, v)| (k, PyTensor(v))).collect();

        slf.inner
            .next()
            .map(|r| {
                r.map(wrap_pytensor)
                    .map_err(|e| PyValueError::new_err(format!("{e:?}")))
            })
            .transpose()
    }
}

#[pymodule]
fn rustfrecord(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.py().import_bound("torch")?;
    m.add_class::<Reader>()?;
    Ok(())
}
