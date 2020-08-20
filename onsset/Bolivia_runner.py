
from runner import scenario
import pandas as pd
import os
'''Check if the demand if the constraints are applyied for 2020'''


    # 'Database_lower_ElecPopCalib.csv'
    # 'Database_new_1.csv'
specs_path = os.path.join('Bolivia', 'specs_paper_new.xlsx')
calibrated_csv_path = os.path.join('Bolivia', 'Database_new_4.csv')
results_folder = os.path.join('Bolivia')
summary_folder	= os.path.join('Bolivia')
  
scenario(specs_path, calibrated_csv_path, results_folder, summary_folder)
    
data = pd.read_csv('Bolivia/bo-1-0_0_0_0_0_0.csv', index_col=0)  

df = pd.DataFrame()
df['Demand_Name2020'] = data['Demand_Name2020']
df['Households2020'] = data['NewConnections2020']/data['NumPeoplePerHH']
df['Elevation'] = data['Elevation']
df['Demand_Name2030'] = data['Demand_Name2030']
df['Households2030'] = data['NewConnections2030']/data['NumPeoplePerHH']

#%%
booleans1 = pd.DataFrame()

df1 = df.loc[df['Demand_Name2020'] == 'Amazonia']

booleans1['Elevation'] = list(df['Elevation'] < 800)
booleans1['Households2020 mayor'] = list(df['Households2020'] >= 50)
booleans1['Households2020 minor'] = list(df['Households2020'] < 550)

booleans1['clasification'] = booleans1.all(axis=1)  

df11 = pd.DataFrame()
df11 = booleans1.loc[booleans1['clasification']==True]

comparation = df11.index == df1.index
print(comparation.all())

#%%

booleans2 = pd.DataFrame()

df2 = df.loc[df['Demand_Name2020'] == 'Amazonia minor']

booleans2['Elevation'] = list(df['Elevation'] < 800)
booleans2['Households2020 minor'] = list(df['Households2020'] < 50)

booleans2['clasification'] = booleans2.all(axis=1)  

df21 = pd.DataFrame()
df21 = booleans2.loc[booleans2['clasification']==True]

comparation2 = df21.index == df2.index
print(comparation2.all())

#%%

booleans3 = pd.DataFrame()

df3 = df.loc[df['Demand_Name2020'] == 'Amazonia mayor']

booleans3['Elevation'] = list(df['Elevation'] < 800)
booleans3['Households2020 minor'] = list(df['Households2020'] >= 550)

booleans3['clasification'] = booleans3.all(axis=1)  

df31 = pd.DataFrame()
df31 = booleans3.loc[booleans3['clasification']==True]

comparation3 = df31.index == df3.index
print(comparation3.all())

#%%

booleans4 = pd.DataFrame()

df4 = df.loc[df['Demand_Name2020'] == 'Highlands']

booleans4['Elevation'] = list(df['Elevation'] >= 800)

booleans4['clasification'] = booleans4.all(axis=1)  

df41 = pd.DataFrame()
df41 = booleans4.loc[booleans4['clasification']==True]

comparation4 = df41.index == df4.index
print(comparation4.all())




























