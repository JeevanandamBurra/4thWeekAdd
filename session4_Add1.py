
# coding: utf-8

# ## 1) Write a Python program which accepts a list named : randomList = ['a', 0,2]. Use exception handling using try-catch which gives the output as:

# In[23]:


lst1=['a',0,2]
lst1


# In[25]:


def func(lst):
    for i in lst:        
        try:
            x= 1/i        
        except Exception as ex:
            print('execption {}'.format(ex.__class__))            
        else:
            print('the Reciproal {} is {}:'.format(i,x))
        finally:
            print('The Entry is',i) 


# In[26]:


func(lst1)


# ## 2) Array out of Bound Exception 
# ## Write a Python program to give exception “Array Out of Bound” if the user wants to access the elements beyond the list size (use try and except)

# In[41]:


lst1=[1,2,3,4]
inp=int(input("enter the index to get the element:"))
try:
    x=lst1[inp]
    
except Exception as ex:
    print(ex)
else:
    print(x)


# In[40]:




