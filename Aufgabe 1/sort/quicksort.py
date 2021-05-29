from random import randint


def randomized_quicksort(A: list, p: int, r: int) -> None:
    if p < r:
        q = _randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)


def _randomized_partition(A: list, p: int, r: int) -> int:
    m = randint(p, r)
    A[m], A[r] = A[r], A[m]
    x = A[r]
    i = p-1
    # Rearange list
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A: list, p: int, r: int) -> None:
    if p < r:
        q = _partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def _partition(A: list, p: int, r: int) -> int:
    x = A[r]
    i = p-1
    # Rearange list
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
