import pandas

data = pandas.read_json('os_data.json')
data.dropna(inplace=True)
data = data[0: 100]
print(data.os.value_counts())
