def first_non_consecutive(arr):
    for i in range(len(arr)):
        if arr[i] - arr[i - 1] > 1:
            return arr[i]
    return None


print(first_non_consecutive([0,1,2,4,5,6,7]))