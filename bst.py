
from collections import deque
from grap import Graph


# ==========================================
# NON-LINEAR DATA STRUCTURE
# LAST NAME: SELLOTE
# ==========================================


# ==========================================
# 1. BINARY TREE
# ==========================================

class TreeNode:

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):

        # Binary Tree using SELLOTE

        self.root = TreeNode("S")

        self.root.left = TreeNode("E1")
        self.root.right = TreeNode("L1")

        self.root.left.left = TreeNode("L2")
        self.root.left.right = TreeNode("O")

        self.root.right.left = TreeNode("T")
        self.root.right.right = TreeNode("E2")

    # Display Binary Tree
    def display(self, node, level=0, position="ROOT"):

        if node is not None:

            print("    " * level + position + ": " + node.name)

            self.display(node.left, level + 1, "LEFT")
            self.display(node.right, level + 1, "RIGHT")

    # Breadth-First Search (BFS)
    def bfs(self):

        if self.root is None:
            return []

        queue = deque([self.root])
        result = []

        while queue:

            current = queue.popleft()
            result.append(current.name)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return result

    # Depth-First Search (DFS - Preorder)
    def dfs(self):

        result = []

        def traverse(node):

            if node is not None:

                result.append(node.name)

                traverse(node.left)
                traverse(node.right)

        traverse(self.root)

        return result


# ==========================================
# 2. MAIN MENU
# ==========================================

def display_menu():

    print("\n")
    print("========================================")
    print("       NON-LINEAR DATA STRUCTURE")
    print("              SELLOTE")
    print("========================================")

    print("\nMAIN MENU")

    print("1. Display Binary Tree")
    print("2. Binary Tree BFS Traversal")
    print("3. Binary Tree DFS Traversal")
    print("4. Display Graph")
    print("5. Graph BFS Traversal")
    print("6. Graph DFS Traversal")
    print("7. Display All Traversals")
    print("8. Exit Program")

    print("========================================")


# ==========================================
# 3. MAIN PROGRAM
# ==========================================

def main():

    binary_tree = BinaryTree()
    graph = Graph()

    while True:

        display_menu()

        choice = input("Enter your choice (1-8): ")

        # OPTION 1: DISPLAY BINARY TREE
        if choice == "1":

            print("\nBINARY TREE - SELLOTE")

            binary_tree.display(binary_tree.root)

        # OPTION 2: BINARY TREE BFS
        elif choice == "2":

            print("\nBINARY TREE - BREADTH-FIRST SEARCH")

            print("BFS Traversal:")
            print(" -> ".join(binary_tree.bfs()))

        # OPTION 3: BINARY TREE DFS
        elif choice == "3":

            print("\nBINARY TREE - DEPTH-FIRST SEARCH")

            print("DFS Traversal (Preorder):")
            print(" -> ".join(binary_tree.dfs()))

        # OPTION 4: DISPLAY GRAPH
        elif choice == "4":

            print("\nGRAPH - SELLOTE")

            graph.display()

        # OPTION 5: GRAPH BFS
        elif choice == "5":

            print("\nGRAPH - BREADTH-FIRST SEARCH")

            print("BFS Traversal:")
            print(" -> ".join(graph.bfs("S")))

        # OPTION 6: GRAPH DFS
        elif choice == "6":

            print("\nGRAPH - DEPTH-FIRST SEARCH")

            print("DFS Traversal:")
            print(" -> ".join(graph.dfs("S")))

        # OPTION 7: DISPLAY ALL TRAVERSALS
        elif choice == "7":

            print("\n========================================")
            print("          ALL TRAVERSAL RESULTS")
            print("========================================")

            print("\nBINARY TREE")

            print("BFS:", " -> ".join(binary_tree.bfs()))
            print("DFS:", " -> ".join(binary_tree.dfs()))

            print("\nGRAPH")

            print("BFS:", " -> ".join(graph.bfs("S")))
            print("DFS:", " -> ".join(graph.dfs("S")))

            print("\n========================================")

        # OPTION 8: EXIT
        elif choice == "8":

            print("\nThank you for using the program!")
            print("Programmer: SELLOTE")
            print("Program exited successfully.")

            break

        # INVALID CHOICE
        else:

            print("\nInvalid choice! Please select from 1-8.")


# ==========================================
# RUN PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
