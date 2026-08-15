N, a, b, c = input().split()
N = int(N)
a,b,c = map(float, (a,b,c))

answer = []

for na in range(N + 1):
    for nb in range(N - na + 1):
        nc = N - na - nb

        if (100 * na >= a * N and 100 * nb >= b * N and 100 * nc >= c * N):
            answer.append((na,nb,nc))
if answer:
    for na, nb, nc in answer:
        print(na, nb, nc)
else:
    print('EMPTY')
