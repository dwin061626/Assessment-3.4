
from collections import deque


# ==========================================
# GRAPH DATA STRUCTURE
# LAST NAME: SELLOTE
# ==========================================

class Graph:

    def __init__(self):

        # Graph connections using SELLOTE

        self.graph = {

            "S": ["E1", "L1"],

            "E1": ["S", "L2", "O"],

            "L1": ["S", "T"],

            "L2": ["E1", "O"],

            "O": ["E1", "L2", "T"],

            "T": ["O", "L1", "E2"],

            "E2": ["T"]

        }

    # ==========================================
    # DISPLAY GRAPH CONNECTIONS
    # ==========================================

    def display(self):

        print("\nGRAPH CONNECTIONS")

        for node, connections in self.graph.items():

            print(node, "->", ", ".join(connections))

    # ==========================================
    # BREADTH-FIRST SEARCH (BFS)
    # ==========================================

    def bfs(self, start):

        visited = set()
        queue = deque([start])
        result = []

        visited.add(start)

        while queue:

            current = queue.popleft()

            result.append(current)

            for neighbor in self.graph[current]:

                if neighbor not in visited:

                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    # ==========================================
    # DEPTH-FIRST SEARCH (DFS)
    # ==========================================

    def dfs(self, start):

        visited = set()
        result = []

        def traverse(node):

            visited.add(node)
            result.append(node)

            for neighbor in self.graph[node]:

                if neighbor not in visited:

                    traverse(neighbor)

        traverse(start)

        return result
