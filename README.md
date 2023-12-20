# 🐟 Improved prediction of salmon runs using historical salmon and weather data to enhance business planning and resource allocation
 Team 55's group project GitHub repository for MGT 6203 (Canvas) Spring of 2023 semester.
 
 ## Quick Link
 [🖥️ VIDEO PRESENTATION ](https://www.youtube.com/watch?v=AAObhweJ6dE)
 
 [:bookmark_tabs: POWERPOINT PRESENTATION](https://github.com/binhvu3/Salmon-Analysis/blob/main/Final%20Presentation%20Slides/Project%20Report%20Video%20Presentation.pdf)
 
  [ 📄 WRITTEN REPORT]( https://github.com/binhvu3/Salmon-Analysis/blob/main/Final%20Report/Salmon%20Prediction%20Final%20Project%20Team%2055.pdf)

## 👓 Background/Goal
Our goal is to see if we can create an accurate prediction model using historical fish count data and weather data from the Kenai River. 
Creating such a tool – or better understanding of the factors that influence salmon runs would be hugely beneficial for the community, their economy, and those who depend on the salmon for financial or other reasons. 


## Repository Structure
Description of relevant folders

## Code Structure
    .
    ├── Code                         # All of the intermediate R code files and python scripts used to clean data
    │   ├── LM_fish_gui.py                          
    │   ├── bv_regression_models.ipynb               
    │   ├── clean_data.py  
    │   ├── clean_nets_data.py 
    │   ├── final_regression_analysis.R 
    │   ├── liner_regression_analysis.r
    │   ├── more_data_clean.ipynb 
    │   ├── peak_fish_count_analysis.r
    │   ├── placeholder.txt 
    │   └── rl_eda_kmeans_logit.R            
    │
    ├── Data                          # All data that was used for the project. The final complete dataset is fish_master_final.csv
    │   ├── Kenai_AP_combined.csv     
    │   ├── Kenai_Late_run_Sockeye_Fish_Counts.xls      
    │   └── ...
    │   
    ├── Final Code                     # Contains the final, clean code files used for our analysis. Each file helps generates visuals used in the final report and explanations of code and analyses is also in the final report
    │   ├── LM_fish_gui.py       
    │   ├── advanced_regression_models.ipynb
    │   ├── final_peak_analysis.r
    │   ├── final_regression_analysis.R
    │   ├── more_data_clean.ipynb
    │   ├── placeholder.txt
    │   └── rl_eda_kmeans_logit.R
    │
    ├── Final Presentation Slides      # Final slides for our video    
    │   └── Project Report Video Presentation.pdf 
    │
    ├── Final Report                
    │   └── Salmon Prediction Final Project Team 55.pdf
    │
    ├── Other Resources               
    │
    ├── Progress Report               
    │   └── Salmon Prediction Project Report.docx
    │
    ├── Project Proposal                          # All data that was used for the project. The final complete dataset is fish_master_final.csv
    │   ├── Team 55 - Proposal DRAFT.docx          
    │   └── Team 55 Proposal.pdf
    │   
    ├── Proposal Presentation               
    │   └── Final Project Proposal Video Presentation.pptx
    │
    ├── Visualizations            
    │   ├── bv_dataset_visualization.ipynb       
    │   ├── corrplot2.png
    │   ├── drift_location.png
    │   ├── fish-boxplot.png
    │   ├── fish_count_peaks.png
    │   └── outcome_distr.png
    │
    ├── requirements_python.txt                   # Contains the python and R packages used in this project
    │
    ├── requirements_r.txt
    └── ...

 # 📔 Opening Jupyter Notebook
 In order to run Jupyter Notebook that is found in this Repo, please install Jupyter Notebook with R kernel. (Steps are below)

## 🔨 Installation of Jupyter Notebook
You can find the installation documentation for the [Jupyter platform, on ReadTheDocs](https://jupyter.readthedocs.io/en/latest/install.html). 

## 🔨 Install R kernel for Jupyter Notebook
[More Info](https://stackoverflow.com/questions/57870575/install-and-run-r-kernel-for-jupyter-notebook)

Open any R session (e.g. in RStudio is fine, or open terminal/bash and type R to start an R session). 

Install the kernel with:

```bash
install.packages("devtools")
devtools::install_github("IRkernel/IRkernel")
IRkernel::installspec()

```

## 📟 Run Jupyter Notebook with R kernel
Launch with:

```bash
jupyter notebook
```
Once Jupyter Notebook Instance is running, navigate to the Jupyter Notebook and open the file.

You need to confirm that R kernel is running. If not, check the top menu 

```bash
Top Menu > Kernel > Change kernel > R 
```
# 📟 GUI Application using Python
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
