import pandas as pd
import time
import original
import optimized

data_frame = pd.read_csv("ks-projects-201801.csv")

size = 10000

subset_data_frame = pd.DataFrame(data_frame.loc[0:size])
start = time.time()
original.preprocess_data(subset_data_frame)
end = time.time()
print('Original Time =', end - start)

subset_data_frame = pd.DataFrame(data_frame.loc[0:size])
start = time.time()
optimized.preprocess_data(subset_data_frame)
end = time.time()
print('Optimized Time =', end - start)
