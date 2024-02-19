def bubble_sort(arr):
    a = len(arr)
    for i in range(a):
        for j in range(0, a-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

mylist= [90,65,400,23,89,5,29,44,12,234,58,6]

bubble= mylist.copy()
insertion= mylist.copy()

# Sorting using Bubble Sort
bubble_sort(bubble)
print("Sorted list using Bubble Sort:", bubble)

# Sorting using Insertion Sort
insertion_sort(insertion)
print("Sorted list using Insertion Sort:", insertion)
