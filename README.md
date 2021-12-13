# Traffic sign classifier

Traffic Sign Recognition Classifier capstone project for Machine Learning Zoomcamp course: [https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/12-capstone](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/12-capstone).

## Introduction

The main goal is build a model to classify traffic signs with Convolutional Neural Network.

## Dataset

The dataset we’ll be using to train our own custom traffic sign classifier is the German Traffic Sign Benchmark https://www.kaggle.com/valentynsichkar/traffic-signs-preprocessed.

### About the dataset

The German Traffic Sign Benchmark is a multi-class, single-image classification challenge held at the International Joint Conference on Neural Networks (IJCNN) 2011. We cordially invite researchers from relevant fields to participate: The competition is designed to allow for participation without special domain knowledge. Our benchmark has the following properties:

* Single-image, multi-class classification problem
* More than 40 classes
* More than 50,000 images in total
* Large, lifelike database

#### Credits

* [https://benchmark.ini.rub.de/](https://benchmark.ini.rub.de/)


### Copy of the datase

* https://drive.google.com/file/d/1-bGLNOY0z9-UwbW5iHUyIHiFzhQNK4n5/view?usp=sharing

Labels:

* [label_names.csv](./dataset/label_names.csv)

### Sample of dataset

![43 Classes of German TrafficSign](./43-classes-of-German-Traffic-Sign.png)


## Notebook

* Colab notebook: https://colab.research.google.com/drive/1Z8ktFYEDljLWVolxGTC0jFrDG5ohjpCQ#scrollTo=94vMp9UzVQrW
* Copy of the notebook here: [notebook.ipynb](./notebook.ipynb)

### What you'll find in the notebook

* Data preparation and cleaning
* Model creation
  * generator and training
  * model metrics
* Data augmentation
* model fitting
* Export model in h5
* Load model and evaluation
* Predict
* Covert model in tslite from h5

## Local deploy

Python required. For more see: https://packaging.python.org/tutorials/installing-packages/.

### Install & run

in /src dir:

```
pip install pipenv
pipenv install
pipenv shell
python predict.py
```

### Test

```
curl --location --request POST 'http://localhost:9696/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "http://clipart-library.com/images/gieERjykT.jpg"
}'
```


## Deploy

### Docker

```
docker build -t traffic-sign-classifier-prediction ./src
docker run -it -p 9696:9696 traffic-sign-classifier-prediction:latest
```

### Deploy to heroku

Heroku account needed. Install heroku cli.

#### Docker file

Update docker file:

```
#ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"] 
ENTRYPOINT ["gunicorn", "predict:app"]
```

#### login

heroku login
heroku container:login

#### create app in heroku

heroku create your-app-name

#### Push docker image to Heroku

heroku container:push web -a your-app-name

#### Deploy container on Heroku

heroku container:release web -a your-app-name

#### Launch app

Test is up: https://your-app-name-xyz.herokuapp.com/heartbeat

## LICENSE

[LICENSE](./../midterm-project/LICENSE)
