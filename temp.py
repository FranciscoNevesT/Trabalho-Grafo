import pandas as pd
import os
from grafo import makeGraph
import imageio

ims = []
im = 0
graph = 0
pos = 0

path = "Temporal"
for data in os.listdir("data/temporal"):

    itemset = pd.read_csv("data/temporal/{}".format(data))

    nome = data.split(".csv")[0]


    print(nome)

    graph, im, pos = makeGraph(itemset= itemset, nome= nome, path= path, makeGif=False, inter= "fig2", pos = pos)

    print(" ")

    ims.append(im[0])

    itemset.to_csv("apresentacao/{}/{}.csv".format(path,nome),index=False)

imageio.mimsave("apresentacao/{}/{}.gif".format(path, "dataT"), ims)


