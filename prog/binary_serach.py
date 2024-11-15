pos = -1

def binary_search(arr, n):
    l = 0  # lower bound
    u = len(arr) - 1  # upper bound

    while l <= u:
        mid = (l + u) // 2
        if arr[mid] == n:
            globals()['pos'] = mid
            return True  # Element found, so return True

        elif arr[mid] > n:
            u = mid - 1  # Move the upper bound down

        else:
            l = mid + 1  # Move the lower bound up

    return False  # Element not found after loop

arr = [15, 56, 89, 23, 67]
n = 89

if binary_search(arr, n):
    print("found", pos+1)
else:
    print("not found")
