#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Q1.

d = {"key1":'Value1',"key2":'Value2', "key3":'Manu', "key4":"Goyal","key5":'Manu',"key6": 2, "key7": "2","key8": "Hello"}
for i in set(d.values()):
     print(i)


# In[8]:


#Q2.
sum1 = 0
d = {"key1":2,"key2":'Value2', 2:'Manu', "key4":"Goyal","key5":'Manu',"key6": 2, "key7": 2,"key8": "Hello",
     "key9": 4, "key10":"ineuron"}
for k,v in d.items():
    if type(k)==int :
        sum1 = sum1 + k
        
    if type(v)==int:
        sum1 = sum1 + v
sum1        


# In[1]:


#Q3.
d = {"key1":2,"key2":'Value2', 2:'Manu', "key4":"Goyal","key5":'Manu',"key6": 2, "key7": 2,"key8": "Hello",
     "key9": 4, "key10":"ineuron"}
d1 = {"key1":'Value1',"key2":'Value2', "key3":'Manu', "key4":"Goyal","key5":'Manu',"key6": 2, "key7": "2","key8": "Hello"}
# output

for k,v in  d.items():
    if k not in d1.keys():
        d1[k]=v
d1    


# In[12]:


#Q4.
l = [1,2,3,4,5]
d3 = {}
for i in range(len(l)):
    d3[i]=l[i]
    
d3


# In[38]:


#Q5.


# In[ ]:


#Q6.


# In[31]:


#Q7.
d = {"A":10000, "B":8000,"C":9000,"D":5000}
for k , v in sorted(d.items()):
    print(k,v)


# In[37]:


#Q7.
SortedValue = {k:v for k , v in sorted(d.items(), key = lambda v : v[1])}
SortedValue


# In[ ]:




