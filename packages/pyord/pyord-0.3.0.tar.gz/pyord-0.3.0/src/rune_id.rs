use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;

use ordinals::RuneId;

/// RuneId
/// :param block: Etching block height
/// :type block: int
/// :param tx: Etching transaction index
/// :type tx: int
#[pyclass(name="RuneId")]
#[derive(Debug, PartialEq, Copy, Clone, Hash, PartialOrd, Ord, Eq)]
pub struct PyRuneId(pub RuneId);

#[pymethods]
impl PyRuneId {
    #[new]
    pub fn new(block: u64, tx: u32) -> Self {
        PyRuneId(RuneId { block, tx })
    }

    pub fn __eq__(&self, other: Self) -> bool {
        self.0 == other.0
    }

    /// :rtype: str
    pub fn __repr__(&self) -> String {
        format!("RuneId(block={}, tx={})", self.0.block, self.0.tx)
    }

    /// Parse the RuneId from a string "block:tx"
    /// :param s: block height and tx separated by a colon
    /// :type s: str
    /// :rtype: RuneId
    #[staticmethod]
    pub fn from_str(s: &str) -> PyResult<Self> {
        s.parse::<RuneId>().map(Self).map_err(|_| PyValueError::new_err("Invalid RuneId"))
    }

    /// :type next: RuneId
    /// :rtype: typing.Optional[typing.Tuple[int, int]]
    pub fn delta(&self, next: PyRuneId) -> Option<(u128, u128)> {
        let (block, tx) = self.0.delta(next.0)?;
        Some((block, tx))
    }

    /// :type block: int
    /// :type tx: int
    /// :rtype: typing.Optional[RuneId]
    pub fn next(&self, block: u128, tx: u128) -> Option<Self> {
        self.0.next(block, tx).map(Self)
    }

    /// :rtype: int
    #[getter]
    pub fn block(&self) -> u64 {
        self.0.block
    }

    /// :rtype: int
    #[getter]
    pub fn tx(&self) -> u32 {
        self.0.tx
    }
}
