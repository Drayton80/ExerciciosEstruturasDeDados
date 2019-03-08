import matplotlib.pyplot as plt
import pandas as pd
import time
import original
import optimized

number_of_instances = []
original_times = []
optimized_times = []

actual_size = 5000

data_frame = pd.read_csv("ks-projects-201801.csv")

# Itera de 5000 até 100000 linhas para obter os tempos
# aumentando de 5000 em 5000 linhas a cada iteração:
for actual_size in range(500, 10000, 500):
	number_of_instances.append(actual_size)

	subset_data_frame = pd.DataFrame(data_frame.loc[0:actual_size])
	start = time.time()
	original.preprocess_data(subset_data_frame)
	end = time.time()
	duration = end - start
	original_times.append(duration)

	subset_data_frame = pd.DataFrame(data_frame.loc[0:actual_size])
	start = time.time()
	optimized.preprocess_data(subset_data_frame)
	end = time.time()
	duration = end - start
	optimized_times.append(duration)

plt.plot(number_of_instances, original_times , 'b',
         number_of_instances, optimized_times, 'g')
plt.show()


