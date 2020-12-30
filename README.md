# A small service for shortening links

### This is a small link shortening service written in Django 3. 

It was created as a thesis for the Python course https://itproger.com/intensive/python

### Run project
First you must clone project then choice run method
1. Clone project
   `git clone https://github.com/vanya2143/briefly`

2. Choose a way to run the project

### Launch methods

#### Run from source

1. Go to the project directory
   
2. Install and create virtualenv (in the project directory)
    1. Install `pip3 install virtualenv`
    2. Create virtualenv `python3 -m venv .env`
    3. Install requirements `pip3 install -r requirements.txt`

3. Create a database and run project
    1. Create database `python2 manage.py migrate`
    2. Run `python3 manage.py runserver`

#### Run in docker-compose

1. Go to the project directory
2. Run command `docker-compose up --build`
3. Run migrations `docker-compose run web python3 manage.py migrate`
