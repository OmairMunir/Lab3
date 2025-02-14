from collections import deque


class Graph:
    def __init__(self, adj_list):
        """Initializes the graph with an adjacency list."""
        self.adjacency_list = adj_list

    def get_neighbors(self, v):
        """Returns the neighbors of a given node."""
        return self.adjacency_list.get(v, [])

    def h(self, n):
        """Heuristic function: estimates the cost from node n to the goal."""

        H = {
            "The": 4,
            "cat": 3,
            "dog": 3,
            "runs": 2,
            "fast": 1
        }
        return H[n]

    def find_chota(self, g, don):
        chota = (99999, None)
        for a in don:
            if g[a] + self.h(a) < chota[0]:
                chota = (g[a] + self.h(a), a)

        return chota[1]

    def a_star_algorithm(self, start_node, stop_node):
        """Implements the A* search algorithm to find the optimal path."""

        open_list = {start_node}
        closed_list = set([])

        g = {start_node: 0}
        parents = {start_node: None}

        while open_list:
            n = self.find_chota(g, open_list)

            if n == stop_node:
                path = []
                costtttttttttt = g[n]
                while n is not None:
                    path.append(n)
                    n = parents[n]
                path.reverse()

                print("sentence:", path, "cost", costtttttttttt)
                return path, costtttttttttt

            open_list.remove(n)
            closed_list.add(n)

            for (m, cost) in self.get_neighbors(n):
                if m in closed_list:
                    continue

                new_g = g[n] + cost

                if m not in open_list or new_g < g[m]:
                    g[m] = new_g
                    parents[m] = n
                    open_list.add(m)

        print("Path does not exist!")
        return None


# Define the graph given in adjacency list
adjacency_list = {
    "The": [("cat", 2), ("dog", 3)],
    "cat": [("runs", 2)],
    "dog": [("runs", 2)],
    "runs": [("fast", 2)],
    "fast": []
}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('The', 'fast')
