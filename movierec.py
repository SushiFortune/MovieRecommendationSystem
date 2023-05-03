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
df["actor_2_name"] = df["actor_2_name"].fillna("DOE")

# Find profit
df['profit'] = (df['gross'] - df['budget']) / (10 ** 8)

# sort by profit
df = df.sort_values(['profit', 'movie_title'], ascending=[False, True])

# get rid of duplicates
df.drop_duplicates(subset=None, keep='first', inplace=True)


# method to set the language to either English, French or Foreign
def language(lang):
    if lang == 'English':
        return 'English'
    elif lang == 'French':
        return 'French'
    else:
        return 'Foreign'


df['language'] = df['language'].apply(language)


# method for length of movies;long,medium,short
def length(len):
    if len >= 120:
        return 'That\'s a long one'
    elif len >= 90:
        return 'Grab a blanket'
    else:
        return 'It\'ll be over before you know it'


df['duration'] = df['duration'].apply(length)

# method for recommendation based on language
def rlang(lang):
    recommended_list = df[['language', 'movie_title', 'imdb_score']][df['language'] == lang]
    recommended_list = recommended_list.sort_values(by='imdb_score', ascending=False)
    return recommended_list.head(15)


print(rlang('Foreign'))
