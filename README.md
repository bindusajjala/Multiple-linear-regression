# Multiple-linear-regression
# 📊 Multiple Linear Regression Model - Income Prediction

## 🚀 Project Overview
This project demonstrates an **end-to-end implementation** of a **Multiple Linear Regression (MLR)** model using **Python** and **Flask**.  
It predicts an individual's **Income** based on two independent variables:
- **Age**
- **Experience**

The project includes **data preprocessing**, **exploratory data analysis (EDA)**, **model building**, **model deployment** using **Flask**, and a **responsive HTML interface**.

---

## 🛠️ Technologies Used
- **Python 3.11+**
- **NumPy** → For numerical computations  
- **Pandas** → For data manipulation & preprocessing  
- **Matplotlib** → For data visualization  
- **Scikit-learn** → For building the Multiple Linear Regression model  
- **Pickle** → For saving and loading the trained model  
- **Flask** → For deploying the model on a web app  
- **HTML / CSS** → For creating a beautiful and interactive frontend

---

## 📊 Dataset Description
The dataset contains three main columns:

| Column Name    | Description                  | Data Type |
|---------------|-------------------------------|-----------|
| **Age**       | Age of the individual         | Integer   |
| **Experience**| Years of work experience      | Integer   |
| **Income**    | Annual income in USD          | Float     |

---

## 🔄 End-to-End Workflow

### **1. Data Preprocessing**
- Import dataset using **pandas**  
- Handle missing values if any  
- Check for multicollinearity  
- Split dataset into **train** and **test** sets  

### **2. Exploratory Data Analysis (EDA)**
- Plot scatterplots between **Age**, **Experience**, and **Income**  
- Draw heatmaps to check correlations  
- Visualize regression lines  

### **3. Model Building**
- Use **Multiple Linear Regression** from **scikit-learn**
- Train model using training data
- Evaluate using:
  - R² Score
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)

### **4. Model Saving**
- Save trained model as `model.pkl` using **pickle**

### **5. Model Deployment**
- Create a **Flask API** to:
  - Take inputs (**Age**, **Experience**) from HTML form  
  - Load the saved `model.pkl`
  - Return predicted income to the frontend

### **6. Visualization**
- Show a **graph** on HTML:
  - Training data points
  - Regression plane/line
  - Predicted point highlighted

---

## 📈 Multiple Linear Regression Formula

\[
Y = b_0 + b_1 \cdot X_1 + b_2 \cdot X_2
\]

Where:
- \( Y \) = Predicted Income  
- \( X_1 \) = Age  
- \( X_2 \) = Experience  
- \( b_0 \) = Intercept  
- \( b_1, b_2 \) = Regression Coefficients




