
# coding: utf-8

# In[37]:

import pandas as pd


# In[38]:

data_nulls = pd.read_csv("WISE_NEA_COMET_DISCOVERY_STATISTICS.csv")


# In[39]:

###Since comets do not have PHA classification they must be removed


# In[40]:

column = data_nulls['PHA']
rows_to_remove = []
index = 0
for i in column:
    if i == 'n/a':
        rows_to_remove.append(index)
    index += 1
data = data_nulls.drop(rows_to_remove)


# In[41]:

data


# In[ ]:



