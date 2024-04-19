use pyo3::prelude::*;

use ordinals::Cenotaph;

use super::flaw::PyFlaw;
use super::rune::PyRune;
use super::rune_id::PyRuneId;

/// Cenotaph
/// :type etching: typing.Optional[Rune]
/// :type flaw: typing.Optional[Flaw]
/// :type mint: typing.Optional[RuneId]
#[pyclass(name="Cenotaph")]
#[derive(Debug, PartialEq)]
pub struct PyCenotaph(pub Cenotaph);


#[pymethods]
impl PyCenotaph {
    #[new]
    #[pyo3(signature = (etching=None, flaw=None, mint=None))]
    pub fn new(
        etching: Option<PyRune>,
        flaw: Option<PyFlaw>,
        mint: Option<PyRuneId>,
    ) -> Self {
        Self(Cenotaph {
            etching: etching.map(|e| e.0),
            flaw: flaw.map(|e| e.0),
            mint: mint.map(|m| m.0),
        })
    }

    pub fn __eq__(&self, other: &PyCenotaph) -> bool {
        self.0 == other.0
    }

    /// :rtype: str
    pub fn __repr__(&self) -> String {
        format!(
            "Cenotaph(flaws={}, etching={}, mint={})",
            self.flaw()
                .map(|f| f.__repr__())
                .unwrap_or_else(|| "None".to_string()),
            self.etching()
                .map(|e| e.__repr__())
                .unwrap_or_else(|| "None".to_string()),
            self.mint()
                .map(|m| m.__repr__())
                .unwrap_or_else(|| "None".to_string())
        )
    }

    /// :rtype: typing.Optional[Flaw]
    #[getter]
    pub fn flaw(&self) -> Option<PyFlaw> {
        self.0.flaw.map(|f| PyFlaw(f))
    }

    /// :rtype: typing.Optional[Rune]
    #[getter]
    pub fn etching(&self) -> Option<PyRune> {
        self.0.etching.map(|e| PyRune(e))
    }

    /// :rtype: typing.Optional[RuneId]
    #[getter]
    pub fn mint(&self) -> Option<PyRuneId> {
        self.0.mint.map(|m| PyRuneId(m))
    }

    /// :rtype: bool
    #[getter]
    pub fn is_cenotaph(&self) -> bool {
        true
    }
}
