class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def adjMatrix(self, matrix):
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                print(matrix[i][k], " ", end='')
                print('')
        edge_u = []
        edge_v = []
        adjmatrix = [[0 for i in range(self.V)] for k in range(self.V)]

        for a in range(len(edge_u)):
            u = edge_u[a]
            v = edge_v[a]
            adjmatrix[u][v] = 1
        print("Adjacency matrix: ")
        return self.adjMatrix(adjmatrix)

    # A utility function to find set of an element i
    # (uses path compression technique)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct Kruskal algorithm
    def KruskalMST(self):
        result = []
        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]
        # Step 1:  Sort all the edges in non-decreasing order of their weight.
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            # If including this edge doesn't cause cycle,
            # include it in result and increment the index of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                # Else discard the edge
        print("Following are the edges in the constructed MST")

        for u, v, weight in result:
            # print str(u) + " -- " + str(v) + " == " + str(weight)
            print("%d -- %d == %d" % (u, v, weight))


if __name__ == '__main__':

    g = Graph(4)

    while True:
        action = input("GRAPH AND TREES\n"
                       "----------------\n"
                       " SELECT OPTION \n"
                       "[1]Add Elements\n"
                       "[2]Print Matrix\n"
                       "[3]Display Kruskal ST")
        if action not in "123" or len(action) != 1:
            print("Option not available")
            continue
        elif action == "1":
            g.addEdge(u=int(input("Enter u: ")), v=int(input("Enter v: ")), w=int(input("Enter w: ")))
        elif action == "2":
            from test2 import main
            print(main)
        elif action == "3":
            g.KruskalMST()
        else:
            continue
