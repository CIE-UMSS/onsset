
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
    
data = pd.read_csv('Bolivia/bo-1-0_0_0_0_0_0.csv', index_col=0)  
df = pd.DataFrame()
df['MG_Hybrid_ChacoFuelCost2020'] = data['MG_Hybrid_ChacoFuelCost2020']
df['MG_Hybrid_Chaco2020'] = data['MG_Hybrid_Chaco2020']
df['MG_Hybrid_Chaco2030'] = data['MG_Hybrid_Chaco2030']
df['InvestmentCost2020'] = data['InvestmentCost2020']
df['InvestmentCost2030'] = data['InvestmentCost2030']
df['MinimumOverall2020'] = data['MinimumOverall2020']
df['MinimumOverallLCOE2020'] = data['MinimumOverallLCOE2020']
df['NewCapacity2020'] =  data['NewCapacity2020']
df['NewCapacity2030'] =  data['NewCapacity2030']
df['PVcapacity2020'] =  data['PVcapacity2020']
df['PVcapacity2030'] =  data['PVcapacity2030']
df['GenSetcapacity2020'] =  data['GenSetcapacity2020']
df['GenSetcapacity2030'] =  data['GenSetcapacity2030']
df['Batterycapacity2020'] =  data['Batterycapacity2020']
df['Batterycapacity2030'] =  data['Batterycapacity2030']