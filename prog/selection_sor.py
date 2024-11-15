#selection sorting

def selecting_sorting(array,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if(array[j]<array[min]):
                min=j
        array[i],array[min]=array[min],array[i]
    return array
n=int(input("enter array length:"))
array=[]
for i in range(n):
    array_elements = int(input(f"enter array elements [{i}]:"))
    array.append(array_elements)
print("ORGINAL ELEMENTS:",array)
print("AFTER SORTING:",selecting_sorting(array,n))
