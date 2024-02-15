# project-manager
Step 1:
create a database in mysql - project_management
To start Django Project Clone main branch
After cloning branch add .env file with following variables
ENGINE=django.db.backends.mysql
DATABASE=project_management
USER=root
HOST=localhost
PORT=3306
PASSWORD=


Step 2:
follow the following commands 
>python -m venv venv
>venv/Scripts/activate
(venv)>pip install -r requirements.txt
(venv)>python manage.py makemigrations
(venv)>python manage.py migrate
(venv)>python manage.py createsuperadmin
(venv)>python manage.py runserver

create super admin user and login to "http://127.0.0.1:8000/admin"
add one user in employee model using django admin panel

Step 3:
after adding user you can procide with the application
"http://127.0.0.1:8000"
login with the username and password you just created
Enjoy ;-)