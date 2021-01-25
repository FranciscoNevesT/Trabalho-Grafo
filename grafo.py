import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval
import imageio



def makeImg(grafo,ims, path,nome,inter = "fig", pos = 0):

    fig = plt.figure(figsize=(40,40))

    fig.suptitle(nome , fontsize=100)

    if pos == 0:
        pos = nx.spring_layout(grafo)
    else:
        nodes = list(grafo.nodes())

        nodesMissing = []
        for key in pos.keys():
            if nodes.count(key) == 0:
                nodesMissing.append(key)

        for key in nodesMissing:
            del pos[key]


        pos = nx.spring_layout(grafo,pos = pos)

    nx.draw(grafo, pos = pos, with_labels=True, connectionstyle='arc3, rad = 0.5', node_size= 5000, font_size = 20 )

    plt.savefig("inter/{}.png".format(inter))

    plt.savefig("apresentacao/{}/{}.png".format(path,nome))

    plt.cla()

    plt.close(fig)

    im = imageio.imread("inter/{}.png".format(inter))

    ims.append(im)

    return ims,pos

def makeGraph(itemset, nome, path, inter = "fig", makeIm = True, makeGif = True, freq = 5, getSingles = False, pos = 0):
    itemset = itemset
    itemset["itemsets"] = itemset["itemsets"].apply(literal_eval)

    grafo = nx.Graph()

    ims = []

    c = 0
    for x in itemset["itemsets"]:

        atul = 0
        if len(x) == 1 and getSingles:
            nodes = list(grafo.nodes())

            if nodes.count(x) == 0:
                grafo.add_node(x[0])
                atul = 1


        else:
            for a in range(0,len(x)):
                for b in range(a+1, len(x)):
                    node1 = x[a]
                    node2 = x[b]

                    edges = list(grafo.edges)

                    if edges.count((node1,node2)) == 1 or edges.count((node2,node1)) == 1:
                        continue

                    nodes = list(grafo.nodes())

                    if nodes.count(node1) == 0:
                        grafo.add_node(node1)

                    if nodes.count(node2) == 0:
                        grafo.add_node(node2)

                    grafo.add_edge(node1,node2)

                    atul = 1

        if atul == 0:
            continue

        c += 1

        if makeIm and makeGif:

            if c == freq:
                ims,pos = makeImg(grafo, ims, path, nome,inter = inter, pos = pos)
                c = 0

    if makeIm:
        ims, pos = makeImg(grafo, ims, path, nome,inter = inter, pos = pos)

    if makeIm and makeGif:
        imageio.mimsave("apresentacao/{}/{}.gif".format(path,nome), ims)


    return grafo, ims, pos
