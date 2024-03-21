class DisjointSet:
    def _init_(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return  # Elements are already in the same set

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1


class Edge:
    def _init_(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


def kruskal(graph, num_vertices):
    # Sort edges by weight in ascending order
    sorted_edges = sorted(graph, key=lambda edge: edge.weight)

    # Create a disjoint-set to track the connected components
    disjoint_set = DisjointSet(num_vertices)

    mst = []  # Minimum spanning tree
    for edge in sorted_edges:
        src_root = disjoint_set.find(edge.src)
        dest_root = disjoint_set.find(edge.dest)

        # Add the edge to the MST if it does not create a cycle
        if src_root != dest_root:
            mst.append(edge)
            disjoint_set.union(src_root, dest_root)

    return mst


# Test the Kruskal's algorithm
num_vertices = 5
graph = [
    Edge(0, 1, 2),
    Edge(0, 3, 6),
    Edge(1, 2, 3),
    Edge(1, 3, 8),
    Edge(1, 4, 5),
    Edge(2, 4, 7),
    Edge(3, 4, 9)
]

minimum_spanning_tree = kruskal(graph, num_vertices)

print("Edges in the Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge.src, "-", edge.dest, "with weight", edge.weight)