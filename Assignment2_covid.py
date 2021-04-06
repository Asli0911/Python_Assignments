age= input ("Are you a cigarette addict older than 75 years old?").lower() 
chronic= input ("Do you have a severe chronic disease?").lower() 
immune= input ("Is your immune system too weak?").lower() 
risk= age=="yes" or chronic=="yes" or immune=="yes"
print ("You are in risky group"*risk + "You are not in risky group"* (not risk))   
