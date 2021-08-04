



get_ipython().magic(u'pylab inline')

import networkx as nx
import matplotlib.pyplot as plt

#ADD an ADJACENT MATRIX from NUMMPY
#nx.from_numpy_matrix

ls

#run READregulon.py

#EVITAR ESPACIOS EN BLANCO AL FINAL DEL TEXTO!!!

#leyendo la info del grafo
regulon= 'regulonDB.txt'
f= open(regulon, 'r')
regLines= f.readlines()
f.close()

len(regLines)

regLines[224]

regLines[0]

regLines[224][0] != '#'

regLines[0][0] != '#'

L= 'una Linea DE textO con MAYUSCULAS y minUSCULAS'
L.lower().split()

#construyendo el grafo
redE = nx.DiGraph()

#construir un loop
for linea in regLines:
    if linea[0] != '#':
        info= linea.lower().split()
        redE.add_edge(info[0],info[1])

info

#regLines[2]

redE

redE.order() #VERTICES NODES ELEMENTOS

redE.size() #ARISTAS EDGES CONEXIONES

redE.edges()[:4]

nx.draw(redE, node_size=50)

#pos= nx.circular_layout(redE)
#nx.draw(redE, node_size=50, pos)

#nx.draw_spring(redE, with_labels = True, node_size = 500, node_color = 'b', alpha= .8)

#COMPONENTES CONEXAS ---> NOT FOR DIRECTED GRAPH
#nx.number_connected_components(redE)

#EXENTRICIDAD -----> NOT CONNECTED
#nx.eccentricity(redE)

#DIAMETRO   -------> NOT CONNECTED
#nx.diameter(redE)

E= nx.Graph(redE)
E

#COMPONENTES CONEXAS ---> NOT FOR DIRECTED GRAPH
nx.number_connected_components(E)

E_components = nx.connected_component_subgraphs(E)
E_components

for g in E_components:
    print(g.order())

#nx.draw_spring(E, node_size=100)

E_grados = nx.degree(E)
type(E_grados)

#primero extraigo los valores del diccionario,
#luego los reduzco a un conjunto con los elementos únicos -sin repeticiones- y
#finalmente los ordeno de menor a mayor
Eg = sorted(set(E_grados.values()))
len(Eg)

Eg

E_freq= [E_grados.values().count(g) for g in Eg]
#plt.loglog(Eg, E_freq)
#plt.xlabel('grados')
#plt.ylabel('frequencia x grado')

#INICIO DISTRIBUCION DE GRADOS
#crear un DICCIONARIO: { D.keys() x D.values() }
DEc= redE.degree(redE)
#D

#DEFINIR FUNCION para una t: tupla
def segundaComponente(t):
    return t[1]

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(DEc.items(), key=segundaComponente)[-5:]

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(DEc.items(), key=segundaComponente)[:5]

#plt.hist?

#DISTRIBUCION DE GRADOS por histograma
plt.hist(DEc.values())

#DISTRIBUCION DE GRADOS por histograma NORMALIZADO
#plt.hist(DEc.values(), normed=True)

#DISTRIBUCION DE GRADOS
#plt.plot(sorted(D.values(), reverse=True))
#plt.plot(DEc.values())
#plt.xlabel('vertice')
#plt.ylabel('grado')

DCEc=nx.degree_centrality(redE)
#plt.hist(DCEc.values())

DBEc=nx.betweenness_centrality(redE)
#plt.hist(DBEc.values())

nx.flow_hierarchy(redE)

#GRAFO ALEATORIO
B= nx.barabasi_albert_graph(redE.order(),min(DEc.values())) #VALUES extracted from Ecoli GRN: #VERTICES and min(#ARISTAS)=1
B

#nx.barabasi_albert_graph?

#NÚMERO DE VERTICES
B.order()

#NÚMERO DE ARISTAS
B.size()

#nx.draw(B, node_size=50)

#COMPONENTES CONEXAS ---> NOT FOR DIRECTED GRAPH
nx.number_connected_components(B)

#nx.draw_spring(B, node_size=50)

#DIAMETRO
nx.diameter(B)

#DISTRIBUCION DE GRADOS por PLOTEO
B_grados = nx.degree(B)
Bg = sorted(set(B_grados.values()))
B_freq= [B_grados.values().count(g) for g in Bg]
#plt.loglog(Bg, B_freq)
#plt.xlabel('grados')
#plt.ylabel('frequencia x grado')

#EXENTRICIDAD ----> ENTENDER / RESULTADO PROLONGADO
#nx.eccentricity(B)

#INICIO DISTRIBUCION DE GRAFOS
#crear un DICCIONARIO: D.keys() x D.values()
DB= B.degree(B)

#DEFINIR FUNCION para una t: tupla
def segundaComponente(t):
    return t[1]

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(D.items(), key=segundaComponente)[-5:]

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(D.items(), key=segundaComponente)[:5]

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(DB.items(), key=segundaComponente)[-5:]

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(DB.items(), key=segundaComponente)[:5]

#DISTRIBUCION DE GRADOS por histograma
#plt.hist(DB.values())
#plt.xlabel('grados')
#plt.ylabel('frequencia x grado')

#DISTRIBUCION DE GRADOS
#plt.plot(sorted(D.values(), reverse=True))
#plt.plot(DB.values())
#plt.xlabel('vertice')
#plt.ylabel('grado')

DCB=nx.degree_centrality(B)
#plt.hist(DCB.values())

DBB= nx.betweenness_centrality(B)
#plt.hist(DBB.values())

#nx.flow_hierarchy(B)

#?nx.draw_networkx

B_degree = nx.degree(B)
np.mean(B_degree.values())

redE_degree = nx.degree(redE)
np.mean(redE_degree.values())

plt.subplot(1,2,1)
nx.draw(B, node_size=50)
plt.title('Barabasi random')
plt.subplot(1,2,2)
nx.draw(redE, node_size=50)
plt.title('Ecoli real GRN')
plt.show()

plt.subplot(1,2,1)
nx.draw_spring(B, node_size=50)
plt.title('Barabasi random')
plt.subplot(1,2,2)
nx.draw_spring(E, node_size=50)
plt.title('Ecoli real GRN')
plt.show()

plt.subplot(1,2,1)
plt.plot(DB.values())
plt.title('Barabasi random')
plt.xlabel('vertice')
plt.ylabel('grado')
plt.subplot(1,2,2)
plt.plot(DEc.values())
plt.title('Ecoli real GRN')
plt.xlabel('vertice')
plt.ylabel('grado')
plt.show()

#plt.subplot(1,2,1)
plt.plot(DEc.values())
plt.xlabel('vertice')
plt.ylabel('grado')
#plt.subplot(1,2,2)
plt.plot(DB.values())
#plt.xlabel('vertice')
#plt.ylabel('grado')
#plt.show()

plt.subplot(1,2,1)
plt.loglog(Bg, B_freq)
plt.title('Barabasi random')
plt.xlabel('grados')
plt.ylabel('frequencia x grado')
plt.subplot(1,2,2)
plt.loglog(Eg, E_freq)
plt.title('Ecoli real GRN')
plt.xlabel('grados')
plt.ylabel('frequencia x grado')
plt.show()

#plt.subplot(1,2,1)
plt.loglog(Eg, E_freq)
plt.title('Barabasi random (verde) y Ecoli real GRN (azul)')
plt.xlabel('grados')
plt.ylabel('frequencia x grado')
#plt.subplot(1,2,2)
plt.loglog(Bg, B_freq)
#plt.xlabel('grados')
#plt.ylabel('frequencia x grado')
plt.show()

line1, = plt.plot([1,2,3], label="Line 1", linestyle='--')
line2, = plt.plot([3,2,1], label="Line 2", linewidth=4
first_legend = plt.legend(handles=[line1], loc=1
ax = plt.gca().add_artist(first_legend
plt.legend(handles=[line2], loc=4)

plt.show()



