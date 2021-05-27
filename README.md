# FOREXRecommendationSystem

The goal of the project was to create a system recommending transactions on the forex market.
To build recommending algorithms, in project were used  Candlestick chart method from Technical Analysis and recursive
artificial neural networks with LSTM units. Evrything was wrappend into Django web app with generated Angular frontend.
The algorithms were developed and tested in the environment Jupyter Lab.

## Installation

### Pre Required

- Python 3.8
- Angular 11.0.3
- Node 14.15
- Npm 6.14.8


### 1. Clone the repository
  
  `git clone https://github.com/sondisonda/FOREXRecommendationSystem`
  

### 2. Frontend

Go to the `forexAPP` directory via terminal and enter `npm install`.
Then execute` ng build` and copy `forexAPP\dist\forexAPP` folder contents to `forexAPI\forexPredict\static`.

### 3. Backend

Create and/or activate your Python virtual environment and install project dependencies.
To do it go to the `forexAPI` directory via terminal with active venv and execute `pip install -r requirements.txt`.
After that you check if evrything is correct with database, execute `python manage.py makemigrations`, and next command
`python manage.py migrate`. If there is no errors you can start server with `python manage.py runserver`



## Use application

Enter `localhost:8000` in your browser and enjoy FOREX stock predictions 