# Django Morgan Blog

You can use the personal blog project I made according to your wishes.

## Description

I made the backend part of the project. I made some minor changes to the front end. After installing the project, you will be able to publish blogs from the admin panel and manage them as you wish. Users can register, login and edit their own information. Your most read blog posts will be in the popular blogs section of the page. The blogs you share can be commented and shared. Users can contact you in the contact section.
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
