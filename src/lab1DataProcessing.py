#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
myList = []
with open(r'C:\Users\Iulia\Desktop\lab1 ia\iris.data') as csvfile:
 readCSV = csv.reader(csvfile, delimiter=',')
 for row in readCSV:
  if len(row) == 5:
   myList.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])


# In[2]:


import numpy as np
npArray = np.array(myList)


# In[3]:


print("DATASET:")
print(npArray.shape)
print(npArray)


# In[30]:


col0_min = np.min(npArray[:,0])
col0_max=np.max(npArray[:,0])
col0_med=(col0_min+col0_max)/2
col_sortata=npArray[npArray[:, 0].argsort()][:,0]
print("Minimul primei coloane: %f" % col0_min)
print("Maximul primei coloane: %f" % col0_max)
print("Media primei coloane: %f" % col0_med)
if len(col_sortata)%2==0:
    print("Mediana primei coloane: %f" % col_sortata[int(npArray.shape[0]/2)])
else:
    print("Mediana primei coloane: %f" % (col_sortata[int(npArray.shape[0]/2)]+col_sortata[int(npArray.shape[0]/2)+1])/2)


# In[31]:


col1_min = np.min(npArray[:,1])
col1_max=np.max(npArray[:,1])
col1_med=(col1_min+col1_max)/2
col_sortata=npArray[npArray[:, 1].argsort()][:,1]
print("Minimul coloanei 2: %f" % col1_min)
print("Maximul coloanei 2: %f" % col1_max)
print("Media coloanei 2: %f" % col1_med)
if len(col_sortata)%2==0:
    print("Mediana coloanei 2: %f" % col_sortata[int(npArray.shape[0]/2)])
else:
    print("Mediana coloanei 2: %f" % (col_sortata[int(npArray.shape[0]/2)]+col_sortata[int(npArray.shape[0]/2)+1])/2)


# In[42]:


col2_min = np.min(npArray[:,2])
col2_max=np.max(npArray[:,2])
col2_med=(col2_min+col2_max)/2
col_sortata=npArray[:,2]
col_sortata=np.sort(col_sortata)
print("Minimul coloanei 3: %f" % col2_min)
print("Maximul coloanei 3: %f" % col2_max)
print("Media coloanei 3: %f" % col2_med)
if len(col_sortata)%2==0:
    print("Mediana coloanei 3: %f" % col_sortata[int(npArray.shape[0]/2)])
else:
    print("Mediana coloanei 3: %f" % (col_sortata[int(npArray.shape[0]/2)]+col_sortata[int(npArray.shape[0]/2)+1])/2)


# In[43]:


col3_min = np.min(npArray[:,3])
col3_max=np.max(npArray[:,3])
col3_med=(col3_min+col3_max)/2
col_sortata=npArray[:,3]
col_sortata=np.sort(col_sortata)
print("Minimul coloanei 4: %f" % col3_min)
print("Maximul coloanei 4: %f" % col3_max)
print("Media coloanei 4: %f" % col3_med)
if len(col_sortata)%2==0:
    print("Mediana coloanei 4: %f" % col_sortata[int(npArray.shape[0]/2)])
else:
    print("Mediana coloanei 4: %f" % (col_sortata[int(npArray.shape[0]/2)]+col_sortata[int(npArray.shape[0]/2)+1])/2)


# In[48]:


print('NORMALIZAREA COLOANELOR:')
npArray[:,0]= (npArray[:,0]-min(npArray[:,0])) / (max(npArray[:,0])-min(npArray[:,0]))
npArray[:,1] = (npArray[:,1]-min(npArray[:,1])) / (max(npArray[:,1])-min(npArray[:,1]))
npArray[:,2] = (npArray[:,2]-min(npArray[:,2])) / (max(npArray[:,2])-min(npArray[:,2]))
npArray[:,3] = (npArray[:,3]-min(npArray[:,3])) / (max(npArray[:,3])-min(npArray[:,3]))
print("Rezultat:")
print(npArray)


# In[49]:


ponderi=np.array([0.2,1.1,-0.9,1])


# In[63]:


print(np.dot(npArray,ponderi).shape)


# In[65]:


npArray=np.append(npArray, values=np.dot(npArray,ponderi))


# In[67]:


print("Ponderi:")
print(npArray)


# In[ ]:




