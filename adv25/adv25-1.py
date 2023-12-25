from aocd import get_data
import re
import networkx as nx

data = get_data(year=2023, day=25)

G = nx.Graph()

for line in data.split("\n"):
    vertex, connected_vertices = line.split(": ")
    connected_vertices = connected_vertices.split(" ")

    for other_vertex in connected_vertices:
        G.add_edge(vertex, other_vertex)
        G.add_edge(other_vertex, vertex)

G.remove_edges_from(nx.minimum_edge_cut(G))
components = list(nx.connected_components(G))
print(len(components[0]) * len(components[1]))

    