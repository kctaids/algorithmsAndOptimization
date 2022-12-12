from math import inf

graph = [[0,   5,  inf, 10],
        [inf,  0,  3,  inf],
        [inf, inf, 0,   1],
        [inf, inf, inf, 0]]

for i in range(len(graph)):
    for j in range(len(graph)):
        for k in range(len(graph)):
            graph[i][k] = min(graph[i][k],graph[i][j]+graph[j][k])

print(graph)
