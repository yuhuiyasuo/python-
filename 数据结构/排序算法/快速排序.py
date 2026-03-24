
def quick_sort(arr,start,end):
    if start >= end:
        return
    mid = arr[start]
    l,r = start,end
    while l < r:
        while l < r and arr[r] >= mid:
            r -= 1
        arr[l] = arr[r]
        while l < r and arr[l] < mid:
            l += 1
        arr[r] = arr[l]

    arr[l] = mid
    quick_sort(arr,start,l-1)
    quick_sort(arr,l+1,end)


if __name__ == "__main__":

    arr = [23,23,45,67,2,54645,645,4564,4]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

