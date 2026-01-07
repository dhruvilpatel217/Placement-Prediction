import pandas as pd 
import os

file_path = os.path.join("data", "placement_data.csv")
output_path = os.path.join("data", "cleaned_placement_data.csv")
print(file_path)

#Read csv file
df=pd.read_csv(file_path)
print("Data Loaded Successfully!")

#Printing first five rows of the dataset
print(df.head())
print(df.shape)

#Checking missing values
print(df.isnull().sum())

#Checking data types
print(df.info())

#Now converting the object based columns into the numerical values so Ml model can work on it
# mapping yes-->1 and no-->0
df['Placement'] = df['Placement'].map({'Yes': 1, 'No': 0})
df['Internship_Experience'] = df['Internship_Experience'].map({'Yes': 1, 'No': 0})
print(df.info())
print(df.head())

#Dropping column of the college id as it does not help in making prediction of the placement.
df = df.drop(columns=['College_ID'])
print(df.head())

#Saving the cleaned file
df.to_csv(output_path, index=False)
print(f"\n Success! Cleaned data saved to: {output_path}")
df=pd.read_csv(output_path)
print(df.head())

