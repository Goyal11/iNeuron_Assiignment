#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1.

A = int(input("Enter the value in Kilometres: "))

C = 0.62137119*A

print("Value After Conversion:{}".format(C))


# In[2]:


#Q2.

Temp = int(input("Enter the value in degree Celsius: "))

F = 1.8*Temp + 32

print("Temperature after conversion in Fahrenheit: {}".format(F))


# In[3]:


#Q3.

import calendar as cd

Y = int(input("Enter the YEAR : "))
M = int(input("Enter the Month : "))
print(cd.month(Y,M))


# In[22]:


#Q4.

# Equation : a*x^2 + b*x + c = 0 
import cmath
A= int(input("Enter the value of a: "))
B= int(input("Enter the value of b: "))
C= int(input("Enter the value of c: "))
M = cmath.sqrt(B*B-4*A*C) 
X = -B + M/2*A
Y = -B - M/2*A
print(X)
print(Y)


# In[14]:


#Q5.

A = int(input("Enter the value: "))
B = int(input("Enter the value: "))
A = A + B
B = A - B
A = A - B 
 
print(A)
print(B)


# In[ ]:




