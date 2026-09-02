#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[11]:


#python data structures
#list()
   #empty_list[]
empty_list=[]
print(empty_list)

print(type(empty_list))

nums=[10,20,30]
print(nums)

fruits=["apple","banana"]
print(fruits)

mixed_types=[10,3.07,'a','true']
print(mixed_types)


# In[14]:


#len()
nums=[1,2,3,1,2]
print(len(nums))

print(nums[3])

print(nums[1:4])


# In[19]:


#Append()
fruits=["apple","banana"]
fruits.append("mango")
print(fruits)

fruits.remove("banana")
print(fruits)


# In[24]:


#index

num=[1,2,3,4,5]
num.index(2)


# In[25]:


#count()

print(nums.count(2))


# In[28]:


#extend()

nums=[1,2,3]
nums2=[4,5,6]
nums.extend(nums2)
print(num)


# In[33]:


#insert()

nums=[10,20,40]
nums.insert(2,30)
print(nums)


# In[44]:


#sort

nums=[25,10,10,64]
nums.sort()
print(nums)


# In[48]:


#sort

fruits=['apple','mango','banana','cherry']
fruits.sort()
print(fruits)


# In[ ]:




