use pyo3::prelude::*;

use ordinals::Terms;

/// :type amount: typing.Optional[int]
/// :type cap: typing.Optional[int]
/// :type height: tuple[typing.Optional[int], typing.Optional[int]]
/// :type offset: tuple[typing.Optional[int], typing.Optional[int]]
#[pyclass(name="Terms")]
#[derive(Debug, PartialEq, Copy, Clone)]
pub struct PyTerms(pub Terms);

#[pymethods]
impl PyTerms {
    #[new]
    #[pyo3(signature = (amount=None, cap=None, height=(None, None), offset=(None, None)))]
    pub fn new(
        amount: Option<u128>,
        cap: Option<u128>,
        height: Option<(Option<u64>, Option<u64>)>,
        offset: Option<(Option<u64>, Option<u64>)>,
    ) -> Self {
        Self(Terms {
            amount,
            cap,
            height: height.unwrap_or_else(|| (None, None)),
            offset: offset.unwrap_or_else(|| (None, None)),
        })
    }

    pub fn __repr__(&self) -> String {
        format!(
            "Terms(amount={}, cap={}, height=({},{}), offset=({},{}))",
            self.amount().map(|i| i.to_string()).unwrap_or("None".to_string()),
            self.cap().map(|i| i.to_string()).unwrap_or("None".to_string()),
            self.height().0.map(|i| i.to_string()).unwrap_or("None".to_string()),
            self.height().1.map(|i| i.to_string()).unwrap_or("None".to_string()),
            self.offset().0.map(|i| i.to_string()).unwrap_or("None".to_string()),
            self.offset().1.map(|i| i.to_string()).unwrap_or("None".to_string()),
        )
    }

    /// :rtype: typing.Optional[int]
    #[getter]
    pub fn amount(&self) -> Option<u128> {
        self.0.amount
    }

    /// :rtype: typing.Optional[int]
    #[getter]
    pub fn cap(&self) -> Option<u128> {
        self.0.cap
    }

    /// :rtype: tuple[typing.Optional[int], typing.Optional[int]]
    #[getter]
    pub fn height(&self) -> (Option<u64>, Option<u64>) {
        self.0.height
    }

    /// :rtype: tuple[typing.Optional[int], typing.Optional[int]]
    #[getter]
    pub fn offset(&self) -> (Option<u64>, Option<u64>) {
        self.0.offset
    }
}