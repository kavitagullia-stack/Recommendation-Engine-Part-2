import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("movies.csv")
print(data.head())
print(data.info())
print(data.columns)
print("uploading ratings.csv")
data1=pd.read_csv("ratings.csv")
print(data1.head())
print(data1.info())
print(data1.columns)
data["year"]=data.title.str.extract(r'(\(\d\d\d\d\))',expand=True)
data["year"]=data.year.str.extract(r'(\d\d\d\d)',expand=True)
data["title"]=data.title.str.replace(r'(\(\d\d\d\d\))','',regex=True)
data["title"]=data["title"].apply(lambda x:x.strip())
print(data.head())
data["genres"]=data.genres.str.split("|")
movies=data.copy()
for i,row in data.iterrows():
    for g in row["genres"]:
        movies.at[i,g]=1
movies=movies.fillna(0)
print(data.head(5))
data1=data1.drop(["timestamp"],axis=1)
print(data1.head())
genres=movies.drop(["movieId","title","year","genres"],axis=1)
count=genres.sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
plt.bar(count.index,count.values,color="red")
plt.title("Moives per genres")
plt.xlabel("Genres")
plt.ylabel("No. of movies")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()
userinput=[
    {"title":"Dhurandar The revenge","rating":10.0},
    {"title":"Dhurandar","rating":9.0},
    {"title":"Demon slayer Infinity Castle","rating":10.0},
    {"title":"The Chainsaw man","rating":9.0},
    {"title":"Toy Story","rating":10.0},
    {"title":"Dracula: Dead and Loving It","rating":6.0},
    {"title":"Sense and Sensibility","rating":4.0},
    {"title":"Avengers: Infinity War - Part I","rating":10.0}
]
moviesinput=pd.DataFrame(userinput)
print(moviesinput)
inputId=data[data["title"].isin(moviesinput["title"].tolist())]
moviesinput=pd.merge(inputId,moviesinput)
moviesinput=moviesinput.drop(["genres","year"],axis=1)
print(moviesinput)
moviesuser=movies[movies["movieId"].isin(moviesinput["movieId"].tolist())]
moviesuser=moviesuser.reset_index(drop=True)
usergeneratedtable=moviesuser.drop(["movieId","title","genres","year"],axis=1)
userprofile=usergeneratedtable.transpose().dot(moviesinput["rating"])
print(userprofile)
plt.figure(figsize=(10,5))
plt.bar(userprofile.index,userprofile.values,color="red")
plt.title("Your taste profile")
plt.xlabel("genres")
plt.ylabel("weight")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()
