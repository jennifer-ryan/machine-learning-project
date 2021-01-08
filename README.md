# Machine Learning Project
This repository contains a a web application created as part of the assessment in the Machine Learning and Statistics module for the Higher Diploma in Data Analytics with Galway-Mayo Institute of Technology.

## About the Repository
The repository can be accessed [here](https://github.com/jennifer-ryan/machine-learning-project). Click the green "Code" button and copy the link. In your command line type "git clone" followed by the repository link to create a local copy for review.

The contents of the repository are:
1. This **README** file that outlines the project and contains instructions on how to run the web application.
2. **powerproduction.csv**, a CSV file that contains two columns which represent wind speed and respective power output. This is used to train the model for this project.
3. **Power Production Analysis and Models**, a Jupyter Notebook that examines the data in the CSV file and builds several prospective models. These models are compared to one another and one was chosen to be implemented in the web application: Random Forest Regression. 
4. **model.pkl**, a pickle file that contains the Random Forest model created in the Jupyter Notebook.
5. **power.py**, a Python Flask app that runs the API. It imports the model from the pickle file, passes user input to it and sends the HTTP response back to the web page. 
6. **staticpages**, a folder that contains a HTML document, **index.html** which is the user interface. 
7. **requirements.txt**, a simple text file that contains the modules required to run the web application. 
8. A **Dockerfile** which allows you to create a container to run the web application.