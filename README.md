# Improved prediction of salmon runs using historical salmon and weather data to enhance business planning and resource allocation
 Team 55's group project GitHub repository for MGT 6203 (Canvas) Spring of 2023 semester.
 
 ## Quick Link
 [:bar_chart: SEE VISUALIZATION HERE ](https://public.tableau.com/app/profile/binh.vu5742/viz/Visualization_16835996323470/MainDashboard)

## Repository Structure
Description of relevant folders
- **Code**: All of the intermediate R code files and python scripts used to clean data
- **Data**: All data that was used for the project. The final complete dataset is fish_master_final.csv
- **Final Code**: Contains the final, clean code files used for our analysis. Each file helps generates visuals used in the final report and explanations of code and analyses is also in the final report
  - Data cleaning: clean_data.py, clean_nets_data.py, more_data_clean.ipynb
  - Peak Analysis: final_peak_analysis.r
  - EDA, Logistic Regression, Kmeans clustering: rl_eda_kmeans_logit.R
  - Random Forest, Lasso, and Ridge Regression: advanced_regression_models.ipynb
  - Linear Regression: final_regression_analysis.R
  - Prediction tool GUI: LM_fish_gui.py
- **Final Presentation Slides**: Final slides for our video
- **Final Report**: The final report
- **Other Resources**: Not used
- **Progress Report**: The progress report
- **Project Proposal**: The project proposal report
- **Proposal Presentation**: Slides for our project proposal
- **Visualizations**: Key visualizations for our analysis
- requirements_python.txt & requirements_r.txt: Contains the python and R packages used in this project

 # Opening Jupyter Notebook
 In order to run Jupyter Notebook that is found in this Repo, please install Jupyter Notebook with R kernel. (Steps are below)

## Installation of Jupyter Notebook
You can find the installation documentation for the [Jupyter platform, on ReadTheDocs](https://jupyter.readthedocs.io/en/latest/install.html). 

## Install R kernel for Jupyter Notebook
[More Info](https://stackoverflow.com/questions/57870575/install-and-run-r-kernel-for-jupyter-notebook)

Open any R session (e.g. in RStudio is fine, or open terminal/bash and type R to start an R session). 

Install the kernel with:

```bash
install.packages("devtools")
devtools::install_github("IRkernel/IRkernel")
IRkernel::installspec()

```

## Run Jupyter Notebook with R kernel
Launch with:

```bash
jupyter notebook
```
Once Jupyter Notebook Instance is running, navigate to the Jupyter Notebook and open the file.

You need to confirm that R kernel is running. If not, check the top menu 

```bash
Top Menu > Kernel > Change kernel > R 
```
# GUI Application using Python
This project is a GUI application that utilizes the Tkinter library to create a user interface for data analysis. The application uses the pandas, numpy, and sklearn.linear_model libraries for data manipulation and linear regression analysis.

## Getting Started
Install the required python packages in requirements_python.txt.

To run the application, simply run the gui.py file using Python. You can do this by opening a terminal or command prompt in the project directory and running the following command:

```bash
LM_fish_GUI.py
```
This will launch the GUI application.

Features
The GUI application requires the user to download our data file "gui_test" CSV file and perform linear regression analysis prediction on the data. The user can select the dependent variables from the data, and the application will perform linear regression and display the results.

Usage
To use the application, follow these steps:

Download gui_test.csv
Edit script to your directory containing gui_test.csv
Launch the application by running the LM_fish_GUI.py file using Python.
Input the independent variables from the drop-down menus or text boxes.
Click the "Predict" button to perform linear regression analysis on the data.
The application will display the prediction results of the analysis.
