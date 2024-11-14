def quick_sort(arr): #pivot
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[-1] #assigning the last element in the array as pivot
        left = []
        right=[]

        for num in arr[:-1]:
            if num<=pivot:
                left.append(num)
            else:
                right.append(num)
        return quick_sort(left) + [pivot] +quick_sort(right)
n=int(input("Enter array length:"))
arr=[]
for i in range (n):
    arr_elements = int(input(f"Enter the array element {i}:"))
    arr.append(arr_elements)
print("Orginal array",arr)
print("Quick Sort:",quick_sort(arr))
