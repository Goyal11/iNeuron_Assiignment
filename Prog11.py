#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Q1.


Length = int(input("Enter the length: "))
S =  "Cruise was born on July 3, 1962, in Syracuse, New York,[4] to electrical engineer Thomas Cruise Mapother III (1934–1984) and special education teacher Mary Lee (née Pfeiffer; 1936–2017).[5] His parents were both from Louisville, Kentucky,[6] and had English, German, and Irish ancestry.[7][8] Cruise has three sisters named Lee Anne, Marian, and Cass. One of his cousins, William Mapother, is also an actor who has appeared alongside Cruise in five films.[9] \n Cruise grew up in near poverty and had a Catholic upbringing. He later described his father as a merchant of chaos ,[10] a bully, and a coward who beat his children. \n He elaborated, [My father] was the kind of person where, if something goes wrong, they kick you. It was a great lesson in my life—how he'd lull you in, \n make you feel safe and then, bang! For me, \n it was like, 'There's something wrong with this guy. Don't trust him. Be careful around him"
A = S.split(" ")
for i in A:
    i = i.replace(",","")
    if len(i)>Length:
        print(i)
    


# In[6]:


#Q2.
l = []
char = int(input("Enter the index which u want to remove: "))
s = "Hii, I am Mayank @ I am a Data Analyst"
for i in range(len(s)):
    if i!= char:
        l.append(s[i])
"".join(l)    
    
    

    
    


# In[23]:


#Q3.
s1 = "I am Mayank and I am a student "
s2 = "I am a Data Analyst"
A = s1.split("and")
# I am Mayank and I am a Data Analyst

#nt(A,s2) 
#A.append("")
#print(A,s2)
s2.join(A)
    


# In[4]:


#Q4.
a = input("Enter the string: ")
if a[0:2]=="0b":
    s=set(a[2:])
    if "0"in s :
        s.remove("0")
    if "1" in s:    
        s.remove("1")
    if len(s)==0:
        print("Is a binary string")
    else:
        print("Is not a binary string")
else:
    print("Not a binary string")


# In[30]:


#Q5.

s1 = "I am Mayank and I am Data Analyst and I am Mechanical Engineer"
s2 = "I am pursing a course of Data Science from Ineuron and I want to go in Data Analytics which is a domain of Data science as a Data Analyst"

a = s1.split(" ")
b = s2.split(" ")

for i in a:
    if i in b:
        continue
    else:
        print(i)
    
        

    


# In[33]:


s1 = "I am Mayank and I am Data Analyst and I am Mechanical Engineer"
s2 = "I am pursing a course of Data Science from Ineuron and I want to go in Data Analytics which is a domain of Data science as a Data Analyst"

a = set(s1.split(" "))
b = set(s2.split(" "))

uncommon = a.difference(b)
uncommon


# In[38]:


#Q6.
s1 = "I am Mayank and I am Data Analyst and I am Mechanical Engineer"

for i in set(s1):
    print(i, s1.count(i))


# In[45]:


#Q7.
s = "Hii, I am Mayank @ I am a Data Analyst"
l = ["@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|","\",:,;,,""<",">",".","?","/"]

for i in s:
    if i in l:
        print(i)
    


# In[ ]:





# In[ ]:





# In[ ]:




