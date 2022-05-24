#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1.

D = {}


# In[2]:


#Q2.

D1 = {"foo":42}
D1.values()


# In[ ]:


#Q3.

A data can be stores in dict in a from of keys and values in a curly backets.

Whereas 

In list data can be store in a form of values only in a square backets.


# In[3]:


#Q4.

spam = {'bar': 100}

spam['foo']

We get a KeyError if we try to access spam['foo'].


# In[8]:


#Q5.

spam = {'cat'}
'cat'in spam

This expression will gave True.


# In[9]:


#Q5.

spam = {'cat'}
'cat'in spam.keys()
This expression will give an Attribute error.


# In[10]:


#Q6.

spam = {'cat'}
'cat'in spam
This expression will gave True.


# In[11]:


#Q6.

spam = {'cat'}
'cat' in spam.values()
This expresion will give an attribute error.


# In[51]:


#Q7.

spam = {"hello":'Mayank'}

if "color"   not in spam.keys():
    spam.update({"color":'black'})       
    

spam


# In[ ]:





# In[ ]:




