## Student Performance Data Cleaning

# Overview

This project focuses on cleaning a student performance dataset using Python and Pandas. It was created as a practice project to understand real-world data preprocessing techniques such as handling missing values, cleaning categorical and numerical data, and exporting a cleaned dataset.

# Objectives
Load a CSV dataset using Pandas.
Identify missing values.
Clean both numerical and categorical columns.
Apply appropriate techniques for handling missing data.
Save the cleaned dataset for further analysis.

# Technologies Used
Python
Pandas
NumPy
Visual Studio Code

# Project Structure

studentperformance_dataset/
│── data_cleaning.py
│── uncleaned_data.csv
│── cleaned_student_performance_updated_1000.csv
│── README.md

# Dataset Description

The dataset contains information about students and their academic performance. 
It includes:
- demographic details
- study habits
- attendance
- extracurricular participation
- parental support
- and grades


# Columns Included

 Column Name - Description 
 StudentID - Unique identifier for each student 
 Name - Student's name 
 Gender - Gender of the student 
 AttendanceRate - Student's attendance rate 
 StudyHoursPerWeek - Weekly study hours 
 PreviousGrade - Previous academic grade/score 
 ExtracurricularActivities - Participation in extracurricular activities 
 ParentalSupport - Level of parental support 
 FinalGrade - Student's final grade 
 Study Hours - Total study hours 
 Attendance (%) - Attendance percentage 
 Online Classes Taken - Number of online classes attended 


# Data Cleaning Performed

The following preprocessing steps were applied:

* Checked missing values in every column.
* Filled missing Name values with "Unknown".
* Filled missing Gender values with "Unknown".
* Used Linear Interpolation for missing Student IDs.
Filled numerical columns using the Median, including:
 -Attendance Rate
 -Study Hours Per Week
 -Previous Grade
 -Final Grade
 -Study Hours
 -Attendance (%)
 -Filled categorical columns using the Mode, including:
 -Extracurricular Activities
 -Parental Support
 -Online Classes Taken
 -Exported the cleaned dataset into a new CSV file.

# Skills Practiced

-> Data Cleaning
-> Missing Value Treatment
-> Median Imputation
-> Mode Imputation
-> Linear Interpolation
-> CSV File Handling
-> Data Preprocessing using Pandas

# How to Run

- Clone this repository.
- Install the required libraries.
- Run the Python script.
- The cleaned dataset will be generated automatically.


# Output

-> Cleaned student performance dataset
-> Missing values handled appropriately
-> New CSV file generated for further analysis

# Future Improvements
- Perform Exploratory Data Analysis (EDA).
- Create visualizations using Matplotlib.
- Detect and handle outliers.
- Build a machine learning model for student performance prediction.


# Author

Zeel Chauhan

Practice Project – Python Data Cleaning with Pandas and NumPy


