import pandas as pd
import numpy as np

# df = pd.read_csv('D:\python\Project\empolyee_dataset\student_performance_updated_1000.csv')
data = pd.read_csv(r'D:\python\DataScience-ML\DA Project\studentperformance_dataset\uncleaned_data.csv')
# print(df)

df = pd.DataFrame(data)

# TO READ HIDDEN COLUMNS
# column = df[['PreviousGrade','ExtracurricularActivities','ParentalSupport','FinalGrade']]
# print(column)

# print('Missing values in each column:')
# print(df.isnull().sum())

df['StudentID'] = df['StudentID'].interpolate(method="linear")
df['Name'] = df['Name'].fillna('Unknown')
df['Gender'] = df['Gender'].fillna('Unknown')
# df['Gender'] = df['Gender'].fillna(df['Gender'].mode())
df['AttendanceRate'] = df['AttendanceRate'].fillna(df['AttendanceRate'].median())
df['StudyHoursPerWeek'] = df['StudyHoursPerWeek'].fillna(df['StudyHoursPerWeek'].median())
df['PreviousGrade'] = df['PreviousGrade'].fillna(df['PreviousGrade'].median())
df['ExtracurricularActivities'] = df['ExtracurricularActivities'].fillna(df['ExtracurricularActivities'].mode()[0])
df['FinalGrade'] = df['FinalGrade'].fillna(df['FinalGrade'].median())
df['ParentalSupport'] = df['ParentalSupport'].fillna(df['ParentalSupport'].mode()[0])
df['Study Hours'] = df['Study Hours'].fillna(df['Study Hours'].median())
df['Attendance (%)'] = df['Attendance (%)'].fillna(df['Attendance (%)'].median())
df['Online Classes Taken'] = df['Online Classes Taken'].fillna(df['Online Classes Taken'].mode()[0])

# print('After changes:')
print(df.isnull().sum())

df.to_csv('cleaned_student_performanance_updated_1000.csv', index=False)
print('Data cleaning completed')

