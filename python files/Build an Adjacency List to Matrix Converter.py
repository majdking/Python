def adjacency_list_to_matrix(adj_list: dict) -> list:
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]
    # print(adj_matrix, n)
    # counter = 0
    for node in adj_list:
        # print('node_no',node)
        for edge in adj_list[node]:
            # print('edge to node', edge)
            #print(f'{node}{edge}',adj_matrix[node][edge])
            # print('node_no',node,'has edge to node', edge)
            adj_matrix[node][edge] = 1
            # print(adj_matrix[node])
            # counter += 1
    # print(counter)
    print(adj_matrix)
    return adj_matrix

adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

adjacency_list_to_matrix(adj_list)