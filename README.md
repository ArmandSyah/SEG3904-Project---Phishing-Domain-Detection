# SEG3904-Project---Phishing-Domain-Detection

Innovation project looking at different ways of tyring to predict phishing sites through link alone

## Requirements
Python 3.6+
Mongo DB Community Version
Mongo DB Compass
Windows 10 Prefered

## How to set up

### Setting up virtualenv
1. Install virtualenv by typing 'pip install virtualenv' on the command line
2. Next, install virtualenvwrapper-win by typing 'pip install virtualenvwrapper-win' on the command line
3. Make a virtual environment, by typing 'mkvirtualenv [name of virtualenv]'
4. The virtual environment should be activated, indicated by the '[name of virtualenv]' on the left side of prompt
    - You can deactivate the virtual environment by typing 'deactivate'
    - If you want to go back to the virtual environment type 'workon [name of virtualenv]'

### Installing packages
1. Change Directory to the root of this project (ex: C:\Users\Armand Syahtama\Documents\SEG3904-Project---Phishing-Domain-Detection) 
2. Install all the required packages by typing 'pip install -r requirements.txt'. This recursively reads the contents of requirements.txt and installs each package per line
3. Since there are dependencies between files in different folders in the src, type 'pip install -e .', to ensure they are all working

### Setting up Data and Models
The models and data have already been set up, but in case you want to try building everything yourself, here's how

0. Make sure you have Mongo DB installed as well as Mongo DB Compass to see url insertions. Shouldnt have to change any of the defaults during installation (so keep hostname: localhost and port: 27017)
1. While terminal is still in the root of the project, set up the file probability json by typing 'python src\data\make_data.py'. This will set up a json file containing all possible url file extensions read from the datasets and calculate the probabilities of each
2. Turn the raw url data into training data with processed features by typing 'python src\features\build_features.py'. This will process various features per url and then store them into a MongoDB collection
3. Build the machine learning models (Naive Bayes, Decision Tree, Random Forest), by typing 'python src\models\train_model.py'.
4. Finally, start predicting using 'python src\models\predict_model.py'. This will start up a flask server that will ingest urls through POST requests, do a prediction using a preloaded random forest model, and then store results and sends back a response containing results.
You can do the post requests using CURL, Postman, ect. The endpoint for prediction is http://127.0.0.1:5000/predict
    - (Optional): to test api, I have set up a python script called test_api.py. Type 'python test_api.py' and it will run through a set of phishing and benign sites and spit out percentage of correct/incorrect predictions
