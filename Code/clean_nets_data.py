# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:59:29 2023

@author: blackbuh
"""

import os
import pandas as pd

folder_path = 'C:\\Users\\blackbuh\MyPythonScripts\\fishing_nets'

df_list = []

# loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):  # assuming all files are CSV files
        file_path = os.path.join(folder_path, filename)
        # read CSV file into a dataframe and append to list
        if (file := int(filename.split('.')[0]) < 2013):
                  df = pd.read_csv(file_path, header=3, skip_blank_lines=True)
                  # extract year from filename (assuming filename format is "year.csv")
                  year = int(filename.split('.')[0])
                  # add year column to dataframe
                  df['year'] = year
                  df_list.append(df)
        else: 
            df = pd.read_csv(file_path, header=2, skip_blank_lines=True)
            # extract year from filename (assuming filename format is "year.csv")
            year = int(filename.split('.')[0])
            # add year column to dataframe
            df['year'] = year
            df_list.append(df)
# concatenate all dataframes in the list into one big dataframe
big_df = pd.concat(df_list, ignore_index=True)



#big_df.to_excel('C:\\Users\\blackbuh\MyPythonScripts\\fish_test.xlsx')

locations = pd.unique(big_df[['Set Gill Net', 'Drift Gill Net']].values.ravel('K'))

kenai_affected_set = ['All',
'Kasilof Section',
'Kenai/Kasilof',
'Western s. of Redoubt Pt & Upper Subdistrict',
'Upper Subdistrict',
'Kasilof Section within 1/2 mile of shore',
'All West-side & Kasilof Section to 1/2 mile',
'Kasilof 1/2 mile and W. Subdistrict S. of Redoubt Pt.',
'Kasilof 1/2 mile, Kustatan, Kalgin, Western, Chinitna Bay',
'Kasilof Section & Western Subdistrict S. of Redoubt Pt.',
'Kasilof Section  ',
'All  ',
'Kenai, Kasilof & East Forelands Sections',
'Kasilof Section withing 1/2 mile of shore',
'Kenai, Kasilof, E. Forelands, and W. Sub. S. of R. Pt',
'Kasilof River Special Harvest Area',
'Kasilof Section ',
'Kenai, Kasilof, & East Forelands Sections',
'All except N. District',
'Kasilof Section 1/2 mile',
'Kenai, Kasilof, and E. Forelands',
'All ',
'Kenai and E. Forelands',
'Kasilof Section within 600 feet',
'Kasilof Section within 1/2 mile of mean high tide mark',
'All, except W. Sub. south of Redoubt Pt. ',
'Kenai & East Foreland sections',
'All, except Kasilof Section',
'Kenai, Kasilof, & E. Foreland Sections',
'All except Portion of Gen. Sub.',
'Kasilof Section within one-half mile',
'All except Kenai Section of U. Subdistrict',
'Kasilof Section within 600ft',
'All except Salamatof Section of U. Subdistrict',
'Kenai & Kasilof Section within one-half mile and N. K. Beach 600ft',
'Kasilof Section one-half mile and N. K Beach 600ft',
'Kasilof Special Harvest Area (KRSHA)',
'Kasilof, Kenai, & E. Foreland Sections',
'1/2 mile Kasilof Section & NKB 600ft',
'Kasilof 600ft & NKB 600ft',
'Kasilof Section - NKB 600ft',
'Kasilof 600ft',
'Upper Subdistrict 600ft',
'KRSHA'
]

big_df['set_net'] = big_df['Set Gill Net'].isin(kenai_affected_set).astype(int)
big_df['drift_net'] = (~((big_df['Drift Gill Net'].fillna('').str.contains('Chinitna')) | (big_df['Drift Gill Net'].isna()))).astype(int)

big_df.to_excel('C:\\Users\\blackbuh\MyPythonScripts\\fish_test.xlsx')
    
