from flask import Flask, render_template, request
import numpy as np
import pickle
import matplotlib
matplotlib.use('Agg')  # For non-GUI environments
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("MLR_model", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs from HTML form
        age = float(request.form['age'])
        experience = float(request.form['experience'])

        # Prepare input for prediction
        input_data = np.array([[age, experience]])

        # Predict income
        predicted_income = model.predict(input_data)[0]

        # Generate regression graph
        generate_graph(age, experience, predicted_income)

        return render_template(
            'index.html',
            prediction_text=f"Predicted Income: ₹ {predicted_income:,.2f}"
        )
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

def generate_graph(age, experience, predicted_income):
    # Generate scatter plot + prediction point
    plt.figure(figsize=(6,4))
    plt.scatter(age, predicted_income, color='red', label='Predicted Income', s=80)
    plt.xlabel("Age")
    plt.ylabel("Predicted Income")
    plt.title("Multiple Linear Regression Prediction")
    plt.legend()
    plt.grid()

    # Save graph in static folder
    graph_path = os.path.join("static", "prediction.png")
    plt.savefig(graph_path)
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)
