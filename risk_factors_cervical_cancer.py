import pandas as pd
import numpy as np  # Importing the numpy library
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
df = pd.read_csv('kag_risk_factors_cervical_cancer.csv')

# Replace non-numeric values ('?') with NaN
df.replace('?', np.nan, inplace=True)

# Convert all columns to numeric and replace NaN with the column mean
df = df.apply(pd.to_numeric, errors='coerce')
df.fillna(df.mean(), inplace=True)

# Check for missing values and general structure of the dataframe
df.info()

# Replace missing values for specific columns
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Number of sexual partners'] = df['Number of sexual partners'].fillna(df['Number of sexual partners'].mode()[0])

# Drop rows with missing values in the 'Biopsy' column
df.dropna(subset=['Biopsy'], inplace=True)

# Create a new column for smoking severity
df['Smokes (years)'] = pd.to_numeric(df['Smokes (years)'], errors='coerce')
df['Smokes (packs/year)'] = pd.to_numeric(df['Smokes (packs/year)'], errors='coerce')
df['Smokes (packs/year)'] = df['Smokes (packs/year)'].fillna(0)

# Calculate Smoking Severity as a new column
df['Smoking Severity'] = df['Smokes (years)'] * df['Smokes (packs/year)']

# Convert 'Smokes' to a categorical column for visualization
df['Smokes'] = df['Smokes'].astype('category')

# Descriptive statistics
print(df.describe())

# Check unique values for categorical variables
print(df['Smokes'].value_counts())
print(df['Hormonal Contraceptives'].value_counts())

# Histogram for Age
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Boxplot for Smoking Severity by Smoking Status
sns.boxplot(x='Smokes', y='Smoking Severity', data=df)
plt.title('Smoking Severity by Smoking Status')
plt.show()

# Calculate and visualize correlation matrix
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Boxplot for Number of Sexual Partners vs. Biopsy Result
sns.boxplot(x='Biopsy', y='Number of sexual partners', data=df)
plt.title('Number of Sexual Partners vs. Biopsy Result')
plt.show()

# Create a subset for STD analysis
std_columns = ['STDs', 'STDs:HPV', 'STDs:AIDS']
if 'STDs:genital herpes' in df.columns:
    std_columns.append('STDs:genital herpes')

df_std = df[std_columns + ['Biopsy']]

# Correlation analysis for STDs
print(df_std.corr())

# Scatter plot for time since first diagnosis vs. biopsy result
if 'STDs: Time since first diagnosis' in df.columns:  # Check if column exists
    sns.scatterplot(x='STDs: Time since first diagnosis', y='Biopsy', data=df)
    plt.title('Time Since First Diagnosis vs. Biopsy Result')
    plt.show()

# Logistic Regression Model

# Features and target variable
X = df[['Age', 'Number of sexual partners', 'Smokes', 'Hormonal Contraceptives', 'STDs']]
y = df['Biopsy']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))