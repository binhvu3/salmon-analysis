setwd("C:\\Users\\rjli\\Documents\\Grad School\\MGT 6203 - Data Analytics in Business\\Team-55\\data")

library(tidyverse)
library(dplyr)
library(ggplot2)
library(corrplot)
library(stats)
library(pROC)
library(caret)

# fish <- read.csv("fish_data.csv", header = TRUE)
# fish_water <- read.csv("fish_data_water_temp.csv", header = TRUE)
# 
# ggplot(data = fish, mapping = aes(x = year, y = fish_count)) +
#   geom_boxplot()
# 
# M = cor(fish_water[,-1])
# corrplot(M, method='number')
# 
# plot(fish$year, fish$fish_count)
# plot(fish$precipitation, fish$fish_count)
# plot(fish_water$water_temp, fish_water$fish_count)
# plot(fish$air_temp, fish$fish_count)
# plot(fish$discharge, fish$fish_count)
# plot(fish$luna, fish$fish_count)
# 
# 
# p_lm <- lm(fish_count~precipitation, data=fish)
# p_res <- resid(p_lm)
# plot(fitted(p_lm), p_res)
# abline(0,0)
# qqnorm(p_res)
# qqline(p_res)
# 
# plot(density(p_res))

# fish_master <- read.csv('fish_master.csv', header=TRUE)

# kmeans of all data
# kmeans_fish <- kmeans(fish_water[,3:ncol(fish_water)], centers=2)
# summary(kmeans_fish)

# perform PCA to reduce to 2 dimensions for visualization
# scaled_fish <- scale(fish_water[,3:ncol(fish_water)])
# pca_fish <- prcomp(scaled_fish)
# 
# pca_fish$sdev^2 / sum(pca_fish$sdev^2)
# ggplot(data = data.frame(pca_fish$x[,1:2]), aes(x = PC1, y = PC2)) +
#   geom_point() +
#   labs(title = "PCA of fish dataset")
# 
# pc1 <- pca_fish$x[,1]
# pc2 <- pca_fish$x[,2]
# pca_data <- data.frame(pc1, pc2)

# kmeans on with 4 centers
# kmeans_pca <- kmeans(pca_data, centers=6)
# ggplot(data = pca_data, aes(x = pc1, y = pc2, color = factor(kmeans_pca$cluster))) +
#   geom_point() +
#   labs(title = "Clustering on PCA of fish data", color = "Cluster")
# 
# 
# # elbow plot to find optimal center
# wcss <- vector()
# 
# # Loop over k from 1 to 10 and calculate the WCSS
# for (i in 1:10) {
#   kmeans_model <- kmeans(scaled_fish, centers = i)
#   wcss[i] <- kmeans_model$tot.withinss
#   ggplot(data = pca_data, aes(x = pc1, y = pc2, color = factor(kmeans_model$cluster))) +
#     geom_point() +
#     labs(title = "Clustering on PCA of fish data with centers")
# }

# elbow_plot <- ggplot(data.frame(wcss), aes(x = 1:length(wcss), y = wcss)) +
#   geom_line() +
#   geom_point(size = 3) +
#   labs(title = "Elbow plot of fish dataset", x = "Number of centers (k)", y = "Within-cluster sum of squares (WCSS)")
# elbow_plot
# 
# elbow_point <- elbow_plot + annotate("point", x = 3, y = wcss[3], size = 5, color = "red")
# elbow_point

## Final cleaned data ###################################################################################################
fmf2 <- read.csv("fish_master_fixed2.csv", header = TRUE)
fmf2 <- filter(fmf2, year_x>=2014)
fish_master <- select(fmf2, fish_count, precipitation, air_temp, water_temp, discharge, set_net, drift_net, moon_phase)
fm_logit <- fish_master
#dummy vars for moon phase
fish_master$newmoon <- ifelse(fish_master$moon_phase == "New Moon", 1, 0) 
fish_master$firstquarter <- ifelse(fish_master$moon_phase == "First Quarter", 1, 0)
fish_master$fullmoon <- ifelse(fish_master$moon_phase == "Full Moon", 1, 0)
fish_master$thirdquarter <- ifelse(fish_master$moon_phase == "Third Quarter", 1, 0)
fish_master <- select(fish_master, -moon_phase)
fish_master$water_temp <- as.numeric(fish_master$water_temp)

fish_master$air_temp[is.na(fish_master$air_temp)] <- mean(fish_master$air_temp, na.rm=TRUE)
fish_master$precipitation <- as.integer(fish_master$precipitation)

# scale and PCA
fm_scaled <- scale(fish_master)
# fm_pca <- prcomp(fm_scaled)

# shows how much each PC contributions to explaining the variance of the data
# fm_pca$sdev^2 / sum(fm_pca$sdev^2)
# ggplot(data = data.frame(fm_pca$x[,1:2]), aes(x = PC1, y = PC2)) +
#   geom_point() +
#   labs(title = "PCA of fish dataset")


# pc1 <- fm_pca$x[,1]
# pc2 <- fm_pca$x[,2]
# fm_pca1 <- data.frame(pc1, pc2)
# 
# initial_centers <- data.frame( c(0, 0, 0), c(-1.5, 0.5, 1.5))
# 
# fm_pca_kmeans <- kmeans(fm_pca1, centers = initial_centers)
# ggplot(data = fm_pca1, aes(x = pc1, y = pc2, color = factor(fm_pca_kmeans$cluster))) +
#   geom_point() +
#   labs(title = "Clustering on PCA of fish data", color = "Cluster")

# visualize the contributions to the first PC. Confirms this is mostly drift_net and set_net (95%)
# library(factoextra)
# fviz_contrib(fm_pca, choice = "var", axes = 1)



# kmeans with all data, not PCA
set.seed(999)
wcss <- vector()

# Loop over k from 1 to 10 and calculate the WCSS for PCA
for (i in 1:20) {
  kmeans_model <- kmeans(fm_scaled, centers = i)
  wcss[i] <- kmeans_model$tot.withinss
  # ggplot(data = fm_scaled, aes(x = pc1, y = pc2, color = factor(kmeans_model$cluster))) +
  #   geom_point() +
  #   labs(title = "Clustering on PCA of fish data with centers")
}

elbow_plot <- ggplot(data.frame(wcss), aes(x = 1:length(wcss), y = wcss)) +
  geom_line() +
  geom_point(size = 3) +
  labs(title = "Elbow plot of fish dataset", x = "Number of centers (k)", y = "Within-cluster sum of squares (WCSS)")
elbow_plot

# 5 clusters look good
fm_kmeans <- kmeans(fm_scaled, centers=5)

# get cluster assignment 
fish_master$cluster <- fm_kmeans$cluster

summary_stats <- aggregate(fish_master, by = list(cluster = fish_master$cluster), FUN = mean)
summary_stats

###################### logistic regression, ROC, AUC
fm_logit <- select(fish_master, -cluster)
fm_logit$moon_phase <- factor(fm_logit$moon_phase)
fm_logit$precipitation <- as.integer(fm_logit$precipitation)
fm_logit$water_temp <- as.numeric(fm_logit$water_temp)
fcount_mean <- mean(fm_logit$fish_count)

fm_logit$high_fish <- factor(ifelse(fish_master$fish_count > fcount_mean, 1, 0)) 
fish_logit <- glm(high_fish~precipitation+air_temp+water_temp+discharge+set_net+drift_net+moon_phase, data=fm_logit, family="binomial")
summary(fish_logit)
temp <- fm_logit %>%
  filter(drift_net == 1)
temp2 <- fm_logit %>%
  filter(high_fish == 1)
mean_temp_high_fish <- mean(temp2$water_temp)
mean_temp <- mean(fm_logit$water_temp)
probs <- predict(fish_logit, newdata = select(fm_logit, -high_fish, -fish_count), type = "response")
fm_logit$probs <- probs
fm_logit$prediction <- factor(ifelse(probs>=0.8, 1, 0))
roc <- roc(fm_logit$high_fish, fm_logit$probs)
auc <- auc(roc)
plot(roc, main = paste0("ROC Curve (AUC = ", round(auc,3), ")"))

confusionMatrix(fm_logit$prediction, fm_logit$high_fish, positive='1')


### correlation plot with final dataset
fish_cor <- select(fmf2, fish_count, precipitation, air_temp, stage, discharge, water_temp, moon_phase, set_net, drift_net)
fish_cor$newmoon <- ifelse(fish_cor$moon_phase == "New Moon", 1, 0) 
fish_cor$firstquarter <- ifelse(fish_cor$moon_phase == "First Quarter", 1, 0)
fish_cor$fullmoon <- ifelse(fish_cor$moon_phase == "Full Moon", 1, 0)
fish_cor$thirdquarter <- ifelse(fish_cor$moon_phase == "Third Quarter", 1, 0)
fish_cor <- select(fish_cor, -moon_phase)
fish_cor$precipitation <- as.integer(fish_cor$precipitation)
fish_cor$water_temp <- as.numeric(fish_cor$water_temp)
fish_cor$air_temp[is.na(fish_cor$air_temp)] <- mean(fish_cor$air_temp, na.rm=TRUE)
fish_cor$stage[is.na(fish_cor$stage)] <- mean(fish_cor$stage, na.rm=TRUE)
M = cor(fish_cor[,-1])
corrplot(M, method='number')
