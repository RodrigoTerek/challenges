from random import randrange


def quickSort(arr, init=0, last=None):
    last = last if last is not None else len(arr)

    if init < last:
        part = partition(arr, init, last)
        quickSort(arr, init, part)
        quickSort(arr, part + 1, last)

    return arr


def partition(arr, init, last):
    rand = randrange(init, last)
    arr[rand], arr[last - 1] = arr[last - 1], arr[rand]

    pivot = arr[last - 1]
    print(arr)
    print(pivot)
    for i in range(init, last):
        last -= 1
        if arr[i] <= pivot:
            init += 1
            arr[i], arr[init - 1] = arr[init - 1], arr[i]
    return init - 1


arr = [2, 5, -4, -6, 7, 3, 6, 9, 1, 0]
print(quickSort(arr))
