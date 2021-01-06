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
    # change format to suit model
    data = data.reshape(-1,1)
    # Put data through model to make a prediction
    prediction = model.predict(data)
    # Send prediction to 'predict' page
    return render_template("index.html", prediction=prediction[0]) # just want the value, not the array


# Run main
if __name__ == "__main__":
   app.run(debug=True)