def hamiltonian_circuit(graph):

    n = len(graph)
    path = [-1] * n

    def is_valid(vertex, position):
       
        if graph[path[position-1]][vertex] == 0:
            return False

        for i in range(position):
            if path[i] == vertex:
                return False

        return True

    def find_path(position):
       
        if position == n:
            if graph[path[position-1]][path[0]] == 1:
                return True
            else:
                return False

        for vertex in range(1, n):
            if is_valid(vertex, position):
                path[position] = vertex

                if find_path(position + 1):
                    return True

                path[position] = -1

        return False

    
    path[0] = 0

    if find_path(1):
        return path
    else:
        return None

graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

hamiltonian_path = hamiltonian_circuit(graph)

if hamiltonian_path is not None:
    print("Hamiltonian Circuit found: ", end="")
    for vertex in hamiltonian_path:
        print(vertex, end=" ")
else:
    print("No Hamiltonian Circuit found.")

