# Iris-species-predictor


### Python Flask web app which predicts the species of Iris flower.
You can find a live version of the site -> https://iris-speciespredict.herokuapp.com/

It uses trained **Logistic Regression model** 
These model is trained on local machine and saved using pickle library in Python. Then the saved models are called using Flask.

**HTML** is used for the frontend.

**How to run locally**

 - Clone the repo
``` 
git clone https://github.com/clerintom/iris-species-predictor.git
```

- Change your current working directory to this
``` 
cd iris-species-predictor 
```

- create a virtual environment
```
python -m venv venv
```

- activate the virtual environment 
```
#linux
source env/bin/activate
# windows
venv\Scripts\activate 
```

- Install the required libraries 
```
pip install -r requirements.txt
```

- Run the app and predict away! :) 
``` 
python app.py
```










[here]:http://clerin.pythonanywhere.com/
