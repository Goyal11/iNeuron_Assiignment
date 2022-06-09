#!/usr/bin/env python
# coding: utf-8

# In[ ]:



NO ,Pyinputplus is not included with Python Standard library 


# In[ ]:


#Q2.

PyInputPlus commonly imported with import pyinputplus as pypi Because it is not included in python standard library
so we have seprately install it and then import it and use alias pypi when we have to call it .


# In[ ]:


#Q3.

inputint() takes integer values and return integer values.

Whereas  

inputfloat() takes integer/Float values and return Float values only.


# In[2]:




get_ipython().system('pip install pyinputplus')


# In[3]:


import pyinputplus as pyip


# In[3]:


#Q4. 

pyip.inputInt(min =0 , max = 99)


# In[ ]:


#Q5.

We use REGEXES to specify to take a list of regular expression strings to check what are the valid 
pyinputplus function or which one to reject


# In[7]:


#Q6.

H =  pyip.inputStr(limit=3)


# In[6]:


#Q7.
E = pyip.inputStr(limit=3, default = 'Hello')


# In[ ]:




