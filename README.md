# A Complete Beginner's Guide to Django

This is Study project that I was made by studying https://simpleisbetterthancomplex.com

## Table of Contents

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


In order to create the main subject make a superuser (python manage.py createsuperuser).
Login as superuser.
Then access admin page (127.0.0.1:8000/admin).

And create the new boards subject.
Usual users can create new topics and reply on topics.

