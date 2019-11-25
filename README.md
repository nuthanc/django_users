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

### Next is deployment
* pythonanywhere
* Go to console, and then click on Bash
* Create a virtual environment using the following command:
* mkvirtualenv --python=python3.7 myproj
* pip list - to check all the packages installed
* pip install -U django==2.2.1
* To check, which django-admin.py
* git clone whatever_project
* Go to project dir and do python manage.py migrate
* python manage.py makemigrations name_of_app
* python manage.py migrate
* python manage.py createsuperuser
* Go to dashboard and select the Web tab and Add a new web app
* Go next, select Manual configuration, select Python version and next
* Under virtalEnv enter: /home/nuthan(username)/.virtualenvs/myproj(project name)
* Start a console in this virtualenv to get the path to Source code 
* Go to working directory and do pwd and enter that in the Source code 
* Click on WSGI file

* Remove HELLO WORLD code
* Uncomment imports of os and sys, path(Need to change this to actual path), if path block
* Then change path using os.chdir(path)
* os.environ.setdefault("DJANGO_SETTINGS_MODULE","the_project_name.settings")
* import django;django.setup()
* Uncomment from django.core ... and the line below it which is application ...
* Then save this
* Go back to Dashboard
* Click on Web
* Click on your pythonanywhere.com link
* Go back to Web tab to fix Django Admin weird look
* Move to Static files
* Enter URL as /static/admin and PATH as /home/user_name/.virtualenvs/myproj/lib/python3.7/site-packages/django/contrib/admin/static/admin
* Come all the way to the top and click "Reload .com"
* Go to Files tab
* django-deployment-example, click on your project and settings.py file and pass in your username.pythonanywhere.com in ALLOWED_HOSTS and save that
* Create static folder under your working directory
* Come back to Web tab and Reload 
* Go back to Files, deployment-example, project's settings.py file and set DEBUG=False and save
* To set the path to another static file, go to Web tag and go to Static files section
* Enter URL as /static/ and file path to actual static file like /home/user_name/your_project/static and Reload those changes