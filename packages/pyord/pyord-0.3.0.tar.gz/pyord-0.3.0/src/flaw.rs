use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;

use ordinals::Flaw;


/// A Flaw in a Runestone that makes it a Cenotaph
/// :param n: Flaw as integer
/// :type n: int
#[pyclass(name="Flaw")]
#[derive(Debug, PartialEq, Copy, Clone)]
pub struct PyFlaw(pub Flaw);

const ALL_FLAWS: [Flaw; 10] = [
    Flaw::EdictOutput,
    Flaw::EdictRuneId,
    Flaw::InvalidScript,
    Flaw::Opcode,
    Flaw::SupplyOverflow,
    Flaw::TrailingIntegers,
    Flaw::TruncatedField,
    Flaw::UnrecognizedEvenTag,
    Flaw::UnrecognizedFlag,
    Flaw::Varint,
];


#[pymethods]
impl PyFlaw {
    #[new]
    pub fn new(
        n: u32,
    ) -> PyResult<Self> {
        for flaw in ALL_FLAWS.into_iter() {
            if flaw as u32 == n {
                return Ok(Self(flaw));
            }
        }
        Err(PyValueError::new_err(format!("Invalid flaw number: {}", n)))
    }

    /// :rtype: list[Flaw]
    #[staticmethod]
    pub fn all() -> Vec<Self> {
        ALL_FLAWS.into_iter().map(|flaw| Self(flaw)).collect()
    }

    pub fn __eq__(&self, other: &PyFlaw) -> bool {
        self.0 == other.0
    }

    pub fn __repr__(&self) -> String {
        format!("Flaw(value={}, reason='{}')", self.__int__(), self.reason())
    }

    pub fn __int__(&self) -> u32 {
        self.0 as u32
    }

    /// :rtype: str
    #[getter]
    pub fn reason(&self) -> String {
        self.0.to_string()
    }
}
