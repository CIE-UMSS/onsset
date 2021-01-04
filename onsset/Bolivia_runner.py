
from runner import scenario
import pandas as pd
import os



    # 'Database_lower_ElecPopCalib.csv'
    # 'Database_new_1.csv'
specs_path = os.path.join('Bolivia', 'specs_paper_new.xlsx')
calibrated_csv_path = os.path.join('Bolivia', 'Database_new_4.csv')
results_folder = os.path.join('Bolivia')
summary_folder	= os.path.join('Bolivia')
  
scenario(specs_path, calibrated_csv_path, results_folder, summary_folder)


#%%    
data = pd.read_csv('Bolivia/bo-1-0_0_0_0_0_0.csv', index_col=0)  
sumary = pd.read_csv('Bolivia/bo-1-0_0_0_0_0_0_summary.csv', index_col=0)
df = pd.DataFrame()
df['EnergyPerSettlement2020'] = data['EnergyPerSettlement2020']
df['EnergyPerSettlement2030'] = data['EnergyPerSettlement2030']
df['MinimumOverall2020'] = data['MinimumOverall2020']
df['MinimumOverall2030'] = data['MinimumOverall2030']
df['MinimumOverallLCOE2020'] = data['MinimumOverallLCOE2020']
df['MinimumOverallLCOE2030'] = data['MinimumOverallLCOE2030']
df['NPC2020'] = data['NPC2020']
df['NPC2030'] = data['NPC2030']


