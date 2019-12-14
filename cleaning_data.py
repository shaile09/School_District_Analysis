# %%
# Add the Pandas dependency.
import pandas as pd

# %%
# Files to load
file_to_load = "Resources/missing_grades.csv"

# Read the CSV into a DataFrame
missing_grade_df = pd.read_csv(file_to_load)
missing_grade_df

# %%
# Drop the NaNs.
missing_grade_df.dropna()

# %%
# Fill in the empty rows with "85".
missing_grade_df.fillna(85)

# %%
