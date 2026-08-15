 from itertools import product

N, M = map(int, input().split())
halves_by_sum = {}

for half in product(range(M+1), repeat=N):
    current_sum = sum(half)
    if current_sum not in halves_by_sum:
        halves_by_sum[current_sum] = []
    halves_by_sum[current_sum].append(half)

for current_sum in sorted(halves_by_sum):
    halves = halves_by_sum[current_sum]

    for left_half in halves:
        for right_half in halves:
            print(*left_half, *right_half)
