# django_users

Documentation link: https://docs.google.com/presentation/d/1uKZ61h4A_tfv9Nz_YYnQJfzpJVxooB5QCGtDJq2eVks/edit?usp=sharing

* After doing startproject and startapp, add the basic_app in the settings.py file and do the following:
* python manage.py migrate : To register the application with the entire project
* python manage.py makemigrations basic_app
* python manage.py migrate 
* pip install bcrypt
* pip install argon2-cffi
* Add PASSWORD_HASHERS in settings.py file, starting with the most powerful Argon
* Options can be given to Password validators as seen in minimum length
* What you as developer provides should be in 'static' folder and what the user provides should be in 'media' folder

### models.py setup for additional builtin User attributes
* User model setup in models.py file. The default User is already present but in this file we do additional configuration
* Since profile_pic is specified in upload_to, profile_pic directory must be created under media directory
* For images, we need to do pip install pillow

### forms.py setup
* Checkout forms.py file under basic_app 
* Need to register model in admin.py
* Whenever, admin.py is modified or a new model is created, we need to migrate
* python manage.py migrate
* python manage.py makemigrations basic_app
* python manage.py migrate

### template and url setup 
* Created 4 files under basic_app template, urls.py in basic_app
* In registration.html form, we need to have enctype since we are uploading multimedia data

### Registration
* Hashing the password using set_password as seen in views.py file
* request.FILES when file is uploaded by user and key as defined in models

### Create superuser
* python manage.py createsuperuser

### Login
* LOGIN_URL in settings.py file
* Fill login.html file
* More updates in views.py file 
* request.POST.get('username') where username is name field in the HTML form
* Update urls.py of project and urls.py of app

### Media
* Need to add some setup in urls.py of project folder