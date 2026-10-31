names = ["A", "B", "C", "D", "E"]

# adjacency matrix (used for DFS)
matrix = [[0, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [0, 1, 1, 0, 1],
          [0, 0, 0, 1, 0]]

# adjacency list (used for BFS)
graph = {"A": ["B", "C"],
         "B": ["A", "D"],
         "C": ["A", "D"],
         "D": ["B", "C", "E"],
         "E": ["D"]}

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return visited

dfs_visited = []

def dfs(i):
    dfs_visited.append(names[i])
    for j in range(len(names)):
        if matrix[i][j] == 1 and names[j] not in dfs_visited:
            dfs(j)

dfs(0)
print("BFS:", *bfs("A"))
print("DFS:", *dfs_visited)

