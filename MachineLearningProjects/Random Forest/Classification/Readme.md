# Holiday Package Prediction README

## Overview

This project is focused on predicting whether a customer will purchase a holiday package based on various features like age, income, marital status, and others. The prediction model is built using machine learning techniques, and the data is preprocessed to ensure quality before training.

## Problem Statement

The company "Trips & Travel.Com" aims to expand its customer base by introducing new packages, including a Wellness Tourism Package. However, previous marketing efforts have been inefficient, leading to high costs with minimal results. This project seeks to harness existing customer data to make marketing more efficient by predicting which customers are likely to purchase a holiday package.

## Dataset

The dataset consists of 4888 rows and 20 columns and was sourced from [Kaggle](https://www.kaggle.com/datasets/susant4learning/holiday-package-purchase-prediction). It contains various features like customer demographics, package preferences, and more.

## Libraries Used

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `plotly`
- `scikit-learn`
- `warnings`

These libraries are essential for data manipulation, visualization, and machine learning tasks.

## Data Preprocessing

1. **Handling Missing Values**: Missing values in the dataset are handled by imputing medians for numerical columns and modes for categorical columns.
2. **Data Cleaning**: Duplicate values are removed, and categories are standardized.
3. **Feature Engineering**: New features are created, and irrelevant columns like `CustomerID` are dropped.
4. **Train-Test Split**: The dataset is split into training and testing sets to evaluate the model's performance.

## Feature Engineering

The dataset is divided into numerical and categorical features, and transformations like one-hot encoding for categorical data and standard scaling for numerical data are applied.

## Model Training

Multiple machine learning models are trained, including:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

These models are evaluated using metrics like accuracy, F1 score, precision, recall, and ROC AUC score.

## Hyperparameter Tuning

The Random Forest model is further optimized using `RandomizedSearchCV` to find the best parameters.

## Model Evaluation

Each model's performance is evaluated on both the training and test datasets, and results are printed for comparison.

## ROC AUC Plot

The script also generates a ROC AUC curve for the Random Forest model to visually assess its performance. The plot is saved as `auc.png` and is displayed for further analysis.

## How to Run

1. **Data Preparation**: Ensure that the dataset is available in the same directory as the script.
2. **Install Dependencies**: Install the required libraries using pip if they are not already installed.
3. **Execute the Script**: Run the script in a Python environment to train models and generate evaluation metrics.

## Results

The final results, including the best hyperparameters and ROC AUC plots, will help in determining the most suitable model for predicting holiday package purchases, thus aiding in more targeted marketing strategies.