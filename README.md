# Django Morgan Blog

You can use the personal blog project I made according to your wishes.

## Description

I made the backend part of the project. I made it with Jquery on the front end with minor modification that I can do some operations on the back end. After installing the project, you will be able to publish blogs from the admin panel and manage them as you wish. Users can register, log in and edit their own information. Your most read blog posts will be in the popular blogs section of the page. The blogs you share can be commented and shared. Users can contact you in the contact section.<br>
I used Jinja template engine as template language in the project. I made the backend with Python's Django framework.

## Installation

```bash
git clone https://github.com/ibrahimmuradov/django_morgan_blog.git .
pip install -r requirements.txt
django-admin startproject core . 
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```
