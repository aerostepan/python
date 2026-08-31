

def is_cyclic(g, v):
    state = [0] * v
    for start in range(v):
        if state[start] != 0:
            continue
        state[start] = 1
        stack = [(start, 0)]
        while stack:
            vertex, next_index = stack[-1]
            neighbors = g.get(vertex, [])

            if next_index == len(neighbors):
                state[vertex] = 2
                stack.pop()
                continue

            neighbour = neighbors[next_index]
            stack[-1] = (vertex, next_index + 1)

            if state[neighbour] == 1:
                return True
            if state[neighbour] == 0:
                state[neighbour] = 1
                stack.append((neighbour, 0))

    return False

# Код, который запускает тест
n = int(input())  # количество строк, с ребрами графа
v = int(input())  # количество вершин в графе

adj =  {i:[] for i in range(v)}

for _ in range(v):
    u1, u2 = list(map(int, input().split(' ')))
    if u2 != -1:
        adj[u1].append(u2)

res = str(is_cyclic(adj, v))
print(res)
