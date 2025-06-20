# TODO: Implement selection sort
def selection_sort(arr):
    # Make a copy so we don't modify the original list
    result = arr.copy()
    n = len(result)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]

    return result
