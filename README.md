# Analyzing Factors Affecting Cervical Cancer Risk: A Data-Driven Approach  

This project explores the relationship between various factors, such as sexual health, smoking, and medical history, to understand their impact on cervical cancer risk. By leveraging data analysis and statistical modeling, the goal is to identify significant predictors and develop a predictive model to assist in preventive healthcare efforts.  

---

## Table of Contents  
1. [Introduction](#introduction)  
2. [Dataset](#dataset)  
3. [Objectives](#objectives)  
4. [Tools and Libraries](#tools-and-libraries)  
5. [Analysis Workflow](#analysis-workflow)  
6. [Results and Insights](#results-and-insights)  
7. [How to Run the Project](#how-to-run-the-project)  
8. [Future Scope](#future-scope)  
9. [Contributions](#contributions)  

---
## Introduction  
Cervical cancer is a leading health concern globally, but it is also one of the most preventable cancers with early diagnosis and appropriate intervention. This project investigates the relationship between lifestyle, sexual health, and medical history factors to derive actionable insights and develop a predictive model to assist in preventive healthcare efforts.

## Dataset  
- **Source:** [Kaggle - Cervical Cancer Risk Classification Dataset](https://www.kaggle.com/datasets/loveall/cervical-cancer-risk-classification)  
- **Size:** Approximately 858 rows and 36 columns  
- **Description:** The dataset includes demographic, lifestyle, and medical history data, with a target variable (`Biopsy`) indicating whether cervical cancer was diagnosed.  

---

## Objectives  
1. Perform data cleaning and preprocessing to handle missing or invalid values.  
2. Conduct exploratory data analysis (EDA) to identify patterns and trends.  
3. Evaluate correlations between variables and the target (`Biopsy`).  
4. Develop a predictive model using logistic regression to assess cancer risk.  
5. Provide actionable insights for healthcare professionals.  

---

## Tools and Libraries  
- **Python Libraries:**  
  - `pandas`, `numpy`: Data manipulation and preprocessing  
  - `matplotlib`, `seaborn`: Data visualization  
  - `scikit-learn`: Statistical modeling and machine learning  
- **Power BI:** For advanced data visualization  

---

## Analysis Workflow  
1. **Data Cleaning**  
   - Handle missing values and outliers.  
   - Create new features, such as `Smoking Severity`.  

2. **Exploratory Data Analysis**  
   - Analyze distributions of key variables.  
   - Examine relationships between lifestyle factors, medical history, and cervical cancer.  

3. **Correlation Analysis**  
   - Use correlation heatmaps to identify significant relationships between predictors and the target variable.  

4. **Predictive Modeling**  
   - Train a logistic regression model to predict cervical cancer risk.  
   - Evaluate the model using metrics such as accuracy, precision, and recall.  

5. **Data Visualization in Power BI**  
   - Create visualizations like scatter plots, bar charts, and heatmaps for insights.  

---

## Insights
-Demographics: Age and smoking habits are critical factors influencing cancer risk.
-STD Impact: Certain STDs(Genital Herpes, HIV, Condylomatosis, Vulvo-Perineal Condylomatosis)  particularly with early and recurrent diagnosis, significantly increase risk.
-Contraceptive Use: Limited correlations observed between contraceptive use and cancer outcomes.
-High-Risk Profiles: Smoking severity and multiple STD diagnoses highlight individuals at higher risk.
-Correlations: Age, smoking, and sexual health variables are strongly linked to positive biopsy results.

---

## Results    
- Key predictors of cervical cancer include smoking history, contraceptive use, and STDs.  
- Strong correlations between lifestyle and medical history factors were identified.  
- The logistic regression model demonstrated high predictive performance, highlighting its potential for healthcare applications.  

---

## How to Run the Project  
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/Analyzing-Factors-Affecting-Cervical-Cancer-Risk.git

