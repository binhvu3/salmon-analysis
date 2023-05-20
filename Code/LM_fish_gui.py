# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:03:29 2023

@author: blackbuh
"""

import tkinter as tk
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


# read the training data from a CSV file
data = pd.read_csv("C:\\Users\\blackbuh\\MyPythonScripts\\gui_test.csv")

# convert categorical variables to dummy variables
moon_phase_dummies = pd.get_dummies(data['moon_phase'], prefix='moon_phase')
drift_location_dummies = pd.get_dummies(data['drift_location'], prefix='drift_location')
nets_dummies = pd.get_dummies(data['nets'], prefix='nets')

#  moon dummies
third_quarter_dummies = moon_phase_dummies.loc[moon_phase_dummies['moon_phase_Third Quarter'] == 1].iloc[0].to_list()
full_moon_dummies = moon_phase_dummies.loc[moon_phase_dummies['moon_phase_Full Moon'] == 1].iloc[0].to_list()
first_quarter_dummies = moon_phase_dummies.loc[moon_phase_dummies['moon_phase_First Quarter'] == 1].iloc[0].to_list()
new_moon_dummies = moon_phase_dummies.loc[moon_phase_dummies['moon_phase_New Moon'] == 1].iloc[0].to_list()

# drift_location dummies

drift_location_1 =	drift_location_dummies.loc[drift_location_dummies['drift_location_All'] == 1].iloc[0].to_list()
drift_location_2 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Area 3'] == 1].iloc[0].to_list()
drift_location_3 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Area 3, KRSHA'] == 1].iloc[0].to_list()
drift_location_4 =	drift_location_dummies.loc[drift_location_dummies['drift_location_District Wide except Chinitna Bay Sub'] == 1].iloc[0].to_list()
drift_location_5 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Area 1'] == 1].iloc[0].to_list()
drift_location_6 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Area 1 & Expanded Corridor'] == 1].iloc[0].to_list()
drift_location_7 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Area 1&2, Ex Ken/Kas Sec'] == 1].iloc[0].to_list()
drift_location_8 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Area 1, Ex Ken/Kas Sec'] == 1].iloc[0].to_list()
drift_location_9 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Area 1, Ex. Ken/Kas & AP sec'] == 1].iloc[0].to_list()
drift_location_10 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Area 1, Exp. Ken/Kas, & Anchor Pt.'] == 1].iloc[0].to_list()
drift_location_11 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Areas 1 & 3, Ex. Ken/Kas sec'] == 1].iloc[0].to_list()
drift_location_12 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Areas 1, 3 and 4'] == 1].iloc[0].to_list()
drift_location_13 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Areas 3'] == 1].iloc[0].to_list()
drift_location_14 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Drift Areas 3 & 4'] == 1].iloc[0].to_list()
drift_location_15 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Exp. Ken/Kas, & Anchor Pt.'] == 1].iloc[0].to_list()
drift_location_16 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Expanded Kenai & Kasilof Sections'] == 1].iloc[0].to_list()
drift_location_17 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Kasilof River Special Harvest Area'] == 1].iloc[0].to_list()
drift_location_18 =	drift_location_dummies.loc[drift_location_dummies['drift_location_Kasilof Section'] == 1].iloc[0].to_list()
drift_location_19 =	drift_location_dummies.loc[drift_location_dummies['drift_location_None'] == 1].iloc[0].to_list()


# nets dummies

nets_both_dummies = nets_dummies.loc[nets_dummies['nets_both'] ==1].iloc[0].to_list()
nets_drift_dummies = nets_dummies.loc[nets_dummies['nets_drift'] ==1].iloc[0].to_list()
nets_no_nets_dummies = nets_dummies.loc[nets_dummies['nets_no_nets'] ==1].iloc[0].to_list()
nets_set_dummies = nets_dummies.loc[nets_dummies['nets_set'] ==1].iloc[0].to_list()

# concatenate dummy variables with original data
data = pd.concat([data[['water_temp', 'discharge']], moon_phase_dummies, drift_location_dummies, nets_dummies, data[['fish_count']]], axis=1)

# create X and y arrays from the data
X = data.drop('fish_count', axis=1).values
y = data["fish_count"].values

# create linear regression model
model = LinearRegression()

# train the model
model.fit(X, y)

# create the GUI
root = tk.Tk()
root.title("Fish Count Predictor")

# create input fields
tk.Label(root, text="Water Temperature").grid(row=0)
water_temp = tk.Entry(root)
water_temp.grid(row=0, column=1)

tk.Label(root, text="Moon Phase").grid(row=1)
moon_phase = tk.StringVar(root)
moon_phase.set('New Moon') # default value
moon_phase_dropdown = tk.OptionMenu(root, moon_phase, 'New Moon', 'First Quarter','Full Moon', 'Third Quarter')
moon_phase_dropdown.grid(row=1, column=1)



tk.Label(root, text="Discharge").grid(row=2)
discharge = tk.Entry(root)
discharge.grid(row=2, column=1)

tk.Label(root, text='Drift Location').grid(row=3, column=0)
drift_location = tk.StringVar(root)
drift_location.set('None') # default value
drift_location_dropdown = tk.OptionMenu(root, drift_location, 'None', 'Kasilof Section', 
                                         'District Wide except Chinitna Bay Sub', 'Drift Area 1', 
                                         'Drift Area 1, Ex Ken/Kas Sec', 'Expanded Kenai & Kasilof Sections', 
                                         'Drift Area 1, Exp. Ken/Kas, & Anchor Pt.', 'Exp. Ken/Kas, & Anchor Pt.', 
                                         'Drift Areas 3 & 4', 'All', 'Kasilof River Special Harvest Area', 
                                         'Drift Area 1&2, Ex Ken/Kas Sec', 'Area 3', 'Area 3, KRSHA', 
                                         'Drift Areas 3', 'Drift Areas 1, 3 and 4', 
                                         'Drift Areas 1 & 3, Ex. Ken/Kas sec', 'Drift Area 1 & Expanded Corridor', 
                                         'Drift Area 1, Ex. Ken/Kas & AP sec')
drift_location_dropdown.grid(row=3, column=1)

tk.Label(root, text="Nets").grid(row=4)
nets = tk.StringVar(root)
nets.set('no_nets') # default value
nets_dropdown = tk.OptionMenu(root, nets, 'no_nets', 'both', 'set', 'drift')
nets_dropdown.grid(row=4, column=1)

# function to predict fish count
def predict_fish_count():
    # get inputs and convert to float
    water_temp_value = np.log(float(water_temp.get()))
    moon_phase_value = moon_phase.get()
   
    
    discharge_value = np.log(float(discharge.get()))
    drift_location_value = drift_location.get()
    nets_value = nets.get()
    
    
    if moon_phase_value == 'New Moon':
        moon_phase_value = new_moon_dummies
    elif moon_phase_value == 'Third Quarter':
        moon_phase_value = third_quarter_dummies
    elif moon_phase_value == 'Full Moon':
        moon_phase_value = full_moon_dummies
    else: 
        moon_phase_value = first_quarter_dummies
        
    if drift_location_value  == 'All': drift_location_value = drift_location_1
    elif drift_location_value == 'Area 3': drift_location_value = drift_location_2
    elif drift_location_value == 'Area 3, KRSHA': drift_location_value = drift_location_3
    elif drift_location_value == 'District Wide except Chinitna Bay Sub': drift_location_value = drift_location_4
    elif drift_location_value == 'Drift Area 1': drift_location_value = drift_location_5
    elif drift_location_value == 'Drift Area 1 & Expanded Corridor': drift_location_value = drift_location_6
    elif drift_location_value == 'Drift Area 1&2, Ex Ken/Kas Sec': drift_location_value = drift_location_7
    elif drift_location_value == 'Drift Area 1, Ex Ken/Kas Sec': drift_location_value = drift_location_8
    elif drift_location_value == 'Drift Area 1, Ex. Ken/Kas & AP sec': drift_location_value = drift_location_9
    elif drift_location_value == 'Drift Area 1, Exp. Ken/Kas, & Anchor Pt.': drift_location_value = drift_location_10
    elif drift_location_value == 'Drift Areas 1 & 3, Ex. Ken/Kas sec': drift_location_value = drift_location_11
    elif drift_location_value == 'Drift Areas 1, 3 and 4': drift_location_value = drift_location_12
    elif drift_location_value == 'Drift Areas 3': drift_location_value = drift_location_13
    elif drift_location_value == 'Drift Areas 3 & 4': drift_location_value = drift_location_14
    elif drift_location_value == 'Exp. Ken/Kas, & Anchor Pt.': drift_location_value = drift_location_15
    elif drift_location_value == 'Expanded Kenai & Kasilof Sections': drift_location_value = drift_location_16
    elif drift_location_value == 'Kasilof River Special Harvest Area': drift_location_value = drift_location_17
    elif drift_location_value == 'Kasilof Section': drift_location_value = drift_location_18
    elif drift_location_value == 'None': drift_location_value = drift_location_19
 
        
    if nets_value == 'no_nets': nets_value = nets_no_nets_dummies
    elif nets_value == 'both': nets_value = nets_both_dummies
    elif nets_value == 'set': nets_value = nets_set_dummies
    elif nets_value == 'drift': nets_value = nets_drift_dummies  
    
       
    
    
    new_data = []
    new_data.append(water_temp_value)
    new_data.extend(moon_phase_value) 
    new_data.append(discharge_value)
    new_data.extend(drift_location_value)
    new_data.extend(nets_value)
   
    
    new_data = np.array(new_data)
    new_data = new_data.reshape(1,-1)
    # predict the temperature of the new data point
    result = model.predict(new_data)
    
    # display fish count in result label
    result_label.config(text=f"Fish Count: {result[0]:.2f}")
    
# create predict button
predict_button = tk.Button(root, text="Predict", command=predict_fish_count)
predict_button.grid(row=5, column=0, columnspan=2)

# Add a label widget to display the prediction
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

# create result label
result = tk.Label(root, text="")
result.grid(row=6, column=0, columnspan=2)



# run the GUI
root.mainloop()
