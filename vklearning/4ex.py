def read_set():
    line = input()

    if line == 'EMPTY':
        return set()

    return set(map(int, line.split()))

def difference(a,b):
    result = set()
    for element in a:
        if element not in b:
            result.add(element)
    return result

a = read_set()
b = read_set()

result = difference(a,b)

if result:
    print(*sorted(result))
else:
    print('EMPTY')