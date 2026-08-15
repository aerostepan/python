from itertools import product

N, maxDig = map(int, input().split())

for placement in product(range(maxDig+1), repeat=N):
    print(*placement)

