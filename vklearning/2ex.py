from decimal import Decimal

n = int(input())
people = []

for _ in range(n):
    name, check, birth_date = input().split()
    people.append((name, check, birth_date))


def date_key(person):
    day, month, year = map(int, person[2].split('.'))
    return year, month, day


# Сортировка по имени
for person in sorted(people, key=lambda x: x[0]):
    print(*person)

print('#')

# Сортировка по среднему чеку как по числу
for person in sorted(people, key=lambda x: Decimal(x[1])):
    print(*person)

print('#')

# Сортировка по дате рождения
for person in sorted(people, key=date_key):
    print(*person)