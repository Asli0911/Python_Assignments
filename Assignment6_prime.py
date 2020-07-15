def prime(n):
    lst=list(range(2, n+1))
    div=[]
    for i in lst:
        j=2
        while j**2<=i:         
            if i%j==0:           
                div.append(i)
            j=j+1
    set_div=set(div)
    return sorted(set(lst).difference(set_div))


print(prime(100))