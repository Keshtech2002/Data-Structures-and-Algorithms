#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[low];
    int start = low;
    int end = high;

    while (start < end) {
        while (start <= high && arr[start] <= pivot) {
            start++;
        }
        while (end > low && arr[end] > pivot) {
            end--;
        }
        if (start < end) {
            swap(&arr[start], &arr[end]);
        }
    }
    swap(&arr[low], &arr[end]);
    return end;
}

void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quick_sort(arr, low, pivot - 1);
        quick_sort(arr, pivot + 1, high);
    }
}

int main() {
    int arr[] = {45, 12, 89, 34, 77, 67, 23, 78, 90, 11, 56, 43, 19, 77, 32, 88, 25, 64, 39, 50, 15, 45};
    int n = sizeof(arr) / sizeof(arr[0]);

    quick_sort(arr, 0, n - 1);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}