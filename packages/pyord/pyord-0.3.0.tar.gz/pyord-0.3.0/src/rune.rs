use pyo3::prelude::*;

use ordinals::Rune;

/// Rune
/// :param n: The rune number
/// :type n: int
#[pyclass(name="Rune")]
#[derive(Debug, PartialEq, Copy, Clone, PartialOrd, Ord, Eq)]
pub struct PyRune(pub Rune);


#[pymethods]
impl PyRune {
    #[new]
    pub fn new(n: u128) -> Self {
        PyRune(Rune(n))
    }

    /// the number (id) of the rune
    /// :rtype: int
    #[getter]
    pub fn n(&self) -> u128 {
        self.0 .0
    }

    /// the name of the rune as a string
    /// :rtype: str
    #[getter]
    pub fn name(&self) -> String {
        self.0.to_string()
    }

    pub fn __repr__(&self) -> String {
        format!("Rune(n={}, name='{}')", self.n(), self.name())
    }

    /// convert the string representation of the rune to a rune
    /// :param s: the string representation of the rune
    /// :type s: str
    /// :rtype: Rune
    #[staticmethod]
    pub fn from_str(s: &str) -> Self {
        Self(s.parse::<Rune>().unwrap())
    }
}
