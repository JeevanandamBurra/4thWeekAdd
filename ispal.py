
# coding: utf-8

# In[5]:


def ispal(str1):
    rev_str = reversed(str1)
    if list(str1) == list(rev_str):
        print("It is palindrome")
    else:
        print("It is not palindrome")

