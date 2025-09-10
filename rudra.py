def create_matrix(nodes):
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]
    return matrix

def display_matrix(nodes, matrix):
    print("   ", " ".join(nodes))
    for i in range(len(nodes)):
        print(nodes[i], matrix[i])

if __name__ == "__main__":
    n = int(input("Enter number of nodes: "))
    nodes = []
    for _ in range(n):
        node = input("Enter node name: ")
        nodes.append(node)

    matrix = create_matrix(nodes)

    print("\n=== Adjacency Matrix ===")
    display_matrix(nodes, matrix)
