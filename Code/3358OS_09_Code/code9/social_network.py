import matplotlib.pyplot as plt
import networkx as nx


print [s for s in dir(nx) if s.endswith('graph')]
G = nx.davis_southern_women_graph()
plt.figure(1)
plt.hist(nx.degree(G).values())
plt.figure(2)
pos = nx.spring_layout(G)
nx.draw(G, node_size=9)
nx.draw_networkx_labels(G, pos)
plt.show()
