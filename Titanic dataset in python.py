import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
data = pd.read_csv('titanic.csv')

# Display the first few rows of the dataset
print(data.head())

# Exploratory Data Analysis (EDA)
print(data.info())
print(data.describe())

# Visualize missing values
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.show()

# Data Cleaning
# Fill missing 'Age' values with the median age
data['Age'].fillna(data['Age'].median(), inplace=True)

# Fill missing 'Embarked' values with the most common port
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' column due to too many missing values
data.drop('Cabin', axis=1, inplace=True)

# Drop rows with missing 'Fare' values
data.dropna(subset=['Fare'], inplace=True)

# Convert categorical variables to numerical ones
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Feature Engineering
# Create a new feature 'FamilySize'
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

# Drop unnecessary columns
data.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

# Define feature variables (X) and target variable (y)
X = data.drop('Survived', axis=1)
y = data['Survived']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model Building
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

class_report = classification_report(y_test, y_pred)
print('Classification Report:')
print(class_report)
