import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        rejected_edges = []

        self.graph = sorted(self.graph, key=lambda item: item[2])
        vertex_indices = {}
        vertices = set()
        for edge in self.graph:
            u, v, _ = edge
            vertices.add(u)
            vertices.add(v)
        parent = [-1] * len(vertices)
        rank = [0] * len(vertices)

        for edge in self.graph:
            u, v, _ = edge
            if u not in vertex_indices:
                vertex_indices[u] = len(vertex_indices)
            if v not in vertex_indices:
                vertex_indices[v] = len(vertex_indices)

        print("Sorted Edges:")
        for u, v, w in self.graph:
            print(f"{u} -- {v} == {w}")

        print("\nMinimum Spanning Tree (MST):")
        for edge in self.graph:
            u, v, w = edge
            x = self.find(parent, vertex_indices[u])
            y = self.find(parent, vertex_indices[v])

            if x != y:
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                print(f"Selected edge: {u} -- {v} == {w}")
                print("Current MST edges:")
                for u, v, weight in result:
                    print(f"{u} -- {v} == {weight}")
                print()
            else:
                rejected_edges.append([u, v, w])
                print(f"Rejected edge: {u} -- {v} == {w} (Forms cycle)")

        minimum_cost = sum(w for _, _, w in result)
        print(f"\nMinimum Cost Spanning Tree: {minimum_cost}")

        
        G = nx.Graph()
        for u, v, w in result:
            G.add_edge(u, v, weight=w)

        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, node_color='lightblue')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.title('Minimum Spanning Tree with Rejected Edges')
        plt.show()


g = Graph()

V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))

print("Enter the edges as 'u v weight':")
for _ in range(E):
    edge = input().split()
    u, v, w = edge[0], edge[1], int(edge[2])
    g.add_edge(u, v, w)

g.kruskal()
