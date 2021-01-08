from flask import Flask, render_template, request
import pickle
import numpy as np

# Create the app
app = Flask(__name__,
            static_url_path = "", 
            template_folder = "staticpages")

# Load the model
with open("model.pkl", "rb") as mod:
    model = pickle.load(mod)

# Index page 
@app.route('/')
def index():
    index= render_template("index.html")
    return index

# Run prediction
# Adapted from: https://medium.com/techcrush/how-to-deploy-your-ml-model-in-jupyter-notebook-to-your-flask-app-d1c4933b29b5
# and https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/
@app.route("/predict", methods=["POST"])
def predict():
    # Get input from user
    data = np.array(request.form["input"])
    # Change format to suit model
    data = data.reshape(-1,1)
    # Put data through model to make a prediction
    prediction = model.predict(data)
    
    # Get value of wind speed for return request
    wind_speed = float(data[0][0])
    # Send formatted prediction back to index
    return render_template("index.html", prediction=f"A wind speed of {wind_speed:.2f}m/s yields an estimated power output of {prediction[0]:.2f}kW.") # just want the value, not the array

# Run main
if __name__ == "__main__":
   app.run(debug=True)