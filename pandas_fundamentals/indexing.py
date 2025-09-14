import pandas as pd

data: dict = {
    "nama": ["mark", "eduardo"],
    "usia": [27, 29]
}

data_frame = pd.DataFrame(data, index=["row 1", "row 2"])
print(data_frame)

# print(data_frame.index)