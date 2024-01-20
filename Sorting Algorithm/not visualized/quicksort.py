
# Modification date: Wed Oct  4 14:14:11 2023

# Production date: Sun Sep  3 15:44:14 2023

# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
                print("partition", pivot)
                print(array)
                if array[j] <= pivot:
                        # if element smaller than pivot is found
                        # swap it with the greater element pointed by i
                        i = i + 1

                        # swapping element at i with element at j
                        (array[i], array[j]) = (array[j], array[i])

        # swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # return the position from where partition is done
        return i + 1

# function to perform quicksort
def quickSort(array, low, high):
        if low < high:
                # find pivot element such that
                # element smaller than pivot are on the left
                # element greater than pivot are on the right
                pi = partition(array, low, high)
                print("\n\nquicksort passed 1")
                print(array)

                # recursive call on the left of pivot
                quickSort(array, low, pi - 1)
                print("\n\nquicksort passed 2")
                print(array)

                # recursive call on the right of pivot
                quickSort(array, pi + 1, high)
                print("\n\nquicksort passed 3")
                print(array)


data = [8, 7, 3, 1, 0, 9, 2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)


input()