num=int(input("Please enter a number:"))

fib=[]
i=0
j=1
while i<=num:
    fib.append(i)
    i, j=j, i+j

print(fib)

