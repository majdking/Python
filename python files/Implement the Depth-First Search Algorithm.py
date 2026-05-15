adj_matrix_1 = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

adj_matrix_2 = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]


def display_adj_matrix(adj_matrix):
    for n in adj_matrix:
        print('\n')
        for e in n:
            print(e, end='\t')

# display_adj_matrix(adj_matrix_2)



def dfs(adj_matrix: list, node_label:int=0) -> list:
    if node_label < 0 or node_label >= len(adj_matrix):
        raise ValueError('Invalid node label')
    visited_nodes = [False] * len(adj_matrix)
    route = [node_label]
    # Recursion function 
    def search(adj_matrix, node_label, visited_nodes, route):
        visited_nodes[node_label] = True
        for i in range(len(adj_matrix[node_label])-1, -1, -1):
            if adj_matrix[node_label][i] == 1 and not visited_nodes[i]:
                route.append(i)
                search(adj_matrix, i, visited_nodes, route)

    search(adj_matrix, node_label, visited_nodes, route)
    return route

print(dfs(adj_matrix_1,2))
print(dfs(adj_matrix_1,0))
print(dfs(adj_matrix_2,0))
print(dfs(adj_matrix_2,3))