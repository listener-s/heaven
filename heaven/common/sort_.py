def small_big_insert_sort(arr) -> list:
    """
    插入排序: 由小到大排序
    :param arr:
    :return: []
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def big_small_insert_sort(arr) -> list:
    """
    插入排序: 由大到小排序
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def select_sort(arr) -> list:
    """
    选择排序
    :param arr:
    :return:
    """
    length = len(arr)
    if length <= 1:
        return arr
    for j in range(length):
        min_num_index = j
        for i in range(j + 1, length):
            if arr[i] < arr[min_num_index]:
                min_num_index = i
        arr[min_num_index], arr[j] = arr[j], arr[min_num_index]
    return arr
