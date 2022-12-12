from sys import maxsize
from itertools import permutations


def tsp(graph, s):
    V = len(graph)
    vertex = [i for i in range(V) if i != s]
    perms = permutations(vertex)

    min_weight = maxsize
    for i in perms:
        curr_weight = 0
        k = s
        for j in i:
            curr_weight += graph[k][j]
            k = j
        curr_weight += graph[k][s]

        min_weight = min(curr_weight, min_weight)

    return min_weight


if __name__ == "__main__":
	graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
	s = 0
	print(tsp(graph, s))
