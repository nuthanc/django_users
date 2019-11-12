# django_users

Documentation link: https://docs.google.com/presentation/d/1uKZ61h4A_tfv9Nz_YYnQJfzpJVxooB5QCGtDJq2eVks/edit?usp=sharing

* After doing startproject and startapp, add the basic_app in the settings.py file and do the following:
* python manage.py migrate : To register the application with the entire project
* python manage.py makemigrations basic_app
* python manage.py migrate 
* pip install bcrypt
* pip install django[argon2]
* Add PASSWORD_HASHERS in settings.py file, starting with the most powerful Argon
* Options can be given to Password validators as seen in minimum length
* What you as developer provides should be in 'static' folder and what the user provides should be in 'media' folder