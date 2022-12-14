import math


def insertion_sort(array, left, right):
    for i in range(left, right):
        temp = array[i]
        j = i - 1
        while j >= 1 and array[j] > temp:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    sort_arr = array
    return sort_arr


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, left, right):
    v = array[left]
    i = left
    j = right + 1
    while True:
        while True:
            j = j - 1
            if array[j] <= v:
                break
        while True:
            i = i + 1
            if array[i] >= v:
                break
        swap(array, i, j)
        if i >= j:
            break
    swap(array, i, j)
    swap(array, left, j)
    return j


def select_opt(array, k, left, right):
    w = 4
    while 1:
        d = right - left + 1
        if d <= w:
            insertion_sort(array, left, right)
            result = left + k - 1
            break
        dd = math.floor(d / w)  # количество подмассивов
        for i in range(1, dd):
            insertion_sort(array, left + (i - 1) * w, left + i * w - 1)
            swap(array, left + i - 1, left + (i - 1) * w + math.ceil(w / 2) - 1)
        v = select_opt(array, math.ceil(dd / 2), left, left + dd - 1)
        swap(array, left, v)
        v = partition(array, left, right)
        temp = v - left + 1
        if k < temp:
            right = v - 1
        elif k == temp:
            result = v
            break
        else:
            k = k - temp
            left = v + 1
    return result


arr = [20, 12, 18, 16, 24, 10, 22, 14]
n = len(arr) // 2
elem = select_opt(arr, n, 0, len(arr) - 1)
print(arr[elem])
