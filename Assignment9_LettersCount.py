sentence=input("Please write a sentence:")
set1=set(sentence)
answer={}
for i in set1:
    answer[i]=sentence.count(i)
print(answer)    

