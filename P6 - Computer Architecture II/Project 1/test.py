import pandas as pd

data_frame = pd.read_csv("ks-projects-201801.csv")

size = 10

subset_data_frame = pd.DataFrame(data_frame.loc[0:size])

for instance in subset_data_frame.tolist():
	print(instance)
