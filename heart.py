import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Data Loading and Preprocessing

# Load the dataset
url = 'https://drive.google.com/uc?id=1YedPjaNtYAs_hoaC4aIc_j3BwtvIL0UR'
heart_data = pd.read_csv(url)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(heart_data.head())

# Check for missing values
missing_values = heart_data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Handle missing values if any (example: filling with mean or dropping)
heart_data.fillna(heart_data.mean(), inplace=True)  # Assuming numerical columns

# Verify if missing values are handled
missing_values_after = heart_data.isnull().sum()
print("\nMissing values after handling:")
print(missing_values_after)

# Convert categorical variables to dummy/indicator variables
heart_data = pd.get_dummies(heart_data, drop_first=True)

# Display the first few rows of the dataset after encoding
print("\nDataset after converting categorical variables to dummy variables:")
print(heart_data.head())

# Step 2: Data Analysis

# Calculate the average age of patients with and without heart disease
avg_age_with_disease = heart_data[heart_data['target'] == 1]['age'].mean()
avg_age_without_disease = heart_data[heart_data['target'] == 0]['age'].mean()

print(f"\nAverage age of patients with heart disease: {avg_age_with_disease}")
print(f"Average age of patients without heart disease: {avg_age_without_disease}")

# Distribution of chest pain types
cp_distribution = heart_data['cp'].value_counts()
print("\nDistribution of chest pain types:")
print(cp_distribution)

# Correlation between thalach (maximum heart rate) and age
correlation_thalach_age = heart_data['thalach'].corr(heart_data['age'])
print(f"\nCorrelation between thalach (maximum heart rate) and age: {correlation_thalach_age}")

# Effect of sex on the presence of heart disease
effect_of_sex = heart_data.groupby('sex')['target'].mean()
print("\nEffect of sex on the presence of heart disease:")
print(effect_of_sex)

# Step 3: Data Visualization

# Histogram of age distribution
plt.hist(heart_data['age'], bins=10, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Patients')
plt.show()

# Bar chart of chest pain types distribution
cp_distribution.plot(kind='bar')
plt.xlabel('Chest Pain Type')
plt.ylabel('Frequency')
plt.title('Distribution of Chest Pain Types Among Patients')
plt.show()

# Scatter plot of thalach vs. age
plt.scatter(heart_data['age'], heart_data['thalach'], alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Thalach (Maximum Heart Rate)')
plt.title('Relationship between Age and Thalach (Maximum Heart Rate)')
plt.show()

# Box plot of age distribution by heart disease presence
heart_data.boxplot(column='age', by='target', grid=False)
plt.xlabel('Heart Disease')
plt.ylabel('Age')
plt.title('Age Distribution of Patients with and without Heart Disease')
plt.suptitle('')
plt.show()

# Step 4: Advanced Analysis (using numpy)

# Correlation matrix
correlation_matrix = heart_data.corr()
print("\nCorrelation matrix:")
print(correlation_matrix)

# Rolling mean analysis on cholesterol levels
chol_rolling_mean = heart_data['chol'].rolling(window=5).mean()

# Plot rolling mean of cholesterol levels
plt.plot(heart_data['chol'], label='Cholesterol')
plt.plot(chol_rolling_mean, label='Rolling Mean (window=5)', color='orange')
plt.xlabel('Index')
plt.ylabel('Cholesterol Level')
plt.title('Rolling Mean of Cholesterol Levels')
plt.legend()
plt.show()

# Bonus

# Function to predict heart disease based on simple thresholding rules
def predict_heart_disease(age, sex, cp, thalach, chol):
    # Example of simple thresholding rules
    if age > 50 and chol > 200 and thalach < 150 and sex == 1:
        return 1
    else:
        return 0

# Test the function
print("\nPrediction test case result (age=55, sex=1, cp=3, thalach=145, chol=210):")
print(predict_heart_disease(55, 1, 3, 145, 210))  # Example test case

# Use subplots to combine multiple visualizations into one figure
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Histogram of age distribution
axs[0, 0].hist(heart_data['age'], bins=10, edgecolor='black')
axs[0, 0].set_title('Age Distribution')

# Bar chart of chest pain types distribution
cp_distribution.plot(kind='bar', ax=axs[0, 1])
axs[0, 1].set_title('Chest Pain Types Distribution')

# Scatter plot of thalach vs. age
axs[1, 0].scatter(heart_data['age'], heart_data['thalach'], alpha=0.5)
axs[1, 0].set_title('Age vs. Thalach')

# Box plot of age distribution by heart disease presence
heart_data.boxplot(column='age', by='target', grid=False, ax=axs[1, 1])
axs[1, 1].set_title('Age Distribution by Heart Disease')
plt.suptitle('')
plt.show()
