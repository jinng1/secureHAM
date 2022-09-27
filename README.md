# secureHAM dev repo
## How to run
Django is best run in a virtual environment, feel free to setup with the environment you are comfortable using
### Setup for pipenv

In the command prompt\
`pip install pipenv`\
\
cd to the repo directory\
`pipenv shell`\
`pip install -r requirements.txt`

Place the .env file into the root directory. This contains the django secret key

### Setup for web app
Once the requirements are installed, you will need to migrate the database models. We are using sqlite for now, will change in the future\
\
make sure you are in the env `pipenv shell`\
`python manage.py makemigrations`\
`python manage.py migrate`\
\
Create superuser\
`python manage.py createsuperuser`\
\
Once created, start the web app\
`python manage.py runserver`

To create accounts for now, go to user management and use the django user management
