#%%
import pandas as pd
import os

# %%
dataFile = os.path.join(os.getcwd(), 'dataOne.csv')

# %%
dataFilePD = pd.read_csv(dataFile)

#%%
dataFile.head(100)


# %%
dataFilePD.describe()

#%%
dataFile("Gender")#.describe()


# %%
