# Performance Metrics API
API to display a list of movies and actors which reads from Ghibli API:

# Quickstart
Download the zip file and unzip it in the folder of your choice.

## Requirements
- Python 3.8+
- virtualenv
- Django 3.1.2
- For development purpose this service needs cache folder in the root directory.
    If you like to change the path please check the "CACHES" in the "settings.py" module.
    
## Install
Open the Terminal in the project folder and run the following commands:

1- Create a virtualenv and activate it:  
On Linux:
```shell script
> virtualenv venv 
...
> source venv/bin/activate
```
Or on Windows:
```shell script
> py -3 -m venv venv
> ...
> venv\Scripts\activate.bat
```

3- Install all the requirements:
```shell script
> pip install -r requirements.txt
```
Or on Windows:
```shell script
> py .\venv\Scripts\pip.exe install -r requirements.txt
```

4- Run DB migrations:
```shell script
> python manage.py migrate
```
 
## Run the service: 
```shell script
> python manage.py runserver
```

## Usage
- Open [http://127.0.0.1:8000/movies](http://127.0.0.1:8000/movies)

## Run the Test
```shell script
> python manage.py test
```
