from math import floor


def heapsort(A: list) -> None:
    n = len(A)
    _build_max_heap(A)

    for i in range(1, n)[::-1]:
        A[i] = _delete_max(A, n)
        n -= 1


def _build_max_heap(A: list) -> None:
    n = len(A)
    for i in range(floor(n/2), -1, -1):
        _heapify_down(A, n, i)


def _delete_max(A: list, n: int) -> tuple:
    e = A[0]
    A[0] = A[n-1]
    _heapify_down(A, n-1, 0)
    return e


def _heapify_down(A: list, n: int, i: int):
    while 2*i+1 <= n-1:
        left = 2*i+1
        right = 2*i+2
        if right > n-1:
            m = left
        elif A[left] >= A[right]:
            m = left
        else:
            m = right

        if A[i] >= A[m]:
            return

        A[i], A[m] = A[m], A[i]
        i = m
