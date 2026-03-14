
Bankruptcy Prediction using Machine Learning


1.Project Overview
Financial bankruptcy prediction is a critical problem in business risk management.
Organizations, investors, and financial institutions need reliable systems to identify companies with high bankruptcy risk before financial collapse occurs.

This project builds a Machine Learning–based bankruptcy prediction system that analyzes financial risk factors and predicts whether a company is likely to go bankrupt or remain financially stable.

The system uses multiple ML models, performs data preprocessing, feature selection, model comparison, and evaluation, and identifies the best-performing algorithm for deployment.



2) Business Objective

This is a binary classification problem.
Goal:
Predict whether a company will be:
 0 → Non-Bankrupt
 1 → Bankrupt
The system analyzes financial indicators and risk factors to estimate the probability of bankruptcy.
Dataset Information
* Total Companies: 250
* Total Features: 7 financial risk indicators
* Target Variable: Bankruptcy status



3)Exploratory Data Analysis (EDA)
Exploratory Data Analysis was performed to understand patterns, distributions, and relationships between financial indicators.

(1)Class Distribution
Bar chart analysis showed:
Majority companies are non-bankrupt
Smaller portion represent bankrupt firms
This indicates a slight class imbalance in the dataset.

(2) Correlation Heatmap**
The correlation analysis revealed strong relationships between certain financial indicators.
Key observations:
* Financial Flexibility
* Credibility
* Competitiveness
These features show strong positive correlations, indicating their importance in predicting financial stability.
Meanwhile:
* Industrial Risk
* Management Risk
show weaker correlations with bankruptcy outcomes.

(3)  Boxplot Analysis
Boxplots highlight how financial indicators vary between bankrupt and non-bankrupt companies.
Key insight:
Companies with low credibility and poor financial flexibility show significantly higher bankruptcy probability.

4) Data Preprocessing
To ensure accurate model training, the dataset underwent several preprocessing steps.
Data Cleaning
Removed duplicate records
Verified dataset consistency
Checked for missing or invalid values
Encoding

Categorical labels converted to numeric format:
0 → Non-bankrupt
1 → Bankrupt

Feature Scaling
Used StandardScaler to normalize features so that all variables contribute equally during model training.
Train-Test Split

Dataset divided into:
Training Data: 80%
Testing Data: 20%
This ensures reliable evaluation on unseen data.

5) Feature Selection
Feature selection was performed to improve model performance and reduce overfitting.

Methods used:

* Logistic Regression (L1 regularization)
* SelectKBest statistical method
* Correlation heatmap analysis
This helped identify the most influential predictors of bankruptcy risk.
Only statistically significant features were retained for model training.

6) Machine Learning Models Implemented
The project implemented and compared five different machine learning models.

Model	                       Description

Logistic Regression	       Linear classification model

Decision Tree	               Rule-based classification

K-Nearest Neighbors	       Distance-based classification

Random Forest	               Ensemble learning model

XGBoost	                       Gradient boosting algorithm


7) Training Approach
Models trained using Scikit-learn and XGBoost
Hyperparameter tuning using GridSearchCV
Scaling applied for models sensitive to feature magnitude (KNN, SVM)
Each model evaluated independently

8) Model Performance Comparison
Model Evaluation Metrics

|      Model|      Accuracy	       |       F1-Score	      |      Precision|      Recall|         ROC-AUC|         Comment|
|-|-|-|-|-|-|-|
|Logistic Regression|       0.76|        0.86|      1.00|        1.00|         0.30|   Weak performance<br /> |
|Random Forest|       1.00|         1.00 |      1.00|        1.00|         1.00| Excellent \& stable|
|Decision Tree|       1.00|         1.00|      1.00|        1.00|         1.00|Possibly overfitted|
|KNN|       1.00|         1.00|      1.00|        1.00|         1.00|Sensitive to scaling|
|XGBoost|       1.00|         1.00|      1.00|        1.00|         1.00|Excellent \& robust|


Observations
 1️⃣ Logistic Regression
* Underperformed on the test dataset.
* Accuracy = 0.76, ROC-AUC = 0.30.
* Indicates the model is too simple for the dataset.
* Unable to capture non-linear relationships between financial features.
* 
 2️⃣ Random Forest
* Achieved perfect performance metrics on the dataset.
* Out-of-Bag (OOB) score = 0.987, indicating strong generalization.
* Ensemble learning makes it stable and less prone to overfitting.
* Easier to interpret and tune compared to boosting models.

 3️⃣ Decision Tree
* Achieved perfect accuracy on both training and testing sets.
* However, single decision trees are prone to overfitting, especially on small datasets.
* Less stable compared to ensemble models.
  
 4️⃣ K-Nearest Neighbors (KNN)
* Delivered excellent evaluation metrics.
* Performance depends heavily on distance metrics and feature scaling.
* Can become computationally expensive for large datasets during prediction.

5️⃣ XGBoost
* Achieved perfect evaluation scores.
* Known for strong generalization and high predictive power.
* Includes regularization mechanisms to reduce overfitting.
* Handles complex feature interactions effectively.

9)Final Model Selection
After evaluating all models:
Random Forest was selected as the final model for deployment.

Reasons:
* Perfect classification metrics
* Stable ensemble architecture
* Lower risk of overfitting compared to single-tree models
* Balanced combination of accuracy, interpretability, and robustness

10)Project Structure
bankruptcy-prediction-ml

│

├── data

│   └── bankruptcy\_dataset.xlsx

│

├── notebooks

│   └── Bankruptcy\_Prediction\_Model.ipynb

│

├── src

│   ├── data\_preprocessing.py

│   ├── model\_training.py

│   └── prediction.py

│

├── models

│   └── trained\_model.pkl

│

├── images

│   └── project\_demo.png

│

├── requirements.txt

├── README.md

└── app.py

11) Project Demo
Model Used: Random Forest Classifier
Accuracy Achieved: 100%
The trained Random Forest model is deployed using a simple interface where users can enter financial risk indicators to predict whether a company is **Bankrupt or Non-Bankrupt.**



Users select values for the following financial indicators:
* Industrial Risk
* Management Risk
* Financial Flexibility
* Credibility
* Competitiveness
* Operating Risk

After clicking Predict Bankruptcy, the model analyzes the input features and returns the prediction result.

Example Prediction Interface:

* Example Prediction Result – Non-Bankrupt Company
* Example Prediction Result – Bankrupt Company

This demo shows how the machine learning model can assist analysts and financial institutions in **identifying companies with potential bankruptcy risk based on financial indicators.**

12) Tech Stack
|                                     Category|                                           Tools |
|-|-|
|                                   Programming|                                             Python|
|                                   Data Analysis|                                           Pandas, NumPy|
|                                   Visualization|                                           Matplotlib, Seaborn|
|                                   Machine Learning|                                            Scikit-learn|
|                                   Advanced Models|                                             XGBoost|
|                                  Model Deployment|                                             Streamlit|



13) Installation
Clone the repository:
git clone https://github.com/yourusername/bankruptcy-prediction-ml.git
Install dependencies:

* pip install -r requirements.txt
* Run the notebook to reproduce results.

14) Future Improvements
* Deploying the model as a Streamlit web application
* Using larger real-world financial datasets
* Applying deep learning models
* Implementing automated data pipelines
* Adding real-time financial risk prediction



15)Key Learning Outcomes
* This project demonstrates practical experience in:
* End-to-end machine learning workflow
* Financial risk analysis
* Feature engineering and model selection
* Model comparison and evaluation
* Preparing ML systems for deployment


Author
Prachi Patted
Information Science Engineer
Skills: Machine Learning | Data Science | Python | Data Analysis


# Bankruptcy_Prediction
 4d79255adafd67d2c6f9b7d9194fcf6467a4d13c
