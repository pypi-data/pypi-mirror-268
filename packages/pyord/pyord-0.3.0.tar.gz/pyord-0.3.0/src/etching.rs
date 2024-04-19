use pyo3::prelude::*;
use ordinals::Etching;

use super::terms::PyTerms;
use super::rune::PyRune;

/// :type divisibility: typing.Optional[int]
/// :type premine: typing.Optional[int]
/// :type rune: typing.Optional[Rune]
/// :type spacers: typing.Optional[int]
/// :type symbol: typing.Optional[str]
/// :type terms: typing.Optional[Terms]
/// :type turbo: typing.Optional[bool]
#[pyclass(name="Etching")]
#[derive(Debug, PartialEq, Copy, Clone)]
pub struct PyEtching(pub Etching);

#[pymethods]
impl PyEtching {
    #[new]
    pub fn new(
        divisibility: Option<u8>,
        premine: Option<u128>,
        rune: Option<PyRune>,
        spacers: Option<u32>,
        symbol: Option<char>,
        terms: Option<PyTerms>,
        turbo: Option<bool>,
    ) -> Self {
        Self(Etching {
            divisibility,
            premine,
            rune: rune.map(|r| r.0),
            spacers,
            symbol,
            terms: terms.map(|m| m.0),
            turbo: turbo.unwrap_or(false),
        })
    }

    pub fn __repr__(&self) -> String {
        format!(
            "Etching(divisibility={}, premine={}, rune={}, spacers={}, symbol={}, terms={}, turbo={})",
            self.divisibility().map(|i| i.to_string()).unwrap_or("None".to_string()),
            self.premine().map(|i| i.to_string()).unwrap_or("None".to_string()),
            self.rune().map(|r| r.__repr__()).unwrap_or("None".to_string()),
            self.spacers().map(|i| i.to_string()).unwrap_or("None".to_string()),
            self.symbol().map(|s| format!("'{}'", s.to_string())).unwrap_or("None".to_string()),
            self.terms().map(|m| m.__repr__()).unwrap_or("None".to_string()),
            if self.turbo() { "True" } else { "False" },
        )
    }

    /// :rtype: typing.Optional[int]
    #[getter]
    pub fn divisibility(&self) -> Option<u8> {
        self.0.divisibility
    }

    /// :rtype: typing.Optional[int]
    #[getter]
    pub fn premine(&self) -> Option<u128> {
        self.0.premine
    }

    /// :rtype: typing.Optional[Rune]
    #[getter]
    pub fn rune(&self) -> Option<PyRune> {
        self.0.rune.map(|r| PyRune(r))
    }

    /// :rtype: int
    #[getter]
    pub fn spacers(&self) -> Option<u32> {
        self.0.spacers
    }

    /// :rtype: typing.Optional[str]
    #[getter]
    pub fn symbol(&self) -> Option<char> {
        self.0.symbol
    }

    /// :rtype: typing.Optional[Terms]
    #[getter]
    pub fn terms(&self) -> Option<PyTerms> {
        self.0.terms.map(|m| PyTerms(m))
    }

    /// :rtype: bool
    #[getter]
    pub fn turbo(&self) -> bool {
        self.0.turbo
    }
}
