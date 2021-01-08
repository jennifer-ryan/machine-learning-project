# Machine Learning Project
This repository contains a web application created as part of the assessment in the Machine Learning and Statistics module for the Higher Diploma in Data Analytics with Galway-Mayo Institute of Technology.

## About the Repository
The repository can be accessed [here](https://github.com/jennifer-ryan/machine-learning-project). Click the green "Code" button and copy the link. In your command line type "git clone" followed by the repository link to create a local copy for review.

The contents of the repository are:
1. This **README** file that outlines the project and contains instructions on how to run the web application.
2. **powerproduction.csv**, a CSV file that contains two columns which represent wind speed and respective power output. This is used to train the model for this project.
3. **Power Production Analysis and Models**, a Jupyter Notebook that examines the data in the CSV file and builds several prospective models. These models are compared to one another and one was chosen to be implemented in the web application: Random Forest Regression. 
4. **model.pkl**, a pickle file that contains the Random Forest model created in the Jupyter Notebook.
5. **power.py**, a Python Flask app that runs the API. It imports the model from the pickle file, passes user input to it and sends the HTTP response back to the web page. 
6. **staticpages**, a folder that contains a HTML document, **index.html** which is the user interface. 
7. **requirements.txt**, a simple text file that contains the modules required to run the web application. Note that it does not contain all of the packages used in the Jupyter Notebook, such as tensorflow for the neural network, as they were only used in the research phase and are not needed to run the application.
8. A **Dockerfile** which allows you to create a container to run the web application.

## Running the Web Application
You will need to have Python 3 and Docker installed on your machine to run this web application.

- Open Docker to start the Docker daemon.
- On the command line, navigate to the folder where you have cloned the repository.
- Run the command "**docker build -t power-app .**" This builds an image with the tag "power-app".  The "." allows the program to find the Dockerfile in the current folder. From this, the modules in requirements.txt are installed, the environment is set to the Flask app power.py, and the other files that are not in .dockerignore are copied to the image. From this image, several containers can be created.
- To view the image: "**docker image ls**"
-  To create a container run the command "**docker run -d -p 5000:5000 power-app**". The "-d" flag allows you to create a detached container so you can continue to use the terminal and "-p 5000:5000" binds port 5000 of the container and port 5000 on the local machine. The service will run on port 5000 of the machine.
- Open the local host in your browser: "http://127.0.0.1:5000/" and the web application is ready to use. 
- To view the containers created: "**docker container ls**"
- To end a container use the command "**docker kill**" followed by the container ID (This can be found with "docker container ls"). To completely remove the container run "**docker rm**" followed by the container ID.


### A Note on Docker
To run Docker on my OS, Windows 10 Home Edition, I had to install [Docker Desktop](https://docs.docker.com/docker-for-windows/install/) and [Virtual Box](https://www.virtualbox.org/wiki/Downloads). I also needed to [enable virtualisation](https://docs.docker.com/docker-for-windows/troubleshoot/#virtualization-must-be-enabled). If you run Windows Pro/Enterprise, Docker alone should suffice. 

### Using the Web Application
- Enter a number. Because the wind turbine only operates within a range of about 0.33-24.4m/s, values outside of this range are not accepted.
- Choose measurement units. Choices are metres per second (m/s), which is the default, kilometres per hour (kph), or miles per hour (mph). Units chosen outside of the default are converted to m/s for use with the model.
- Click the Convert button and the number you entered will be converted to m/s.
- Click the Predict Power button and a message will appear advising you of the predicted power output for that wind speed. 