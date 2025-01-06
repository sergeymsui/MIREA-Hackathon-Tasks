# Метрополитен состоит из нескольких линий метро. Все станции метро в городе
# пронумерованы натуральными числами от 1 до N. На каждой линии расположено
# несколько станций. Если одна и та же станция расположена сразу на нескольких
# линиях, то она является станцией пересадки и на этой станции можно пересесть
# с любой линии, которая через нее проходит, на любую другую (опять же проходящую через нее).

# Напишите программу, которая по данному вам описанию метрополитена определит,
# с каким минимальным числом пересадок можно добраться со станции A на станцию B.
# Если данный метрополитен не соединяет все линии в одну систему, то может так
# получиться, что со станции A на станцию B добраться невозможно, в этом случае
# ваша программа должна это определить.

# Формат ввода
# Сначала вводится число N — количество станций метро в городе (2 ≤ N ≤ 100).
# Далее следует число M — количество линий метро (1 ≤ M ≤ 20). Далее идет описание
# M линий. Описание каждой линии состоит из числа Pi — количество станций на этой
# линии (2 ≤ Pi ≤ 50) и Pi чисел, задающих номера станций, через которые проходит
# линия (ни через какую станцию линия не проходит дважды).

# Затем вводятся два различных числа: A — номер начальной станции, и B — номер станции,
# на которую нам нужно попасть. При этом если через станцию A проходит несколько линий,
# то мы можем спуститься на любую из них. Так же если через станцию B проходит несколько
#  линий, то нам не важно, по какой линии мы приедем.

from collections import deque, defaultdict


def min_transfers():
    # Чтение количества станций и линий
    N = int(input())
    M = int(input())

    # Список линий, каждая линия содержит список станций
    lines = []
    for _ in range(M):
        parts = list(map(int, input().split()))
        stations = parts[1:]
        lines.append(stations)

    # Чтение начальной и конечной станции
    A, B = map(int, input().split())

    # Сопоставление станции с линиями, которые через неё проходят
    station_to_lines = defaultdict(set)
    for idx, line in enumerate(lines):
        for station in line:
            station_to_lines[station].add(idx)

    # Если A или B отсутствуют в метро
    if A not in station_to_lines or B not in station_to_lines:
        print(-1)
        return

    # Если A и B находятся на одной линии
    common_lines = station_to_lines[A].intersection(station_to_lines[B])
    if common_lines:
        print(0)
        return

    # Построение графа линий
    adjacency = defaultdict(set)
    for station, ls in station_to_lines.items():
        ls = list(ls)
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                adjacency[ls[i]].add(ls[j])
                adjacency[ls[j]].add(ls[i])

    # Линии, на которых находятся станции A и B
    start_lines = station_to_lines[A]
    end_lines = station_to_lines[B]

    # BFS для поиска минимальных пересадок
    visited = [False] * M
    queue = deque()

    # Инициализация очереди стартовыми линиями с 0 пересадками
    for line in start_lines:
        queue.append((line, 0))
        visited[line] = True

    while queue:
        current_line, transfers = queue.popleft()

        # Если текущая линия является одной из конечных, возвращаем количество пересадок
        if current_line in end_lines:
            print(transfers)
            return

        # Проходим по смежным линиям
        for neighbor in adjacency[current_line]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, transfers + 1))

    # Если путь не найден
    print(-1)


# Вызов функции
min_transfers()
