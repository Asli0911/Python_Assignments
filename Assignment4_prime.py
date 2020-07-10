number=int(input("Please enter a number:"))

i=2
divide=[]

while i**2<=number:
    if number%i==0:
        divide.append(i)
    i+=1

if number==1:
    print(number, "is not a prime number.")
elif len(divide)>=1:
    print(number, "is not a prime number.")
else:
    print(number, "is a prime number.")