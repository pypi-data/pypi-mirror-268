#![allow(clippy::unused_unit)]
use polars::prelude::*;
use pyo3_polars::{derive::polars_expr, export::polars_ffi::version_0::SeriesExport};
use serde::Deserialize;
use canparse::pgn::{PgnLibrary, SpnDefinition, ParseMessage};
use polars_core::with_match_physical_numeric_type;


#[derive(Deserialize)]
struct SignalNameKwargs {
    path_to_dbc: String,
    signal_name: String,
}


#[polars_expr(output_type=Float32)]
fn decode_can_message(inputs: &[Series], kwargs: SignalNameKwargs) -> PolarsResult<Series> {
    let arr_series = &inputs[0].list()?;
    let lib = PgnLibrary::from_dbc_file(&kwargs.path_to_dbc)?;
    let signal_def: &SpnDefinition = lib.get_spn(&kwargs.signal_name).unwrap();

    let out: Vec<Option<f32>> = arr_series.into_iter().map(
        |option_value| match option_value {
            Some(option_value) => {
                let binary_vec: Vec<i32> = option_value.i32().unwrap().to_vec_null_aware().left().unwrap();
                let mut binary_arr: [u8; 8] = [0; 8];
                for i in 0..8 {
                    binary_arr[i] = binary_vec[i] as u8;
                }
                let decoded_msg = signal_def.parse_message(&binary_arr).unwrap();
                Some(decoded_msg)
            },
            _ => None,
        }
    ).collect();
    Ok(Series::new(&kwargs.signal_name, out))
}
