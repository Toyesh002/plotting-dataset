import numpy as np
import csv
import pandas as pd
from matplotlib import pyplot as plt
import tensorflow as tf
from matplotlib import style

style.use('ggplot')

df= pd.read_csv(filepath_or_buffer="D:/TF/california_housing_train.csv")
df['median_house_value']/=1000.0
print(df.head())
print(df.describe())

plt.plot(df)

plt.title('info')
plt.ylabel('y axis')
plt.xlabel('x axis')

plt.show()

