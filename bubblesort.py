def bubblesort(arr):
    size = len(arr)
    for k in range(size):
        for i in range(size-1-k):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print(arr)

if __name__ == '__main__':
    arr = [5, 9, 2, 1, 67, 34, 88, 34]
    bubblesort(arr)
    print(arr)