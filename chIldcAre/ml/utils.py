import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
from flask import url_for
from chIldcAre.ml.prediction import predict
import datetime

def do_plot():

    XX=pd.read_csv("dataset/data.csv")
    XX.dropna(inplace=True)
    coll=["ACTIVE_2018"]
    plt.figure(figsize=(5,5))
    sns.heatmap(XX.corr(),
            vmin=-1,
            cmap='coolwarm',
            )
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image




def create_instance(name):
    data=pd.read_csv(name,parse_dates=["created_at"],encoding="utf-8")
    return data
def tweets_table(name):
    data=create_instance(name)
    data2=predict(data["text"])
    data2=pd.DataFrame(data2)
    #for col in data2.columns:
     #   data2[col]=data2[col].apply(lambda x : float(str(x)[0:4]))
    return data.join(pd.DataFrame(data2))

def do_plot1(X=tweets_table("tweets.csv")):

    cols=[col for col in X.columns if col not in ["text"]]
    #X.drop(["text"],axis=1,inplace=True)
    X=X[cols]
    X["created_at"]=X["created_at"].apply(lambda x:x.strftime("%d/%m/%Y"))
    plt.figure(figsize=(10,3))
    
    sns.lineplot(data=X.set_index("created_at")).set(xlabel='Time axis', ylabel='Emotion value')
    plt.title('Evolution temporel des emotions')
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def do_plot2(X=tweets_table("tweets.csv")):

    cols=[col for col in X.columns if col not in ["text","created_at"]]
    #X.drop(["text"],axis=1,inplace=True)
    X=X[cols]
    #X["created_at"]=X["created_at"].apply(lambda x:x.strftime("%d/%m/%Y"))
    plt.figure(figsize=(10,3))
    plt.title('Distribution des postes dans la semaine derniere')
    #X.mean().plot.bar()
    for col in X.columns:
        sns.kdeplot(data=X[col], label=col, shade=True)
    

# Add title
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image



    plt.figure(figsize=(8,8))



