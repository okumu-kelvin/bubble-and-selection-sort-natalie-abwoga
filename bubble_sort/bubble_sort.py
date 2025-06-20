# TODO: Implement bubble sort
def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


# Example of bubble sort in use
print(bubble_sort([3, 2, 1]))  # Output: [1, 2, 3]
print(bubble_sort([4, 5, 3, 4]))  # Output: [3, 4, 4, 5]

