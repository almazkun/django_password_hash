# Hashed password

```bash
git clone git@github.com:almazkun/django_password_hash.git
cd django_password_hash
pip3 install pipenv
pipenv install
pipenv run python3 manage.py migrate
pipenv run python3 manage.py runserver
```
In another terminal:
```bash
curl -d "username=asdasdas&password=password" -X POST http://localhost:8000/create_user/
curl -d "username=username&password1=very_strong&password2=very_strong" -X POST http://localhost:8000/create_user_form/
```
This should produce the following:
```log
Django version 4.0.3, using settings 'settings.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

From post: asdasdas password
From DB: asdasdas pbkdf2_sha256$320000$0YUZpDqMt2r0FkH62KEbCi$ooJjQdlaNzK5Z2DnIw8Mb/uBxI0R3AS5bIhGGQ+Nkz8=

[23/Mar/2022 01:28:49] "POST /create_user/ HTTP/1.1" 302 0

From post: username very_strong
From DB: username pbkdf2_sha256$320000$6cx7IueCHO2TjRnOwc5hmY$23qKXa4BIlrRPH/Q6KRDCA6ryMJDZDv7xtDuqlT3M38=

[23/Mar/2022 01:28:51] "POST /create_user_form/ HTTP/1.1" 302 0
```

Personally, I think you should user Forms for User creation. It will take care of hashing and validation and much more. Added an example. 


# django_template
This is a django started template

## Changes
1. Docker dev and prod setup
2. Templates 
3. Bootstrap 5
4. Logging
5. Pipenv for environment
6. .env file
7. Github Actions
8. Static files 
9. Docker-compose


## Install
1. `git clone https://github.com/almazkun/django_template.git`
2. `pipenv install`
3. `pipenv shell`
4. `python manage.py startapp <app_name>`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py runserver`