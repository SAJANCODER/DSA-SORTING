#insertation sort
def insertation_sort(array,n):
    for i in range(n):
        j=i
        while array[j-1]>array[j] and j>0:
            array[j-1] , array[j] = array[j],array[j-1]
            j-=1
    return array
n=int(input("Enter array lenght:"))
array=[]
for i in range(n):
    array_elements = int(input(f"Enter array element [{i}]:"))
    array.append(array_elements)
print("Orginal array:",array)
print("Array after insertation sort :", insertation_sort(array,n))
