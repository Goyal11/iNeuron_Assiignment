#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1.

Number1 = int(input("Enter the Number: "))
Number2 = int(input("Enter the Number: "))

MaxNum = max(Number1, Number2)

while(True):
       if (MaxNum%Number1==0) and (MaxNum%Number2==0):
            break
            MaxNum = MaxNum + 1
print("{} LCM of Number1 and Number2 ".format(MaxNum))    


# In[1]:


#Q2.
 
a = int(input("Enter the Number: "))
b = int(input("Enter the Number: "))

MinNum = min(a,b)

for i in range(1,MinNum+1):
    if a%i==0 and b%i==0:
        hcf =i
print("{} is hcf of a and b ".format(i))        


# In[1]:


#Q3.

N = int(input("Enter the Number: "))

print(bin(N))
print(oct(N))
print(hex(N))


# In[4]:


#Q4. 

String = input("Enter the Character: ")
print(ord(String))      
        
    

    


# In[5]:


#Q5.
a = float(input("Enter the Number1: ")) 
b = float(input("Enter the Number2: ")) 
Operation = input(" Enter the operation to be perform: ")

if Operation == "+":
    print(a+b)
elif Operation == "-":
    print(a-b)
elif Operation =="*":
    print(a*b)
elif Operation == "/":
    print(a/b)
else:
       print("Invalid Operation") 
    
    
    


# In[ ]:





# In[ ]:




