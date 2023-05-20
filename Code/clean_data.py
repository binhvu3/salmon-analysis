import pandas as pd
import os
from datetime import datetime


current_dir = os.path.dirname(os.getcwd())
# current directory should be ../Team-55

airtemp = os.path.join(current_dir, 'data', 'Kenai_AP_combined.csv') 
fishcount = os.path.join(current_dir, 'data', 'Kenai_Late_run_Sockeye_Fish_Counts.xls') # tab separated
waterlevel = os.path.join(current_dir, 'data', 'Water_Level_Kenai_river_at_Kenai_Keys.csv')

airtemp_df = pd.read_csv(airtemp)
fishcount_df = pd.read_csv(fishcount, sep='\t')
waterlevel_df = pd.read_csv(waterlevel)

# format date into yyyy-mm-dd format
fishcount_df['count_date'] = fishcount_df['count_date'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y').strftime('%Y-%m-%d'))
waterlevel_df['Date (UTC)'] = waterlevel_df['Date (UTC)'].apply(lambda x: x.split(' ')[0])

# join data
all_data = pd.merge(fishcount_df, airtemp_df, how = "left", left_on = 'count_date', right_on = 'Date')
all_data = pd.merge(all_data, waterlevel_df, how = 'left', left_on = 'count_date', right_on = 'Date (UTC)')

# drop unnecessary columns and reorganize columns
all_data.drop(['Date (UTC)', 'count_date', 'Snowfall (in)', 'Snow Depth (in)'], axis = 1, inplace = True)
all_data = all_data.reindex(['Date', 'year', 'fish_count', 'Species', 'Species_ID', 'count_location',
       'count_location_ID', 'Maximum Temperature (degF)',
       'Precipitation (in)', 'Mean Temperature (degF)', 'Cooling Degree Days',
       'Minimum Temperature (degF)', 'Heating Degree Days',
       'Growing Degree Days', 'Type Source', 'Stage'], axis = 1)

waterdata = os.path.join(current_dir, 'data', 'water_data.csv')
lunarphases = os.path.join(current_dir, 'data', 'lunar_phases.csv')

waterdata_df = pd.read_csv(waterdata, sep = '\t')
waterdata_df = waterdata_df.iloc[1:]
waterdata_df.rename(columns = {'698_00060_00003':'discharge (ft3/s)', '701_00010_00001':'water temp max (F)', '702_00010_00002':'water temp min (F)', '703_00010_00003':'water temp mean (F)'}, inplace=True)

# convert to fahrenheit
waterdata_df['water temp max (F)'] = waterdata_df['water temp max (F)'].apply(lambda x: float(x) * (9/5) + 32 if isinstance(float(x), (float)) else x)
waterdata_df['water temp min (F)'] = waterdata_df['water temp min (F)'].apply(lambda x: float(x) * (9/5) + 32 if isinstance(float(x), (float)) else x)
waterdata_df['water temp mean (F)'] = waterdata_df['water temp mean (F)'].apply(lambda x: float(x) * (9/5) + 32 if isinstance(float(x), (float)) else x)

waterdata_df.drop(['698_00060_00003_cd', '699_80154_00003', '699_80154_00003_cd', '700_80155_00003', '700_80155_00003_cd', '701_00010_00001_cd', '702_00010_00002_cd', '703_00010_00003_cd'], axis=1, inplace=True)
all_data = pd.merge(all_data, waterdata_df, how='left', left_on='Date', right_on='datetime')
all_data.drop(['datetime'], axis=1, inplace=True)

lunarphases_df = pd.read_csv(lunarphases)
lunarphases_df['Date'] = pd.to_datetime(lunarphases_df[['year', 'month', 'day']].astype(str).agg('-'.join, axis=1)).dt.date
lunarphases_df['Date'] = lunarphases_df['Date'].astype(str)
lunarphases_df.drop(['year', 'month', 'day'], axis=1, inplace=True)
all_data = pd.merge(all_data, lunarphases_df, how='left', on = 'Date')


all_data.drop(['Species', 'Species_ID', 'count_location', 'count_location_ID', 'Maximum Temperature (degF)', \
               'Cooling Degree Days', 'Minimum Temperature (degF)', 'Heating Degree Days', 'Growing Degree Days', \
               'Type Source', 'agency_cd', 'site_no', 'water temp max (F)', 'water temp min (F)'], axis = 1, inplace=True)

all_data['discharge (ft3/s)'] = all_data['discharge (ft3/s)'].astype(int)

all_data.rename({"Date":"date", "Precipitation (in)":"precipitation", "Mean Temperature (degF)":"air_temp", \
                 "Stage":"stage", "discharge (ft3/s)":"discharge", "water temp mean (F)":"water_temp"}, axis = 1, inplace=True)

exclude_na_water = all_data[all_data['water_temp'].notna()].interpolate()

# interpolate missing values. Data not exported (just for exploration)
temp = all_data.interpolate()
temp = pd.concat([temp, all_data], axis = 1)
# export cleaned file to Team-55/Data folder
all_data.to_csv(os.path.join(current_dir, 'data', 'fish_data.csv'), index=False)

exclude_na_water.to_csv(os.path.join(current_dir, 'data', 'fish_data_water_temp.csv'), index=False)