import pandas as pd

# df = pd.DataFrame(data, index=index, columns=kolom

data = {
    "nama" : ["mark", "eduardo", "peter", "justin"],
    "usia" : [25, 30, 27, 35],
    "gaji" : ["25k", "16k", "11k", "35"]
}

dataframe = pd.DataFrame(data)
print(dataframe.describe)