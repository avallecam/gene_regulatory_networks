# coding: utf-8

# comentarios acuérdense
print('HOla mundo')

# correr desde Ipython
# run (file).py

# start with networkX
import networkx as nx

G= nx.Graph()

# NODOS vertices (en lista)
G.nodes()
# ARISTAS conexiones (lista en tuplas)
G.edges()

# ORDEN numero de vertices
G.order()
# TAMAÑO numero de enlaces (aristas)
G.size()

# GRADO numero de aristas incidentes para cada vertice
G.degree()


G.add_nodes(5)
G.nodes()
G.add_nodes('victor')
# esta es una tupla
G.add_nodes((3,4))
# varios desde lista
G.add_nodes_from([2,'x','y',9])

# crear uniones
G.add_edges_from( [(2,'x'),('x','y'),('maribel','victor')] )
G.nodes()
G.edges()

G.remove_node('victor')

G.add_edge('natalia','VICTOR')

# NEW EXAMPLE with METADATA
K5 = nx.complete_graph(5)
K5.nodes()

# NEW EXAMPLE with METADATA
karateG = nx.karate_club_graph()
karateG.nodes()
# ALL NODES plus metadata
karateG.nodes(data=True)
# ORDEN numero de vertices
karateG.order()
# TAMAÑO numero de aristas enlaces
karateG.size()
# GRADO de elemento
karateG.degree(5)

# after networkX
import matplotlib.pyplot as plt

nx.draw(K5)
plt.show()

pos = nx.circular_layout(K5)
nx.draw(K5,pos)
plt.show()

plt.axis('equal')
nx.draw(K5,pos)
plt.show()

#CLEAN PLOTS
plt.clf()

karateG

nx.draw_spring(karateG, with_labels = True, node_size = 500, node_color = 'b', alpha= .5)
plt.show()

plt.savefig('redKarate.pdf')





