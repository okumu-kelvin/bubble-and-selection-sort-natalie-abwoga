# TODO: Implement bubble sort
def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

# Example of bubble sort in use
my_list = [5, 2, 9, 1, 5, 6]
bubble_sort(my_list)
print("Sorted list:", my_list)
