use pyo3::prelude::*;

/// Just says hi
#[pyfunction]
fn hello_qactus() -> PyResult<String> {
    Ok("Hello, qactus :D".into())
}

/// Quantum Circuit Analysis and Simulation
#[pymodule]
fn qactus(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_qactus, m)?)?;
    Ok(())
}
