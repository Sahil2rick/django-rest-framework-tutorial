# django-rest-framework-tutorial


Project setup
Create a new Django project named tutorial, then start a new app called quickstart.

# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..
The project layout should look like:

$ pwd
<some path>/tutorial
$ find .
.
./manage.py
./tutorial
./tutorial/__init__.py
./tutorial/quickstart
./tutorial/quickstart/__init__.py
./tutorial/quickstart/admin.py
./tutorial/quickstart/apps.py
./tutorial/quickstart/migrations
./tutorial/quickstart/migrations/__init__.py
./tutorial/quickstart/models.py
./tutorial/quickstart/tests.py
./tutorial/quickstart/views.py
./tutorial/settings.py
./tutorial/urls.py
./tutorial/wsgi.py
It may look unusual that the application has been created within the project directory. Using the project's namespace avoids name clashes with external modules (a topic that goes outside the scope of the quickstart).

Now sync your database for the first time:

python manage.py migrate
We'll also create an initial user named admin with a password of password123. We'll authenticate as that user later in our example.

python manage.py createsuperuser --email admin@example.com --username admin
Once you've set up a database and the initial user is created and ready to go, open up the app's directory and we'll get coding...
