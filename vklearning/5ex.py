def read_set():
    line = input()

    if line == 'EMPTY':
        return set()

    return set(map(int, line.split()))


def union(a, b):
    result = set()
    for element in a:
        result.add(element)
    for element in b:
        result.add(element)

    return result


a = read_set()
b = read_set()

result = union(a, b)

if result:
    print(*sorted(result))
else:
    print('EMPTY')
