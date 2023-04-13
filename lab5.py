import itertools
import numpy as np


def get_graph_order(adj_matrix):
    if len(adj_matrix) != len(adj_matrix[0]):
        return -1
    else:
        return len(adj_matrix)


def get_degree_sequence(adj_matrix):
    degree_sequence = []
    for vertex in range(len(adj_matrix)):
        degree_sequence.append(sum(adj_matrix[vertex]))
    degree_sequence.sort(reverse=True)
    return degree_sequence


def get_all_vertex_permutations(adj_matrix):
    if get_graph_order(adj_matrix) > 8:
        print("This function is too inefficient for graph order > 8")
        return -1
    all_adj_matrix = []
    idx = list(range(len(adj_matrix)))
    possible_idx_combinations = [
        list(i) for i in itertools.permutations(idx, len(idx))
    ]
    for idx_comb in possible_idx_combinations:
        a = adj_matrix
        a = a[idx_comb]
        a = np.transpose(np.transpose(a)[idx_comb])
        all_adj_matrix.append({
            "perm_vertex":
                idx_comb,
            "adj_matrix":
                a
        })

    return all_adj_matrix


def brute_force_test_graph_isomporphism(adj_1, adj_2):
    degree_sequence_1 = get_degree_sequence(adj_1)
    degree_sequence_2 = get_degree_sequence(adj_2)
    if get_graph_order(adj_1) != get_graph_order(adj_1):
        return False
    elif np.array_equal(degree_sequence_1, degree_sequence_2) == False:
        return False
    else:
        for adj_matrix in list(
                map(lambda matrix: matrix["adj_matrix"],
                    get_all_vertex_permutations(adj_2))):
            if np.array_equal(adj_1, adj_matrix) == True:
                return True
    return False


with open('data51.txt', 'r') as f:
    lines = f.readlines()

# Create the adjacency matrix from the data
graph1 = []
for line in lines:
    row = [int(x) for x in line.split()]
    graph1.append(row)
n = len(graph1)

print("My data1:")
print(graph1)

with open('data52.txt', 'r') as f:
    lines = f.readlines()

# Create the adjacency matrix from the data
graph2 = []
for line in lines:
    row = [int(x) for x in line.split()]
    graph2.append(row)
n = len(graph2)

print("My data2:")
print(graph2)

adj_matrix_1 = np.array(graph1)
adj_matrix_2 = np.array(graph2)
print()
print(brute_force_test_graph_isomporphism(adj_matrix_1, adj_matrix_2))
