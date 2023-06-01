import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_air = pd.read_csv("air_traffic_data.csv")

print(df_air.isna().sum())

print(df_air.info())