#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Q1.
l = [1,3,44,76,88]
sum(l)


# In[23]:


#Q2.

l = [1,2,3,"Mayank",34,"Hello",23]
N=1

for i in l:
       if type(i)==int:
        N = N*i
print(N)


# In[25]:


#Q3.

l = [1,2,3,0]
min(l)


# In[26]:


#Q4.
l = [1,2,3,0]
max(l)


# In[4]:


#Q5.
l = [1,2,3,0]
l.remove(max(l))
max(l)


# In[35]:


#Q6.


# In[5]:


#Q7.
l = [1,3,44,76,88]

for i in l:
       if i%2==0:
            print(i,"is Even")


# In[6]:


#Q8.
l = [1,3,44,76,88]

for i in l:
    if i%2!=0:
        print(i, "is Odd")


# In[17]:


#9.
L =[1,2,3,6,7,88,[],"Ineuron",24,"Mayank"] 
for i in L:
    if type(i)==list:
        if len(i)==0:
            L.remove(i)
        
L


# In[21]:


#10. 
l =[1,2,3,4,"Mayank"]
l1 = l.copy()
l1


# In[20]:


#11.

l = [1,1,2,2,2,4,3,3,5,5,5,5,6,7,7]
set(l)
for i in set(l):
    print(i,l.count(i))


# In[ ]:




