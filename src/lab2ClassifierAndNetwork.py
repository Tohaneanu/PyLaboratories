#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# In[2]:


a = np.array([2, 1, 2])
b = np.array([[1, -1, 4]]).T

# In[3]:


print("Produsul scalar:")
print(np.dot(a, b))

# In[4]:


from scipy import spatial

result = 1 - spatial.distance.cosine(a, b)

# In[5]:


print(result)

# In[6]:


from numpy.linalg import norm
from numpy import array

# In[7]:


print("Norma vector 1: ")
norma1 = norm(a)
print(norma1)

# In[8]:


print("Norma vector 2:")
norma2 = norm(b)
print(norma2)

# In[9]:


cos = np.dot(a, b) / (norma1 * norma2)

# In[10]:


print("Cosinus dintre vectori:")
print(cos)

# In[11]:


print("Clasificator:")


# In[12]:


def functia(vector):
    if vector[0] + vector[1] + vector[2] > 0:
        print("+++++++++")
    else:
        print("---------")


# In[13]:


functia([-1, -1, -1])
functia([-1, -1, 1])
functia([1, -1, -1])
functia([1, -1, 1])
functia([-1, 1, 1])
functia([1, -1, 1])
functia([1, 1, -1])
functia([1, 1, 1])

# In[14]:


print("Reteaua de memorie:")

# In[15]:


lista = []


def retea(vector, count=None):
    if count is None:
        count = 0
    intrare = vector.copy()
    count += 1
    if vector[1] - vector[2] > 0:
        vector[0] = 1
    elif vector[1] - vector[2] < 0:
        vector[0] = -1
    if vector[0] - vector[2] > 0:
        vector[1] = 1
    elif vector[0] - vector[2] < 0:
        vector[1] = -1
    if -vector[1] - vector[0] > 0:
        vector[2] = 1
    elif -vector[1] - vector[0] < 0:
        vector[2] = -1
    if intrare == vector:
        if count == 1:
            print("Iesire finala, ce nu se poate modifica!")
        print("Final:")
        print(vector)
        if vector not in lista:
            lista.append(vector)
    else:
        print(f"Iesirea {count}: {vector} ")
        retea(vector, count=count)


# In[16]:


print("intrare noua ###########################")
retea([-1, -1, -1])
print("intrare noua ###########################")
retea([-1, -1, 1])
print("intrare noua ###########################")
retea([1, -1, -1])
print("intrare noua ###########################")
retea([1, -1, 1])
print("intrare noua ###########################")
retea([-1, 1, 1])
print("intrare noua ###########################")
retea([1, -1, 1])
print("intrare noua ###########################")
retea([1, 1, -1])
print("intrare noua ###########################")
retea([1, 1, 1])
print()
print(f" Toate iesirile posibile sunt:   {lista}")

