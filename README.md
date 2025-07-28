# 🧬 Breast Cancer Diagnosis using Machine Learning

This project aims to build a predictive machine learning model to diagnose whether a tumor is **malignant (M)** or **benign (B)** based on features computed from digitized images of breast masses. These features capture various characteristics such as texture, radius, area, smoothness, and more.

---

## 📂 Dataset Overview

- **Rows**: 569  
- **Columns**: 33  
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))  
- **Target Variable**: `diagnosis` (Malignant = M, Benign = B)  
- **Note**: The column `Unnamed: 32` is empty and was dropped during preprocessing.

Each row represents data from one patient, including a unique ID, diagnosis label, and numeric measurements of tumor features calculated from digital mammogram images.

---

## 🛠️ Project Steps

### 1. 🧹 Data Preprocessing
- Removed unnecessary columns like `id` and `Unnamed: 32`
- Handled missing values (if any)
- Normalized feature values for model compatibility
- Selected relevant features for training

### 2. 📊 Exploratory Data Analysis (EDA)
- Used histograms, scatter plots, and heatmaps to understand feature distributions and correlations
- Identified patterns and relationships between tumor characteristics and diagnosis
- Observed that certain features (e.g., `radius_mean`, `concavity_worst`) were strongly correlated with malignancy

### 3. 🤖 Model Selection & Training
- Trained multiple machine learning models including:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Random Forest
- Evaluated models using metrics like:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
- Chose the best-performing model based on balanced performance

### 4. 📈 Results & Discussion
- Models achieved high accuracy in predicting diagnoses
- Identified top contributing features to diagnosis predictions
- Discussed real-world implications and limitations of the analysis
- Suggested areas for further research, such as deeper neural networks or real-time diagnostics

---
## Demo
[Click here to view the video demo](https://i.imgur.com/w3kEA0t.mp4)

---

## ✅ Key Findings
- Some features (especially "_worst" and "_mean" values) carry strong predictive power.
- Random Forest and SVM performed the best in terms of overall classification metrics.
- Feature normalization significantly improved model performance and training stability.

---

## 🔚 Conclusion

- This analysis demonstrates that machine learning can effectively support early breast cancer diagnosis.
- With further tuning and clinical validation, such models can assist radiologists and improve diagnostic workflows.
- The project underscores the importance of clean data, feature selection, and model evaluation in health data applications.

---

## 🧾 References

- [UCI Breast Cancer Diagnostic Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
- Scikit-learn documentation
- Relevant academic literature on medical machine learning
