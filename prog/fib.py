#fibnocci series

def fibocciseries(n):
    if n<=1:
        return n
    else:
        return fibocciseries(n-1) + fibocciseries(n-2)
n=int(input("enter the number:"));
for i in range(n):
    print(fibocciseries(i),end=",")
