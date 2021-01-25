import pandas as pd
import os
from grafo import makeGraph

for data in os.listdir("data/all"):


    itemset = pd.read_csv("data/all/{}".format(data))

    nome = data.split(".csv")[0]


    path = "All"

    print(nome)

    if nome.split("_")[1] == "0.01":
        makeGraph(itemset= itemset, nome= nome, path= path, makeGif= False)
    else:
        makeGraph(itemset=itemset, nome=nome, path=path, makeGif=False, getSingles=True)
    print(" ")

    itemset.to_csv("apresentacao/{}/{}.csv".format(path,nome),index=False)
