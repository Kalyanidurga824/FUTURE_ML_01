from flask import Flask, render_template, request
import os
import joblib
import pandas as pd

app = Flask(__name__)

# -------------------------------------------------
# FIXED MODEL PATH (BASED ON YOUR STRUCTURE)
# ML_SALES_FORECAST/notebook/models/sales_model.pkl
# -------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "notebook", "models", "sales_model.pkl")

print("MODEL PATH:", MODEL_PATH)
print("EXISTS:", os.path.exists(MODEL_PATH))

# Load model
model = joblib.load(MODEL_PATH)

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = pd.DataFrame([[
            int(request.form["store_nbr"]),
            int(request.form["onpromotion"]),
            int(request.form["family_encoded"]),
            int(request.form["year"]),
            int(request.form["month"]),
            int(request.form["day"]),
            int(request.form["day_of_week"])
        ]], columns=[
            "store_nbr",
            "onpromotion",
            "family_encoded",
            "year",
            "month",
            "day",
            "day_of_week"
        ])

        prediction = model.predict(data)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted Sales: {prediction:.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)