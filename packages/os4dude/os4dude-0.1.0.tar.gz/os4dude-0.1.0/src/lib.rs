use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    //add a os4dude prefix to the sum
    Ok(()).map(|_| format!("os4dude: {}", a + b))
    //Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn os4dude(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}
