



# 1. Вычисление факториала числа n:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# 2. Вывод чисел Фибоначчи:


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 3. Поиск в глубину (DFS) для обхода графа:


def dfs(graph, node, visited):
    visited[node] = True
    print(node)
    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited)


# 4. Рекурсивная сортировка выбором (Selection Sort):


def selection_sort(arr):
    n = len(arr)
    # Проходим по массиву с конца до начала
    for i in range(n-1, 0, -1):
        # Находим минимальный элемент в неотсортированной части массива
        min_idx = i
        for j in range(i):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем местами найденный минимальный элемент с первым элементом неотсортированной части
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 5. Рекурсивное слияние двух отсортированных списков:


def merge(left, right):
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    else:
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:], right)
        else:
            return [right[0]] + merge(left, right[1:])

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    else:
        return arr


