# iris-species-predictor


## Python Flask web app which predicts the species of Iris flower.
You can find a live version of the site in Heroku-> https://iris-speciespredict.herokuapp.com/

It uses trained **Logistic Regression model**

This model is trained on local machine and saved as a pickle file. The saved model is called using Flask.

**Flask** will render the **HTML** page to get the user inputs used for the prediction
**Gunicorn**  will be used as webserver in heroku 




## How to run locally

- Clone the repo
``` 
git clone https://github.com/clerintom/iris-species-predictor.git
```

- Change your current working directory to this
``` 
cd iris-species-predictor 
```

- Create a virtual environment
```
python -m venv venv
```

- Activate the virtual environment 
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

