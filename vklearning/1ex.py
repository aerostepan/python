numbers = set(map(int, input().split()))
result = sorted(x**5 + 1 for x in numbers)
print(*result)