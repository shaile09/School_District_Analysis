# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies
import pandas as pd


# %%
# We can create a Pandas Series from a raw list
data_series = pd.Series(["UCLA", "UC Berkeley", "UC Irvine",
                         "University of Central Florida", "Rutgers University"])
data_series


# %%
# Convert a list of dictionarys into a dataframe
states_dicts = [{"STATE": "New Jersey", "ABBREVIATION": "NJ"},
                {"STATE": "New York", "ABBREVIATION": "NY"}]

df_states = pd.DataFrame(states_dicts)
df_states


# %%
# Convert a single dictionary containing lists into a dataframe
df = pd.DataFrame(
    {"Dynasty": ["Early Dynastic Period", "Old Kingdom"],
     "Pharoh": ["Thinis", "Memphis"]
     }
)
df



# %%
