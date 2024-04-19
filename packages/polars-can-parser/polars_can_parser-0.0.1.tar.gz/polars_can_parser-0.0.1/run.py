import polars as pl
# from polars_can_parser import pig_latinnify
from polars_can_parser import decode_can_message

df = pl.read_parquet("example.parquet")
# print(df.schema)

# df = df.select(pl.col("data").cas/t(pl.List(pl.UInt8)))

print(df.schema)

print(df[:10])

print(df.select(decode_can_message("data", path_to_dbc='j1939.dbc', signal_name="AxleLoadSum")))

# df = pl.DataFrame({
#     'english': ['this', 'is', 'not', 'pig', 'latin'],
# })
# result = df.with_columns(pig_latin = pig_latinnify('english'))
# print(result)

