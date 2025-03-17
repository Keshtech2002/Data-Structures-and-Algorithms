def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    start = low
    end = high

    while start < end:
        while start <= high and arr[start] <= pivot: #Added boundary check here
            start += 1
        while end > low and arr[end] > pivot: #Added boundary check here
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[low], arr[end] = arr[end], arr[low]
    return end

arr = [45, 12, 89, 34, 77, 67, 23, 78, 90, 11, 56, 43, 19, 77, 32, 88, 25, 64, 39, 50, 15, 45]
quick_sort(arr, 0, len(arr) - 1)
print(arr)