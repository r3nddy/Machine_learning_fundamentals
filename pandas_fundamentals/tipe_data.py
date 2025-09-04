import pandas as pd


temperatur: list[int] = [23, 54, 21, 43, 10]
hari: list[str] = ["senin", "selasa", "rabu", "kamis", "jumat"]

data_series = pd.Series(temperatur, index=hari, name="laporan suhu harian (celcius)")

# print(f"value : {data_series.values}")
# print(f"indexing: {data_series.index}")
print(data_series)