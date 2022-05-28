#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1.

N = int(input("Enter the number: "))
if N > 0:
    print(" {} is positive ".format(N))
elif N < 0:
    print("{} is Negative".format(N))
else :
    print("{} is Zero.".format(N))


# In[2]:


#Q2.
N1 = int(input("Enter the number: "))
if N1%2==0 :
    print("{} is Even".format(N1))
else:
    print("{} is odd".format(N1))


# In[3]:


#Q3.

Y = int(input("Enter the Year: "))
if Y%4==0 :
    print("{} is a leap year".format(Y))
else: 
    print("{} is not a leap year".format(Y))


# In[2]:


#Q4.

Num = int(input("Enter the Number: "))
if Num >1:
    for i in range(2,Num):
        if (Num%i)==0:
            print("{} Number is not a prime number".format(Num))
            break
    else:
        print("{} Number is a Prime Number".format(Num))
        
else:
    print("{} Number is not Prime Number".format(Num))


# In[14]:


#Q5.


        
    


# In[ ]:




