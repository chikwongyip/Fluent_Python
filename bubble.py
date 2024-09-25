# coding:utf-8
# 冒泡排序

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr


arr = [5, 3, 8, 6, 2, 7, 1, 4]
print(arr)
print(bubble_sort(arr))
