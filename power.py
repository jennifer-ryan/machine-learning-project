from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__,
            static_url_path = "", 
            template_folder = "staticpages")

with open("model.pkl", "rb") as mod:
    model = pickle.load(mod)

# Index
@app.route('/')
def index():
    index= render_template("index.html")
    return index

# Adapted from https://medium.com/techcrush/how-to-deploy-your-ml-model-in-jupyter-notebook-to-your-flask-app-d1c4933b29b5
# and https://medium.com/datadriveninvestor/deployment-of-machine-learning-project-using-flask-bf6e5a750319
# and https://towardsdatascience.com/deploying-a-trained-ml-model-using-flask-541520b3cbe9

# For prediction to appear on same page: https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/
@app.route("/predict", methods=["POST"])
def predict():
    # Get input from user
    data = np.array(request.form["input"])
    # Change format to suit model
    data = data.reshape(-1,1)
    # Put data through model to make a prediction
    prediction = model.predict(data)
    # Get value of wind speed to send back to page
    wind_speed = float(data[0][0])
    # Send prediction back to index - formatted here
    return render_template("index.html", prediction=f"A wind speed of {wind_speed:.2f}m/s yields an estimated power output of {prediction[0]:.2f}kW.") # just want the values, not the arrays

# Run main
if __name__ == "__main__":
   app.run(debug=True)