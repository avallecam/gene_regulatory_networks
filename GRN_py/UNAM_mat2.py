
# coding: utf-8

# In[3]:




## Redes en Biología

### UNAM: dia 1

# In[4]:

get_ipython().magic(u'pylab inline')


# In[5]:

import networkx as nx
import matplotlib.pyplot as plt


# In[6]:

# NEW EXAMPLE with METADATA
kG = nx.karate_club_graph()
kG.nodes()


# In[7]:

# ALL NODES plus metadata
kG.nodes(data=True)


# In[8]:

# EDGES o ARISTAS
kG.edges()


# In[9]:

# ORDEN numero de vertices
kG.order()


# In[10]:

# TAMAÑO numero de aristas enlaces
kG.size()


# In[11]:

# GRADO de elemento
kG.degree(32)


# In[12]:

#output DICCIONARIO con DEGREE para cada vertice
kG.degree(kG)


# In[13]:

nx.draw(kG)
#plt.show()


# In[14]:

pos= nx.circular_layout(kG)
nx.draw(kG, pos)
#plt.show()


# In[15]:

nx.draw_spring(kG, with_labels = True, node_size = 500, node_color = 'b', alpha= .5)
#plt.show()


### UNAM: Dia 2

# In[16]:

#COMPONENTES CONEXAS
nx.number_connected_components(kG)


# In[17]:

#DIAMETRO
nx.diameter(kG)


# In[18]:

#EXENTRICIDAD
nx.eccentricity(kG)


# In[19]:

#INICIO DISTRIBUCION DE GRADOS
#crear un DICCIONARIO con estructura { D.keys(): D.values() }
D= kG.degree(kG)
D


# In[20]:

#LISTA con [llaves] o ELEMENTOS VERTICES
#D.keys()


# In[21]:

#LISTA con valores de GRADO para cada ELEMENTO VERTICE
#D.values()


# In[22]:

#LISTA de TUPLAS usado luego para ordernar ELEMENTOS VERTICES de acuerdo a su GRADO
#D.items()


# In[23]:

#DISTRIBUCION DE GRADOS por histograma
plt.hist(D.values())


# In[24]:

#DISTRIBUCION DE GRADOS por histograma NORMALIZADO
plt.hist(D.values(), normed=True)


# In[25]:

#LISTA se define por corchetes
L= [3, 45, 35, 1000, 25, 76]
L


# In[26]:

sorted(L)


# In[27]:

sorted(L, reverse=True)


# In[28]:

P= ['anfibios', 'mamiferos', 'reptiles', 'aves', 'peces']
P


# In[29]:

sorted(P)


# In[30]:

sorted(P, key=len)


# In[31]:

#VISUALIZACION DE { eje X: elementos VERTICE x eje Y: GRADO de cada vertice }
plt.plot(sorted(D.values(), reverse=True))


# In[32]:

plt.plot(sorted(D.values(), reverse=True), 'o')


# In[33]:

#TUPLAS de VERTICES x ARISTAS , como D pero en TUPLAS
#D.items()


# In[34]:

#DEFINIR FUNCION para una t: tupla
def segundaComponente(t):
    return t[1]


# In[35]:

#EJEMPLO
segundaComponente((3,'hola'))


# In[36]:

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(D.items(), key=segundaComponente)[-5:]


# In[37]:

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(D.items(), key=segundaComponente)[:5]


# In[38]:

#ADD an ADJACENT MATRIX from NUMMPY
#nx.from_numpy_matrix


### READ .txt reguloDB

# In[39]:

ls


# In[40]:

#run READregulon.py

#EVITAR ESPACIOS EN BLANCO AL FINAL DEL TEXTO!!!

#leyendo la info del grafo
regulon= 'regulonDB.txt'
f= open(regulon, 'r')
regLines= f.readlines()
f.close()


# In[41]:

len(regLines)


# In[42]:

regLines[224]


# In[43]:

regLines[0]


# In[44]:

regLines[224][0] != '#'


# In[45]:

regLines[0][0] != '#'


# In[46]:

L= 'una Linea DE textO con MAYUSCULAS y minUSCULAS'
L.lower().split()


# In[47]:

#construyendo el grafo
redE = nx.DiGraph()

#construir un loop
for linea in regLines:
    if linea[0] != '#':
        info= linea.lower().split()
        redE.add_edge(info[0],info[1])


# In[48]:

info


# In[49]:

#regLines[2]


# In[50]:

redE


# In[51]:

redE.order() #VERTICES NODES ELEMENTOS


# In[52]:

redE.size() #ARISTAS EDGES CONEXIONES


# In[53]:

redE.edges()[:4]


# In[54]:

nx.draw(redE)


# In[55]:

#nx.draw_spring(redE, with_labels = True, node_size = 500, node_color = 'b', alpha= .8)


# In[56]:

#INICIO DISTRIBUCION DE GRAFOS
#crear un DICCIONARIO: { D.keys() x D.values() }
D= redE.degree(redE)
#D


# In[57]:

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(D.items(), key=segundaComponente)[-5:]


# In[58]:

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(D.items(), key=segundaComponente)[:5]


# In[59]:

#plt.hist?


# In[60]:

#DISTRIBUCION DE GRADOS por histograma
plt.hist(D.values())


# In[61]:

#DISTRIBUCION DE GRADOS por histograma NORMALIZADO
plt.hist(D.values(), normed=True)


# In[62]:

#DISTRIBUCION DE GRADOS
plt.plot(sorted(D.values(), reverse=True))


# In[80]:

D=nx.degree_centrality(redE)
plt.hist(D.values())


# In[64]:

D=nx.betweenness_centrality(redE)
plt.hist(D.values())


# In[65]:

nx.flow_hierarchy(redE)


### Generate a Random graph

# In[66]:

#GRAFO ALEATORIO
B= nx.barabasi_albert_graph(1850,1)
B


# In[67]:

#nx.barabasi_albert_graph?


# In[68]:

B.order()


# In[69]:

B.size()


# In[70]:

nx.draw(B)


# In[71]:

#INICIO DISTRIBUCION DE GRAFOS
#crear un DICCIONARIO: D.keys() x D.values()
D= B.degree(B)


# In[72]:

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(D.items(), key=segundaComponente)[-5:]


# In[73]:

#TUPLAS ordenadas por "POPULARIDAD" nodos o vertices X aristas o conexiones
sorted(D.items(), key=segundaComponente)[:5]


# In[74]:

#DISTRIBUCION DE GRADOS por histograma NORMALIZADO
plt.hist(D.values(), normed=True)


# In[75]:

#DISTRIBUCION DE GRADOS
plt.plot(sorted(D.values(), reverse=True))


# In[76]:

D=nx.degree_centrality(B)
plt.hist(D.values())


# In[77]:

D= nx.betweenness_centrality(B)
plt.hist(D.values())


# In[78]:

#nx.flow_hierarchy(B)


# In[79]:

B

