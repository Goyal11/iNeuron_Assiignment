#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1.

Num = int(input("Enter the number: "))
factorial = 1
if Num <0:
    print("NO factorial")
elif Num ==0:
    print("Factorial is 1")
elif Num ==1:
    print("Factorial is 1")
else:    
    for i in range(Num,1,-1):
        factorial =(factorial*i)
print(factorial)


# In[2]:


#Q2.
Number = int(input("Enter the Number: "))
if Number >1:
    for i in range(1,10):
        Count = Number*i
        print(Count)
        i = i+1


# In[3]:


#Q3.
def Fibbo(n):
    a = 1
    b = 1
    l = []
    for i in range(6):
        l.append(a)
        a=b
        b=a+b
    return l 


    
               
        
    
            
               
            
                
     


# In[4]:


Fibbo(6)


# In[5]:


#Q4.

Num = int(input("Enter the Number: "))
order = len(str(Num))
NUMBER = Num
Sum = 0
while (Num>0):
    digit = Num%10
    Sum += digit**order
    Num = Num//10
if (Sum==NUMBER):
    print("Armstrong Number")
else:
    print("Not a Armstrong")
    
    


# In[6]:


#Q6.

Number = int(input("Enter the Number: "))
Sum = (Number*(Number + 1))/2
Sum



# In[ ]:




