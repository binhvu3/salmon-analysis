#clear
rm(list = ls())

#libraries
library(dplyr)
library(MASS)
#set directory
setwd('C:/Users/blackbuh/MyPythonScripts') 

#read in data
fish_data <- read.csv('fish_master_final.csv', stringsAsFactors = TRUE)
fish_data$date <- as.Date(fish_data$date, format = '%m/%d/%Y')
fish_data <-  dplyr::select(fish_data, date, fish_count, precipitation, air_temp, stage, discharge, water_temp, moon_phase,set_location, drift_location, nets)
fish_data$nets <- relevel(fish_data$nets, ref = "no_nets")
fish_data$drift_location <- relevel(fish_data$drift_location, ref = "None")
fish_data$set_location <- relevel(fish_data$set_location, ref = "None")

#all years - precipitation and water temp -- R^2 of .18
fish_model <- lm(fish_count ~moon_phase + set_location + drift_location 
                 + log(discharge) + air_temp, data = fish_data)
summary(fish_model)

#filtered to just the years with water temp and precipitation R^2 of .35
fish_model_all <- lm(fish_count ~ precipitation + air_temp + log(discharge) + water_temp + moon_phase 
                     + set_location + drift_location + nets
                     , data = fish_data)
summary(fish_model_all)

step.model <- stepAIC(fish_model_all, direction = "both", 
                      trace = FALSE)
summary(step.model)



str(fish_data_filtered)

#remove insignificant factors


str(fish_data)

#just on location -- R^2 of .15
fish_count_location <- lm(fish_count ~ set_location + drift_location, data = fish_data_filtered)
summary(fish_count_location)

#for testing
fish_count_single <- lm(fish_count ~ moon_phase, data = fish_data)
summary(fish_count_single)





typeof(fish_data$date)
fish_data
levels(fish_data$nets)
fish_model2 <- lm(fish_count ~ nets_lag, data = fish_data)
summary(fish_model2)

fish_data$year <- format(fish_data$date, "%Y")
str(fish_data)

fish_sub <- select(fish_data, fish_count, date, year)
# Group the data by year and find the maximum count for each year
peak_counts <- fish_sub %>%
  group_by(year) %>%
  summarise(peak_count = max(fish_count))

# Print the results
print(peak_counts)                