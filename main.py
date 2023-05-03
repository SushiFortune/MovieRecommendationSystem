import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

plt.rcParams["figure.figsize"] = (8, 8)
plt.style.use('fivethirtyeight')  # ??

df = pd.read_csv(r"C:\Users\15144\AppData\Local\Temp\Rar$DIa16648.37294\movie_metadata.csv")

# to find count of missing values per col
count = len(df.index) - df.count()

# take df with rows where gross & budget isn't null since they have the most amount of null values
df = df[df['gross'].notna()]
df = df[df['budget'].notna()]

# check which columns need null values replaced- actor_3_name & actor_2_name
count = len(df.index) - df.count()

df["actor_3_name"] = df["actor_3_name"].fillna("DOE")
df["actor_2_name"]=df["actor_2_name"].fillna("DOE")

