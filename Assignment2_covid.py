age= input ("Are you a cigarette addict older than 75 years old?").lower() 
chronic= input ("Do you have a severe chronic disease?").lower() 
immune= input ("Is your immune system too weak?").lower() 

if age=="yes":
    age= True
else:
    age= False

if chronic=="yes":
    chronic =True
else:
    chronic=False

if immune=="yes":
    immune=True
else:
    immune=False

risk= age or chronic or immune

print ("You are in risky group"*risk + "You are not in risky group"* (not risk))   
