number= input("Please write a positive integer:")

if ("." in list(number) or "," in list(number)):
    print ("Please enter an integer number.")
    
elif ("-" in list(number)):
    print ("Please enter a positive number.")    

elif(number.isnumeric()==False):   
    print("Do not use any entries other than numeric values")
    
else:
    i=0
    sum_num=0
    while i<len(number):
        sum_num +=(int(number[i]))**(len (number))
        i+=1
    
    if sum_num==int(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")
       
