#clear
rm(list = ls())

#libraries 
library(dplyr)
library(MASS)
library(tidyverse)

#set directory #######################################################################################################
setwd('C:/Users/blackbuh/MyPythonScripts') 
 
#read in data #######################################################################################################
fish_data <- read.csv('fish_master_final.csv', stringsAsFactors = TRUE)

#cleanse/manipulate #######################################################################################################
fish_data$date <- as.Date(fish_data$date, format = '%m/%d/%Y')
fish_data <-  dplyr::select(fish_data, date, fish_count, precipitation, air_temp, stage, discharge, water_temp, moon_phase,set_location, drift_location, nets)
fish_data$nets <- relevel(fish_data$nets, ref = "no_nets")
fish_data$drift_location <- relevel(fish_data$drift_location, ref = "None")
fish_data$set_location <- relevel(fish_data$set_location, ref = "None")

#lag nets #######################################################################################################
fish_data$drift_lag <- dplyr::lag(fish_data$drift_location, n=3, default = 'None')
fish_data$set_lag <- dplyr::lag(fish_data$set_location, n=3, default = 'None')
fish_data$netsout_lag <- dplyr::lag(fish_data$nets, n=3, default = 'no_nets')

#lag testing #######################################################################################################
fish_data_lag <- lm(fish_count ~ precipitation + air_temp + log(discharge) + water_temp + moon_phase +
                      drift_lag + set_lag + netsout_lag
                    , data = fish_data)
summary(fish_data_lag)

#LR model testing #######################################################################################################
fish_model_all <- lm(fish_count ~ precipitation + air_temp + log(discharge) + log(water_temp) + moon_phase 
                     + set_location + drift_location + nets
                     , data = fish_data)
summary(fish_model_all)

#stepwise testing###### This is model where we draw our conclusions/insights from ######################################
step.model <- stepAIC(fish_model_all, direction = "both", 
                      trace = FALSE)
summary(step.model)

#lag model
step.model <- stepAIC(fish_data_lag, direction = "both", 
                      trace = FALSE)
summary(step.model)


