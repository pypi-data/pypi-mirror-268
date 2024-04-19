use pyo3::prelude::*;

use ordinals::Edict;
use super::rune_id::PyRuneId;

/// :type id: RuneId
/// :type amount: int
/// :type output: int
#[pyclass(name="Edict")]
#[derive(Debug, PartialEq, Copy, Clone)]
pub struct PyEdict(pub Edict);


#[pymethods]
impl PyEdict {
    #[new]
    pub fn new(
        id: PyRuneId,
        amount: u128,
        output: u32,
    ) -> Self {
        PyEdict(Edict {
            id: id.0,
            amount,
            output,
        })
    }

    pub fn __repr__(&self) -> String {
        format!(
            "Edict(id={}, amount={}, output={})",
            self.id().__repr__(),
            self.amount(),
            self.output()
        )
    }

    /// :rtype: RuneId
    #[getter]
    pub fn id(&self) -> PyRuneId {
        PyRuneId(self.0.id)
    }

    /// :rtype: int
    #[getter]
    pub fn amount(&self) -> u128 {
        self.0.amount
    }

    /// :rtype: int
    #[getter]
    pub fn output(&self) -> u32 {
        self.0.output
    }
}
