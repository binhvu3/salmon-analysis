#clear
rm(list = ls())

#libraries

library(ggplot2)

library(lubridate)
library(dplyr)
#set directory
setwd('C:/Users/blackbuh/MyPythonScripts') 

#read in data
fish_data <- read.csv('fish_master_fixed.csv')

fish_data$date <- as.Date(fish_data$date, format = "%m/%d/%Y")

fish_data <- fish_data %>% 
  group_by(year = lubridate::year(date)) %>% 
  mutate(cusum = cumsum(fish_count))



fish_data <- fish_data %>% 
  mutate(day_of_year = yday(date))

# Define distinct colors for each year
# create a custom color palette for each year
year_colors <- rainbow(length(unique(fish_data$year)))

# Convert year to factor
fish_data$year <- as.factor(fish_data$year)

# Plot using ggplot2
ggplot(fish_data, aes(x = day_of_year, y = cusum, color = year)) +
  geom_line() +
  scale_color_manual(values = year_colors) +
  labs(title = "Cumulative Sum of Fish Count by Day of the Year",
       x = "Day of Year",
       y = "Cumulative Sum of Fish Count")

# Calculate the weekly fish count per year
fish_count_per_week <- aggregate(fish_data$fish_count, 
                                 list(year = fish_data$year, 
                                      week = cut(fish_data$date, "week")), 
                                 sum)

# Create a stacked bar plot
ggplot(fish_count_per_week, aes(x = week, y = x, fill = year)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = year_colors) +
  labs(title = "Fish Count by Week per Year",
       x = "Week",
       y = "Fish Count")
#####################################################################
# Plot fish count by day of the year
ggplot(fish_data, aes(x = day_of_year, y = fish_count, color = year)) +
  geom_line() +
  scale_color_manual(values = year_colors) +
  labs(title = "Fish Count by Day of the Year",
       x = "Day of Year",
       y = "Fish Count") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))  # Rotate x-axis labels

# Save the plot with a larger size
ggsave("fish_count.png", width = 20, height = 10)

########################################################################

# calculate peaks for each year
peaks <- fish_data %>%
  group_by(year) %>%
  slice_max(fish_count, n = 1) %>%
  ungroup()



# Plot using ggplot2
ggplot(fish_data, aes(x = day_of_year, y = fish_count, color = year)) +
  geom_line() +
  scale_color_manual(values = year_colors) +
  labs(title = "Fish Count by Day of the Year",
       x = "Day of Year",
       y = "Fish Count") +
  geom_vline(data = peaks, aes(xintercept = day_of_year, color = year), linetype = "dashed", size = 1) +
  geom_text(data = peaks, aes(x = day_of_year, y = fish_count, label = year), hjust = -0.2, color = "black", size = 3)

###########################################################################


# Compute the cumulative sum of fish count by day of the year
fish_data$cusum <- ave(fish_data$fish_count, fish_data$year, FUN = cumsum)

# Identify the peak for each year
peaks <- subset(fish_data, ave(fish_count, year, FUN = max) == fish_count)

# Plot using ggplot2
ggplot(fish_data, aes(x = day_of_year, y = fish_count, color = year)) +
  geom_line() +
  scale_color_manual(values = year_colors) +
  labs(title = "Fish Count by Day of the Year",
       x = "Day of Year",
       y = "Fish Count") +
  scale_x_continuous(breaks = seq(0, 365, by = 10)) +
  geom_vline(data = peaks, aes(xintercept = day_of_year, color = year), linetype = "dashed", size = 1) +
  geom_label(data = peaks, aes(x = day_of_year, y = fish_count, label = year, color = year), nudge_y = 50)

#############################################################################

