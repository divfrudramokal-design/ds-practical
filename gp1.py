count = int(input("Enter number of nodes: "))
nodes = []
for i in range(count):
    node = input("Enter node name: ")
    nodes.append(node)

size = len(nodes)
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    matrix.append(row)

edge_count = int(input("Enter number of edges: "))
for k in range(edge_count):
    u = input("Enter first node: ")
    v = input("Enter second node: ")
    if u in nodes and v in nodes:
        i = nodes.index(u)
        j = nodes.index(v)
        matrix[i][j] = 1
        matrix[j][i] = 1
    else:
        print("Invalid node name, edge skipped.")


print("\n=== Adjacency Matrix ===")
print(" ", end="")
for node in nodes:
    print(node, end=" ")
print()  

for i in range(size):
    print(nodes[i], end=" ")
    for j in range(size):
        print(matrix[i][j], end=" ")
    print()  

def find_path(start, end, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    if start == end:
        return visited

    i = nodes.index(start)
    for j in range(size):
        if matrix[i][j] == 1 and nodes[j] not in visited:
            result = find_path(nodes[j], end, visited.copy())
            if result:
                return result
    return None

# Asking for the start and end nodes
print("\n=== Path Finding ===")
src = input("Enter start node: ")
dst = input("Enter end node: ")
path = find_path(src, dst)

if path:
    print("Path found: ")
    for node in path:
        print(node, end=" ")
    print()  # Newline after the path
else:
    print("No path exists between", src, "and", dst)

