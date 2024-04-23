# django-example
A simple  Django implementation of algorithms of Differential Evolution and Classic Generic Algorithm.

---

## Table of Contents
- [Intro](#intro)
- [How to run](#how-to-run)

## Intro
Here I implement a basic Django implementation. The system only executes the implementation of Differential Evolution (DE) and Classic Generic Algorithm (CGA) on a simple function. As this is only demostrative I didn't include other functions or the functionality to change parameters. 

## How to run
1. Clone the repository.
2. Go to ```.git/info/exclude``` and add:
```
  *.pyc
  *.sqlite3
  *_initial.py
  *.png
  *.socket
  *.sock
  env/
  .env
  **/migrations/
  **/static/
```
4. Create an environment using virtualenv or conda, it's up to you.
5. Install the requirements.
```
pip install -r requirements.txt
```
7. To run:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
In your browser go to: ```http://127.0.0.1:8000/optimization/```. Sign up and log in then only push in the button you want to execute.

8. If you want to access the Django admin panel, first create a super user
```
python manage.py createsuperuser --username admin --email yourmail@yourdamin.com
```
Then go to In your browser go to: ```http://127.0.0.1:8000/admin/``` and log in.
