from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        self.dfs_util(start, visited)
        print()

    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()

def main():
    g = Graph()

    while True:
        print("\n1. Add Edge")
        print("2. Depth First Search (DFS)")
        print("3. Breadth First Search (BFS)")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            u = int(input("Enter source vertex: "))
            v = int(input("Enter destination vertex: "))
            g.add_edge(u, v)
        elif choice == '2':
            start = int(input("Enter starting vertex for DFS: "))
            print("DFS traversal:")
            g.dfs(start)
        elif choice == '3':
            start = int(input("Enter starting vertex for BFS: "))
            print("BFS traversal:")
            g.bfs(start)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
