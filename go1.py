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
print(" ", " ".join(nodes))
for i in range(size):
    print(nodes[i], " ".join(str(x) for x in matrix[i]))

