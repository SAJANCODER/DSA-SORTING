while True:
    n=int(input("enter the value:"))
    try:
        if(n<0):
            raise ValueError("Zero is not allowed")
        break
    except ValueError as e:
        print(e)
factorial =1
for i in range(1,n+1):
    factorial*=i
print(factorial)
        
