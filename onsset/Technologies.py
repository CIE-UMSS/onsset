#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:22:12 2020

@author: balderrama
"""
from onsset import Technology


def technology_creation(start_year, end_year, grid_price, specs_data, diesel_price, pv_capital_cost_adjust):
    
    technologies = []

    Technology.set_default_values(base_year=start_year,
                                      start_year=start_year,
                                      end_year=end_year,
                                      discount_rate=0.12)
     
    grid_calc = Technology(om_of_td_lines=0.02,
                               distribution_losses=float(specs_data.iloc[0]['GridLosses']),
                               connection_cost_per_hh=125,
                               base_to_peak_load_ratio_type = float(specs_data.iloc[0]['BaseToPeak']),
                               capacity_factor=1,
                               tech_life=30,
                               grid_capacity_investment=float(specs_data.iloc[0]['GridCapacityInvestmentCost']),
                               grid_penalty_ratio=1,
                               grid_price=grid_price,
                               name = 'Grid',
                               code = 1)
    
    technologies.append(grid_calc)
    
    mg_hydro_calc = Technology(om_of_td_lines=0.02,
                                   distribution_losses=0.05,
                                   connection_cost_per_hh=125,
                                   base_to_peak_load_ratio_type = 1,
                                   capacity_factor=0.5,
                                   tech_life=30,
                                   capital_cost={float("inf"): 5000},
                                   om_costs=0.02,
                                   mini_grid=True,
                                   name = 'MG_Hydro_',
                                   code = 7)
    
    technologies.append(mg_hydro_calc)

#    mg_hydro_calc1 = Technology(om_of_td_lines=0.04,
#                                   distribution_losses=0.03,
#                                   connection_cost_per_hh=25,
#                                   base_to_peak_load_ratio_type = 1,
#                                   capacity_factor=0.6,
#                                   tech_life=30,
#                                   capital_cost={float("inf"): 2000},
#                                   om_costs=0.01,
#                                   mini_grid=True,
#                                   name = 'MG_Hydro_Amazonia',
#                                   code = 7)
#    
#    technologies.append(mg_hydro_calc1)
#
#
#    mg_hydro_calc2 = Technology(om_of_td_lines=0.04,
#                                   distribution_losses=0.03,
#                                   connection_cost_per_hh=25,
#                                   base_to_peak_load_ratio_type = 1,
#                                   capacity_factor=0.6,
#                                   tech_life=30,
#                                   capital_cost={float("inf"): 1500},
#                                   om_costs=0.01,
#                                   mini_grid=True,
#                                   name = 'MG_Hydro_Chaco',
#                                   code = 7)
#    
#    technologies.append(mg_hydro_calc2)


   
    mg_wind_calc = Technology(om_of_td_lines=0.02,
                                  distribution_losses=0.05,
                                  connection_cost_per_hh=125,
                                  base_to_peak_load_ratio_type = 0.75,
                                  capital_cost={float("inf"): 2500},
                                  om_costs=0.02,
                                  tech_life=20,
                                  mini_grid=True,
                                  name = 'MG_Wind_',
                                  code = 6)
    
    technologies.append(mg_wind_calc)

#    mg_wind_calc1 = Technology(om_of_td_lines = 0.02,
#                                  distribution_losses = 0.05,
#                                  connection_cost_per_hh = 225,
#                                  base_to_peak_load_ratio_type = 0.55,
#                                  capital_cost={float("inf"): 2000},
#                                  om_costs=0.01,
#                                  tech_life=15,
#                                  mini_grid=True,
#                                  name = 'MG_Wind_Amazonia',
#                                  code = 6)
#    
#    technologies.append(mg_wind_calc1)
#
#
#    mg_wind_calc2 = Technology(om_of_td_lines = 0.02,
#                                  distribution_losses = 0.05,
#                                  connection_cost_per_hh = 225,
#                                  base_to_peak_load_ratio_type = 0.55,
#                                  capital_cost={float("inf"): 2500},
#                                  om_costs=0.01,
#                                  tech_life=15,
#                                  mini_grid=True,
#                                  name = 'MG_Wind_Chaco',
#                                  code = 6)
#    
#    technologies.append(mg_wind_calc2)


    mg_pv_calc = Technology(om_of_td_lines = 0.03,
                                distribution_losses = 0.05,
                                connection_cost_per_hh = 125,
                                base_to_peak_load_ratio_type = 0.9,
                                tech_life=20,
                                om_costs=0.02,
                                capital_cost={float("inf"): 35000},
                                mini_grid=True,
                                name = 'MG_PV_Highlands',
                                code = 5)

    technologies.append(mg_pv_calc)
    
    mg_pv_calc1 = Technology(om_of_td_lines = 0.01,
                                distribution_losses = 0.03,
                                connection_cost_per_hh = 225,
                                base_to_peak_load_ratio_type = 0.5,
                                tech_life = 20,
                                om_costs = 0.01,
                                capital_cost = {float("inf"): 30000},
                                mini_grid = True,
                                name = 'MG_PV_Amazonia',
                                code = 5)

    technologies.append(mg_pv_calc1)    
    
    mg_pv_calc2 = Technology(om_of_td_lines = 0.03,
                                distribution_losses = 0.03,
                                connection_cost_per_hh = 225,
                                base_to_peak_load_ratio_type = 0.5,
                                tech_life = 20,
                                om_costs = 0.01,
                                capital_cost = {float("inf"): 30000},
                                mini_grid = True,
                                name = 'MG_PV_Chaco',
                                code = 5)

    technologies.append(mg_pv_calc2)    
    
    sa_pv_calc = Technology(base_to_peak_load_ratio_type = 0.9,
                                tech_life = 15,
                                om_costs = 0.02,
                                capital_cost={float("inf"): 50700 * pv_capital_cost_adjust,
                                              0.200: 57800 * pv_capital_cost_adjust,
                                              0.100: 76600 * pv_capital_cost_adjust,
                                              0.050: 110500 * pv_capital_cost_adjust,
                                              0.020: 200000 * pv_capital_cost_adjust
                                              },
                                standalone=True,
                                name = 'SA_PV_Highlands',
                                code = 3)
    
    technologies.append(sa_pv_calc)

    sa_pv_calc1 = Technology(base_to_peak_load_ratio_type=0.8,
                                tech_life=20,
                                om_costs=0.01,
                                capital_cost={float("inf"): 60700 * pv_capital_cost_adjust,
                                              0.200: 87800 * pv_capital_cost_adjust,
                                              0.100: 106600 * pv_capital_cost_adjust,
                                              0.050: 120500 * pv_capital_cost_adjust,
                                              0.020: 150000 * pv_capital_cost_adjust
                                              },
                                standalone=True,
                                name = 'SA_PV_Amazonia',
                                code = 3)
    
    technologies.append(sa_pv_calc1)
    
    
    sa_pv_calc2 = Technology(base_to_peak_load_ratio_type=0.8,
                                tech_life=20,
                                om_costs=0.04,
                                capital_cost={float("inf"): 60700 * pv_capital_cost_adjust,
                                              0.200: 87800 * pv_capital_cost_adjust,
                                              0.100: 106600 * pv_capital_cost_adjust,
                                              0.050: 120500 * pv_capital_cost_adjust,
                                              0.020: 150000 * pv_capital_cost_adjust
                                              },
                                standalone=True,
                                name = 'SA_PV_Chaco',
                                code = 3)
    
    technologies.append(sa_pv_calc2)

    mg_diesel_calc = Technology(om_of_td_lines=0.02,
                                    distribution_losses=0.05,
                                    connection_cost_per_hh=125,
                                    base_to_peak_load_ratio_type=0.5,
                                    capacity_factor=0.7,
                                    tech_life=15,
                                    om_costs=0.1,
                                    capital_cost={float("inf"): 10000},
                                    mini_grid=True,
                                    name = 'MG_Diesel_Highlands',
                                    code = 4)
    
    technologies.append(mg_diesel_calc)

    mg_diesel_calc1 = Technology(om_of_td_lines=0.03,
                                    distribution_losses=0.07,
                                    connection_cost_per_hh=100,
                                    base_to_peak_load_ratio_type=0.5,
                                    capacity_factor=0.8,
                                    tech_life=20,
                                    om_costs=0.08,
                                    capital_cost={float("inf"): 15000},
                                    mini_grid=True,
                                    name = 'MG_Diesel_Amazonia',
                                    code = 4)
    
    technologies.append(mg_diesel_calc1)

    mg_diesel_calc2 = Technology(om_of_td_lines=0.05,
                                    distribution_losses=0.07,
                                    connection_cost_per_hh=100,
                                    base_to_peak_load_ratio_type=0.5,
                                    capacity_factor=0.8,
                                    tech_life=20,
                                    om_costs=0.08,
                                    capital_cost={float("inf"): 15000},
                                    mini_grid=True,
                                    name = 'MG_Diesel_Chaco',
                                    code = 4)
    
    technologies.append(mg_diesel_calc2)

    sa_diesel_calc = Technology(base_to_peak_load_ratio_type=0.8,
                                    capacity_factor=0.6,
                                    tech_life=20,
                                    om_costs=0.05,
                                    capital_cost={float("inf"): 12000},
                                    standalone=True,
                                    name = 'SA_Diesel_Highlands',
                                    code = 2)
    
    technologies.append(sa_diesel_calc)
    
    sa_diesel_calc1 = Technology(base_to_peak_load_ratio_type=0.8,
                                    capacity_factor=0.6,
                                    tech_life=20,
                                    om_costs=0.05,
                                    capital_cost={float("inf"): 12000},
                                    standalone=True,
                                    name = 'SA_Diesel_Amazonia',
                                    code = 2)
    
    technologies.append(sa_diesel_calc1)
    
    sa_diesel_calc2 = Technology(base_to_peak_load_ratio_type=0.8,
                                    capacity_factor=0.8,
                                    tech_life=20,
                                    om_costs=0.05,
                                    capital_cost={float("inf"): 12000},
                                    standalone=True,
                                    name = 'SA_Diesel_Chaco',
                                    code = 2)
    
    technologies.append(sa_diesel_calc2)
    
    
    
    surrogate_model_1 = {'name': 'MG_Hybrid_Chaco',
                         'path_LCOE': 'Bolivia/Surrogate_Models/Hybrid/LCOE_Chaco.joblib' ,
                         'path_NPC': 'Bolivia/Surrogate_Models/Hybrid/NPC_Chaco.joblib', 
                         'path_Investment' : 'Bolivia/Surrogate_Models/Hybrid/NPC_Chaco.joblib',
                         'path_PV_Capacity': 'Bolivia/Surrogate_Models/Hybrid/PV_Chaco.joblib' ,
                         'path_Genset_Capacity': 'Bolivia/Surrogate_Models/Hybrid/Genset_Chaco.joblib' ,
                         'path_Battery_Capacity': 'Bolivia/Surrogate_Models/Hybrid/Battery_Chaco.joblib',
                         'Variables' : 10,
                         'var_1' : 'Renewable Invesment Cost',
                         'value_1': 1000,
                         'var_2' : 'Battery Unitary Invesment Cost',
                         'value_2': 300,
                         'var_3' : 'Deep of Discharge',
                         'value_3': 0.02,
                         'var_4' : 'Battery Cycles',
                         'value_4': 7000,
                         'var_5':'GenSet Unitary Invesment Cost',
                         'value_5': 1000,
                         'var_6' : 'Generator Efficiency',
                         'value_6': 0.39,
                         'var_7' : 'Low Heating Value',
                         'value_7': 11,
                         'var_8' : 'Fuel Cost',
                         'var_9' : 'HouseHolds',
                         'var_10' : 'Renewable Energy Unit Total',
                         'value_10': 'PV total output'}                                   
    
    
    mg_hybrid_calc = Technology(om_of_td_lines=0.05,
                                 distribution_losses=0.00,
                                 connection_cost_per_hh=100,
                                 base_to_peak_load_ratio_type = 'surrogate',#
                                 capacity_factor=0.8,
                                 tech_life=10,
                                 om_costs=0.08,
                                 capital_cost={float("inf"): 1500},
                                 mini_grid=True,
                                 name = 'MG_Hybrid_Chaco',
                                 code = 8,
                                 surrogate_model = True,
                                 surrogate_model_data = surrogate_model_1,
                                 tech_life_surrogate = 20)
    
    technologies.append(mg_hybrid_calc)
    
    transportation_cost = []
    
    transportation_cost.append({'diesel_price': diesel_price,
                                'fuel_price': diesel_price,
                                'tech_name': 'MG_Diesel_Highlands',
                                'efficiency': 0.33,
                                'fuel_LHV': 9.9,
                                'diesel_truck_consumption': 33.7,
                                'diesel_truck_volume': 15000})
        
    transportation_cost.append({'diesel_price': diesel_price,
                                'fuel_price': diesel_price,
                                'tech_name': 'MG_Diesel_Amazonia',
                                'efficiency': 0.33,
                                'fuel_LHV': 9.9,
                                'diesel_truck_consumption': 33.7,
                                'diesel_truck_volume': 15000})
    
    transportation_cost.append({'diesel_price': diesel_price,
                                'fuel_price': diesel_price,
                                'tech_name': 'MG_Diesel_Chaco',
                                'efficiency': 0.33,
                                'fuel_LHV': 9.9,
                                'diesel_truck_consumption': 33.7,
                                'diesel_truck_volume': 15000})
    
    transportation_cost.append({'diesel_price': diesel_price,
                                'fuel_price': diesel_price,
                                'tech_name' : 'SA_Diesel_Highlands',
                                'efficiency': 0.28,
                                'fuel_LHV': 9.9,
                                'diesel_truck_consumption': 14,
                                'diesel_truck_volume': 300})
    
    transportation_cost.append({'diesel_price': diesel_price,
                                'fuel_price': diesel_price,
                                'tech_name' : 'SA_Diesel_Amazonia',
                                'efficiency': 0.28,
                                'fuel_LHV': 9.9,
                                'diesel_truck_consumption': 14,
                                'diesel_truck_volume': 300})   


    transportation_cost.append({'diesel_price': diesel_price,
                                'fuel_price': diesel_price,
                                'tech_name' : 'SA_Diesel_Chaco',
                                'efficiency': 0.28,
                                'fuel_LHV': 9.9,
                                'diesel_truck_consumption': 14,
                                'diesel_truck_volume': 300})      
    
    transportation_cost.append({'diesel_price': diesel_price,
                                'fuel_price': diesel_price,
                                'tech_name' : 'MG_Hybrid_Chaco',
                                'diesel_truck_consumption': 33.7,
                                'diesel_truck_volume':  15000,
                                'Surrogate_Models': True})       
    
    # Constraints
    
    tech_constraints = []
    
    tech_constraints.append({'Type': 'mayor',
                             'name': 'MG_Diesel_Highlands',
                             'Column_name': 'Elevation',
                             'bound'      : 800, 
                             'Years'      :  [2020,2030]
                                })
  
    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'MG_Diesel_Amazonia',
                             'Column_name': 'Elevation', 
                             'bound'      : 800, 
                             'Years'      :  [2020,2030]
                                })
    
    tech_constraints.append({'Type': 'minor',
                             'name': 'MG_Diesel_Amazonia',
                             'Column_name': 'HouseHolds', 
                             'bound'      : 550, 
                             'Years'      :  [2020,2030]                          
                                })
    
    tech_constraints.append({'Type': 'mayor',
                             'name':'MG_Diesel_Amazonia',
                             'Column_name':'HouseHolds', 
                             'bound'      : 50, 
                             'Years'      :  [2020,2030]                          
                                })
    
    
    

    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'MG_Diesel_Chaco',
                             'Column_name': 'Elevation', 
                             'bound'      : 800, 
                             'Years'      :  [2020,2030]
                                })
    
    tech_constraints.append({'Type': 'minor',
                             'name': 'MG_Diesel_Chaco',
                             'Column_name': 'Y_deg', 
                             'bound'      : -17, 
                             'Years'      :  [2020,2030]                          
                                })

    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'SA_PV_Highlands',
                             'Column_name': 'Pop2012', 
                             'bound'      : 1926, 
                             'Years'      :  [2020,2030]                          
                                })

    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'SA_PV_Amazonia',
                             'Column_name': 'Pop2012', 
                             'bound'      : 1926, 
                             'Years'      :  [2020,2030]                          
                                })

    tech_constraints.append({'Type'       : 'mayor',
                             'name'       : 'SA_PV_Chaco',
                             'Column_name': 'Pop2012', 
                             'bound'      : 1926, 
                             'Years'      :  [2020,2030]                          
                                })
##########################################
    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'SA_Diesel_Highlands',
                             'Column_name': 'PopStartYear', 
                             'bound'      : 500, 
                             'Years'      :  [2020,2030]                          
                                })
    
    tech_constraints.append({'Type'       : 'mayor',
                             'name'       : 'SA_Diesel_Amazonia',
                             'Column_name': 'PopStartYear', 
                             'bound'      : 500, 
                             'Years'      :  [2020,2030]                         
                                })

    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'SA_Diesel_Amazonia',
                             'Column_name': 'PopStartYear', 
                             'bound'      : 500000, 
                             'Years'      :  [2020,2030]                         
                                })

    tech_constraints.append({'Type'       : 'mayor',
                             'name'       : 'SA_Diesel_Chaco',
                             'Column_name': 'PopStartYear', 
                             'bound'      : 500000, 
                             'Years'      :  [2020,2030]                         
                                })

##########################################
    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'MG_PV_Highlands',
                             'Column_name': 'PopStartYear', 
                             'bound'      :  500, 
                             'Years'      :  [2030]     
                                })

    tech_constraints.append({'Type'       : 'mayor',
                             'name'       : 'MG_PV_Highlands',
                             'Column_name': 'Elevation', 
                             'bound'      :  800, 
                             'Years'      :  [2030]     
                                })

    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'MG_PV_Amazonia',
                             'Column_name': 'PopStartYear', 
                             'bound'      :  500, 
                             'Years'      :  [2030]     
                                })

    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'MG_PV_Amazonia',
                             'Column_name': 'Elevation', 
                             'bound'      :  800, 
                             'Years'      :  [2030]     
                                })
    tech_constraints.append({'Type': 'mayor',
                             'name': 'MG_PV_Amazonia',
                             'Column_name': 'Y_deg', 
                             'bound'      : -17, 
                             'Years'      :  [2030]                          
                                })   
    
    
    tech_constraints.append({'Type': 'minor',
                             'name': 'MG_PV_Chaco',
                             'Column_name': 'Y_deg', 
                             'bound'      : -17, 
                             'Years'      :  [2020]                          
                                })    
    tech_constraints.append({'Type'       : 'minor',
                             'name'       : 'MG_PV_Chaco',
                             'Column_name': 'PopStartYear', 
                             'bound'      :  500, 
                             'Years'      :  [2020]  })    

    # Constraints
    
    demand_constraints = []
    
    demand_constraints.append({'name': 'Amazonia',
                               'path': 'Bolivia/Surrogate_Models/Demand/demand_regression_Amazonia.joblib',
                               'path_peak_load_ratio': 'Bolivia/Surrogate_Models/Hybrid/Peak_to_Base.joblib',
                               'constraints': 3,
                               'Type_1': 'minor',
                               'Column_name_1': 'Elevation',
                               'bound_1'      : 800, 
                               'Type_2': 'mayor',
                               'Column_name_2': 'HouseHolds mayor',
                               'bound_2'      : 50, 
                               'Type_3': 'minor',
                               'Column_name_3': 'HouseHolds minor',
                               'bound_3'      : 550, 
                               'Variables' : 1,
                               'Var_1' : 'HouseHolds'
                                })
    
    demand_constraints.append({'name': 'Amazonia minor',
                               'path': 'Bolivia/Surrogate_Models/Demand/demand_regression_Amazonia.joblib',
                               'path_peak_load_ratio': 'Bolivia/Surrogate_Models/Hybrid/Peak_to_Base.joblib',
                               'constraints': 2,
                               'Type_1': 'minor',
                               'Column_name_1': 'Elevation',
                               'bound_1'      : 800, 
                               'Type_2': 'minor',
                               'Column_name_2': 'HouseHolds minor',
                               'bound_2'      : 50, 
                               'Variables' : 1,
                               'Var_1' : 'HouseHolds'
                                })

    demand_constraints.append({'name': 'Amazonia mayor',
                               'path': 'Bolivia/Surrogate_Models/Demand/demand_regression_Amazonia.joblib',
                               'path_peak_load_ratio': 'Bolivia/Surrogate_Models/Hybrid/Peak_to_Base.joblib',
                               'constraints': 2,
                               'Type_1': 'minor',
                               'Column_name_1': 'Elevation',
                               'bound_1'      : 800, 
                               'Type_2': 'mayor',
                               'Column_name_2': 'HouseHolds mayor',
                               'bound_2'      : 550, 
                               'Variables' : 1,
                               'Var_1' : 'HouseHolds'                               
                                })    
    
    
    # demand_constraints.append({'name': 'Chaco',
    #                             'path': 'Bolivia/Surrogate_Models/Demand/demand_regression_Chaco.joblib',
    #                             'constraints': 2,
    #                             'Type_1': 'minor',
    #                             'Column_name_1': 'Y_deg',
    #                             'bound_1'      : 800, 
    #                             'Type_2': 'minor',
    #                             'Column_name_2': 'Y_deg',
    #                             'bound_2'      : -17, 
    #                             'Variables' : 1,
    #                             'Var_1' : 'HouseHolds'
    #                             })
    
    demand_constraints.append({'name': 'Highlands',
                                'path': 'Bolivia/Surrogate_Models/Demand/demand_regression_HighLands.joblib',
                                'path_peak_load_ratio': 'Bolivia/Surrogate_Models/Hybrid/Peak_to_Base.joblib',
                                'constraints': 1,
                                'Type_1': 'mayor',
                                'Column_name_1': 'Elevation',
                                'bound_1'      : 800, 
                                'Variables' : 1,
                                'Var_1' : 'HouseHolds'
                                })
    
    return technologies, transportation_cost, tech_constraints, demand_constraints
    