use pyo3::prelude::*;

/// Just says hi
#[pyfunction]
fn hello_caqtus() -> PyResult<String> {
    Ok("Hello, caqtus :D".into())
}

/// Quantum Circuit Analysis and Simulation
#[pymodule]
fn caqtus(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_caqtus, m)?)?;
    Ok(())
}
