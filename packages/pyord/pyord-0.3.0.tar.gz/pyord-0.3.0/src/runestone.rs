use pyo3::prelude::*;
use pyo3::types::PyBytes;

use ordinals::Artifact;
use ordinals::Runestone;

use crate::utils::hex_to_bitcoin_tx;

use super::edict::PyEdict;
use super::etching::PyEtching;
use super::rune_id::PyRuneId;
use super::cenotaph::PyCenotaph;

/// Runestone
/// :type edicts: typing.Optional[typing.Iterable[Edict]]
/// :type etching: typing.Optional[Etching]
/// :type mint: typing.Optional[RuneId]
/// :type pointer: typing.Optional[int]
#[pyclass(name="Runestone")]
#[derive(Debug, PartialEq)]
pub struct PyRunestone(pub Runestone);


#[pymethods]
impl PyRunestone {
    #[new]
    #[pyo3(signature = (edicts=None, etching=None, mint=None, pointer=None))]
    pub fn new(
        edicts: Option<Vec<PyEdict>>,
        etching: Option<PyEtching>,
        mint: Option<PyRuneId>,
        pointer: Option<u32>,
    ) -> Self {
        PyRunestone(Runestone {
            edicts: edicts.unwrap_or_default().into_iter().map(|e| e.0).collect(),
            etching: etching.map(|e| e.0),
            mint: mint.map(|m| m.0),
            pointer,
        })
    }

    /// Return a Runestone or Cenotaph from a Bitcoin transaction, or None if the transaction
    /// contains no Runestone
    /// :type hex_tx: str
    /// :rtype: typing.Union[Runestone, Cenotaph, None]
    #[staticmethod]
    pub fn decipher_hex(py: Python, hex_tx: &str) -> PyResult<Option<PyObject>> {
        let tx = hex_to_bitcoin_tx(hex_tx)?;
        let result = Runestone::decipher(&tx);
        match result {
            None => Ok(None),
            Some(artifact) => match artifact {
                Artifact::Cenotaph(cenotaph) => Ok(Some(PyCenotaph(cenotaph).into_py(py))),
                Artifact::Runestone(runestone) => Ok(Some(PyRunestone(runestone).into_py(py))),
            },
        }
    }

    /// get the scriptPubKey of the Runestone
    /// :rtype: bytes
    pub fn encipher(&self, py: Python) -> PyObject {
        let buffer = self.0.encipher().into_bytes();
        // TODO: check that this doesn't leak memory
        PyBytes::new(py, &buffer).into()
    }

    pub fn __repr__(&self) -> String {
        format!(
            "Runestone(edicts={}, etching={}, mint={}, pointer={})",
            format!(
                "[{}]",
                self.edicts().iter().map(|e| e.__repr__()).collect::<Vec<String>>().join(", ")
            ),
            self.etching().map(|e| e.__repr__()).unwrap_or("None".to_string()),
            self.mint().map(|m| m.__repr__()).unwrap_or("None".to_string()),
            self.pointer().map(|i| i.to_string()).unwrap_or("None".to_string()),
        )
    }

    pub fn __eq__(&self, other: &PyRunestone) -> bool {
        self.0 == other.0
    }

    /// :rtype: typing.Optional[Etching]
    #[getter]
    pub fn etching(&self) -> Option<PyEtching> {
        self.0.etching.map(|e| PyEtching(e))
    }

    /// :rtype: typing.List[Edict]
    #[getter]
    pub fn edicts(&self) -> Vec<PyEdict> {
        self.0.edicts.iter().map(|e| PyEdict(*e)).collect()
    }

    /// :rtype: typing.Optional[RuneId]
    #[getter]
    pub fn mint(&self) -> Option<PyRuneId> {
        self.0.mint.map(|m| PyRuneId(m))
    }

    /// :rtype: typing.Optional[int]
    #[getter]
    pub fn pointer(&self) -> Option<u32> {
        self.0.pointer
    }

    /// :rtype: bool
    #[getter]
    pub fn is_cenotaph(&self) -> bool {
        false
    }
}
