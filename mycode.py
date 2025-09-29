import pandas as pd
import os 

# create a sample dataframe with columns names
data = {'Name':['Alice','Bob','Charlie'],
        'Age':[25,30,35],
        'CIty':['New York','Los Angles','Chicago']
        }

df = pd.DataFrame(data)

# Adding new row to df for v2
new_row_loc = {'Name':'GF','Age':20,'City':'city1'}
df.loc[len(df.index)] = new_row_loc
# Adding new row to df for v3
new_row_loc2 = {'Name':'GF2','Age':30,'City':'city2'}
df.loc[len(df.index)] = new_row_loc2
# Ensure the data directory exists at the root level
Data_dir = 'data'
os.makedirs(Data_dir,exist_ok=True)
# Define the file path
file_path = os.path.join(Data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f'csv file saved to {file_path}')
