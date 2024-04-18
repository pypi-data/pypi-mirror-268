use alloy_dyn_abi::{DynSolType, DynSolValue, JsonAbiExt};
use alloy_json_abi::Function;
use alloy_primitives::{Address, FixedBytes, I256, U256};
use num_bigint::{BigInt, BigUint, Sign};
use pyo3::exceptions::PyTypeError;
use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyList, PyTuple};
use pyo3::Bound;

use std::str::FromStr;

fn extract(params: Bound<PyAny>, typ: &DynSolType) -> PyResult<DynSolValue> {
    match typ {
        DynSolType::String => params.extract().map(DynSolValue::String),
        DynSolType::Bool => params.extract().map(DynSolValue::Bool),
        DynSolType::Address => {
            let s: &str = params.extract()?;
            Address::from_str(s)
                .map(DynSolValue::Address)
                .map_err(|_| PyTypeError::new_err("Could not parse address"))
        }
        DynSolType::Int(size) => {
            let x: BigInt = params.extract()?;
            if x.bits() as usize > *size {
                return Err(PyTypeError::new_err(format!(
                    "Integer {} too large for {} bits",
                    x, size
                )));
            }
            let (sign, abs) = x.to_bytes_le();
            let mut i = I256::try_from_le_slice(abs.as_slice()).unwrap();
            if sign == Sign::Minus {
                i = -i;
            }

            Ok(DynSolValue::Int(i, *size))
        }
        DynSolType::Uint(size) => {
            let x: BigUint = params.extract()?;
            if x.bits() as usize > *size {
                return Err(PyTypeError::new_err(format!(
                    "Integer {} too large for {} bits",
                    x, size
                )));
            }

            Ok(DynSolValue::Uint(
                U256::from_le_slice(x.to_bytes_le().as_slice()),
                *size,
            ))
        }
        DynSolType::Bytes => {
            let as_bytes: PyResult<Vec<u8>> = params.extract();
            if let Ok(as_bytes) = as_bytes {
                Ok(DynSolValue::Bytes(as_bytes))
            } else {
                let as_str: String = params.extract()?;
                let Some(as_str) = as_str.strip_prefix("0x") else {
                    return Err(PyTypeError::new_err("Got non-hex str"));
                };

                hex::decode(as_str)
                    .map(DynSolValue::Bytes)
                    .map_err(|_| PyTypeError::new_err("Got non-hex str"))
            }
        }
        DynSolType::FixedBytes(size) => {
            let b: Vec<u8> = params.extract()?;
            if b.len() != *size {
                return Err(PyTypeError::new_err("Got wrong number of bytes"));
            }
            Ok(DynSolValue::FixedBytes(
                FixedBytes::try_from(b.as_slice())?,
                *size,
            ))
        }
        DynSolType::Tuple(types) => {
            let t = params.downcast::<PyTuple>()?;
            if t.len() != types.len() {
                return Err(PyTypeError::new_err("Got wrong number of items for tuple"));
            }

            t.into_iter()
                .zip(types.into_iter())
                .map(|(item, item_type)| extract(item, item_type))
                .collect::<Result<Vec<DynSolValue>, PyErr>>()
                .map(DynSolValue::Tuple)
        }
        DynSolType::Array(list_type) => {
            let l = params.downcast::<PyList>()?;

            l.into_iter()
                .map(|item| extract(item, list_type))
                .collect::<Result<Vec<DynSolValue>, PyErr>>()
                .map(DynSolValue::Array)
        }
        DynSolType::FixedArray(list_type, size) => {
            let l = params.downcast::<PyList>()?;

            if l.len() != *size {
                return Err(PyTypeError::new_err(
                    "Got wrong number of items for fixed array",
                ));
            }

            l.into_iter()
                .map(|item| extract(item, list_type))
                .collect::<Result<Vec<DynSolValue>, PyErr>>()
                .map(DynSolValue::FixedArray)
        }
        DynSolType::Function => Err(PyTypeError::new_err("Could not encode solidity function")),
    }
}

fn parse_type(ty: impl AsRef<str>) -> PyResult<DynSolType> {
    ty.as_ref()
        .parse()
        .map_err(|_| PyTypeError::new_err(format!("Could not parse type {}", ty.as_ref())))
}

fn encode_to_vec(params: Bound<PyAny>, signature: &str) -> PyResult<Vec<u8>> {
    let value = extract(params, &parse_type(signature)?)?;
    Ok(value.abi_encode())
}

#[pyfunction]
fn encode(params: Bound<PyAny>, signature: &str) -> PyResult<Py<PyBytes>> {
    let encoded = encode_to_vec(params, signature)?;
    Python::with_gil(|py| Ok(PyBytes::new_bound(py, &encoded).into()))
}

#[pyfunction]
fn encode_calldata(signature: &str, params: Bound<PyTuple>) -> PyResult<Py<PyBytes>> {
    let function = Function::parse(signature)
        .map_err(|_| PyTypeError::new_err("Could not parse function signature"))?;

    if params.len() != function.inputs.len() {
        return Err(PyTypeError::new_err(
            "Wrong number of argument for function",
        ));
    }

    let params: Vec<DynSolValue> = function
        .inputs
        .iter()
        .zip(params.into_iter())
        .map(|(func_param, param)| extract(param, &parse_type(&func_param.ty)?))
        .collect::<PyResult<Vec<DynSolValue>>>()?;

    let encoded = function
        .abi_encode_input(&params)
        .map_err(|_| PyTypeError::new_err("Could not encode parameters"))?;

    Python::with_gil(|py| Ok(PyBytes::new_bound(py, &encoded).into()))
}

#[pymodule]
fn allopy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode, m)?)?;
    m.add_function(wrap_pyfunction!(encode_calldata, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn encode_string() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let x = "asd".to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "string").unwrap();
            assert_eq!(encoded, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03asd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00");
        })
    }

    #[test]
    fn encode_bool() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let x = true.to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "bool").unwrap();
            assert_eq!(encoded, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01");
        })
    }

    #[test]
    fn encode_address() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let usdt = "0xdAC17F958D2ee523a2206206994597C13D831ec7";
            let x = usdt.to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "address").unwrap();
            assert_eq!(encoded, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xda\xc1\x7f\x95\x8d.\xe5#\xa2 b\x06\x99E\x97\xc1=\x83\x1e\xc7");
        })
    }

    #[test]
    fn encode_int() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let big: BigInt = (Into::<BigInt>::into(2).pow(240) + (4587263478562 as i64)) * -1;

            let x = big.to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "int256").unwrap();

            assert_eq!(encoded, b"\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xd3\xf1\xca4\xde");

            let x = (-1).to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "int8").unwrap();
            assert_eq!(encoded, b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff");

            let big: BigInt = Into::<BigInt>::into(2 as u32).pow(241) + (2378465283745 as u64);

            let x = big.to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "int256").unwrap();
            assert_eq!(encoded, b"\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02)\xc7\x94\x0e\xa1");

            let x = (7).to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "int16").unwrap();
            assert_eq!(encoded, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07");
        })
    }

    #[test]
    fn encode_uint() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let big: BigUint = Into::<BigUint>::into(2 as u32).pow(241) + (2378465283745 as u64);

            let x = big.to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "uint256").unwrap();
            assert_eq!(encoded, b"\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02)\xc7\x94\x0e\xa1");

            let x = (7).to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "uint16").unwrap();
            assert_eq!(encoded, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07");
        })
    }

    #[test]
    fn encode_bytes() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let x = b"\x12\x34".to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "bytes").unwrap();
            assert_eq!(encoded, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x124\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00");

            let x = "0x1234".to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x.as_ref().clone(), "bytes").unwrap();
            assert_eq!(encoded, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x124\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00");
        })
    }

    #[test]
    fn encode_fixed_bytes() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let b32 = b"\x12\x34\x56\x78\x90\x12\x34\x56\x78\x90\x12\x34\x56\x78\x90\x12\x34\x56\x78\x90\x12\x34\x56\x78\x90\x12\x34\x56\x78\x90\x12\x34";
            let x = b32.to_object(py).bind(py).clone();

            let encoded = encode_to_vec(x, "bytes32").unwrap();
            assert_eq!(
                encoded,
                b"\x124Vx\x90\x124Vx\x90\x124Vx\x90\x124Vx\x90\x124Vx\x90\x124Vx\x90\x124"
            );
        })
    }

    #[test]
    fn encode_tuple() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let x = (1, 2).to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x, "(int256,int256)").unwrap();
            assert_eq!(
                encoded,
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02"
            );
        })
    }

    #[test]
    fn encode_array() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let x = vec![1, 2, 3].to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x, "int256[]").unwrap();
            assert_eq!(
                encoded,
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03"
            );
        })
    }

    #[test]
    fn encode_fixed_array() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let x = vec![1, 2, 3].to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x, "int256[3]").unwrap();
            assert_eq!(
                encoded,
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03"
            );
        })
    }

    #[test]
    fn encode_nested() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let usdt = "0xdAC17F958D2ee523a2206206994597C13D831ec7";
            let obj = (
                usdt,
                vec![(1, b"\x12"), (2, b"\x34"), (3, b"\x56")],
                (true, false),
            );
            let x = obj.to_object(py).bind(py).clone();
            let encoded = encode_to_vec(x, "(address,(uint256,bytes)[],(bool,bool))").unwrap();
            assert_eq!(
                encoded,
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xda\xc1\x7f\x95\x8d.\xe5#\xa2 b\x06\x99E\x97\xc1=\x83\x1e\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x014\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01V\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            );
        })
    }

    #[test]
    fn test_encode_calldata() {
        pyo3::prepare_freethreaded_python();

        Python::with_gil(|py| {
            let signature = "execTransactionWithRole(address,uint256,bytes,uint8,uint16,bool)";
            let params = (
                "0x3943665751bd48263daaea7680d2852a7dfbe1db",
                0,
                "0x02329a290000000000000000000000000000000000000000000000000000000000000001",
                0,
                1,
                false,
            );

            let params = params
                .to_object(py)
                .bind(py)
                .clone()
                .downcast_into::<PyTuple>()
                .unwrap();

            let encoded: Vec<u8> = encode_calldata(signature, params)
                .unwrap()
                .extract(py)
                .unwrap();

            assert_eq!(
                encoded,
                b"i(\xe7K\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009CfWQ\xbdH&=\xaa\xeav\x80\xd2\x85*}\xfb\xe1\xdb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x022\x9a)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            );
        })
    }
}
