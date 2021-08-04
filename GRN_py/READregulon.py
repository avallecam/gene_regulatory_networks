import networkx as nx

#leyendo la info del grafo
regulon= 'regulonDB.txt'
f= open(regulon, 'r')
regLines= f.readlines()
f.close()

#construyendo el grafo
redE= nx.DiGraph()
#construir un loop
#lower() ALL minusculas
for linea in regLines:
    if linea[0] != '#':
        info= linea.lower().split()
        redE.add_edge(info[0],info[1])
