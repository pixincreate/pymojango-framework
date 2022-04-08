# About: framework-pymojango
Integration of Django with MongoDB using PyMongo later implement REST API to talk to frontend of the code.  
  
## Pre-requisites:
- command-prompt
- [python 3.6 or later](https://www.python.org/downloads/)
- An IDE (PyCharm preferred)
- Patience

## Getting-Started:
- Open Command-Prompt by typing CMD on **RUN**(Win_Key + R) or in your preferred dir.
- `mkdir <folder-name>`  (give a folder-name and this is optional)
- `django-admin startproject <project-name>`  (start django project)
- `cd <project-name>`  (access the dir to start working)
- Create a virtual environment by typing `python -m venv <environment-name>`
- Activate the `environment` by typing `venv\scripts\activate`. You'll see `(environment-name)` written in before the path in **cmd**.
- After activating the `environment`, install the [`requirements.txt`](https://github.com/pixincreate/framework-pymojango/blob/main/requirements.txt) by typing `pip install -r requirements.txt`.
- `python manage.py startapp <app-name>`  (create an app)
- `type nul> utils.py` (make sure that `utils.py` file exists where `manage.py` exist)
- `type nul> readme.md` (to keep a documentation of what you're doing)
- `git init`  (initialise git repo)
- Put the following commands to set-up a git-repo on GitHub (in case the repo doesn't exist in prior)
  ```commandline
    echo "# <repo-name>" >> README.md           :: Creted a readme.md file with repo-name in 1st line.
    git init
    git add README.md                           :: Tracks the file
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/<user-name>>/<git-repo-name>.git
    git push -u origin main                     :: Pushes the commits to repo
    ``` 
- Put the following commands to push to git-repo on GitHub (in case the repo does exist in prior)
    ```commandline
    git remote add origin https://github.com/pixincreate/blah.git
    git branch -M main
    git push -u origin main                     :: Pushes the commits to repo
    ```

## Current Project Structure:
```
<framework-pymojango> [dir]
├ .git [dir]
├ .idea [dir]
├ app [dir]	# you can create n-number of apps
|   ├ migrations [dir]
|   ├ __init__.py
|   ├ admin.py
|   ├ apps.py
|   ├ models.py
|   ├ tests.py
|   ├ urls.py
|   └ views.py
├ framework [dir]
|   ├ __init__.py
|   ├ asgi.py
|   ├ settings.py	# Comment the DATABSES section here
|   ├ urls.py
|   └ wsgi.py
├ inputs [dir]
|   ├ config.py
|   ├ schema.py
|   └ user_inputs.py
├ test [dir]
|   └ this_code_here_works.py
├ .gitignore
├ LICENSE
├ manage.py
├ readme.md
├ requirements.txt
├ basic-architecture-for-integration-with-react.png
└ utils.py

```

### [NOTE:] 
As previously observed, many issues arised upon execution [_Latest fixes are not tested_]. However, `this_code_here_works.py` situated in `./test` folder that has everything **unified** runs without any hassle or error. 

## References:
1. [Schema Validation Docuentation](https://docs.mongodb.com/manual/core/schema-validation/)
2. [Schema Validation in pymongo query on stackoverflow](https://stackoverflow.com/questions/46569262/does-pymongo-have-validation-rules-built-in/51520384#51520384)
3. [Django Rest Framework](https://www.django-rest-framework.org/)
4. [Django tutorial for Beginners](https://data-flair.training/blogs/django-tutorial/)
5. [MongoDB Integration with Django](https://www.mongodb.com/compatibility/mongodb-and-django)
6. [Connect Django with ReactJS - Geeks for Geeks](https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/)
7. [Django REST Framework by Geeky Shows(Hindi) | YouTube](https://www.youtube.com/playlist?list=PLbGui_ZYuhijTKyrlu-0g5GcP9nUp_HlN)
8. [Does Pymongo have validation rules built in?](https://stackoverflow.com/questions/46569262/does-pymongo-have-validation-rules-built-in)
9. [Defining Data Schema using Pymongo](https://www.mongodb.com/community/forums/t/defining-data-schema-using-pymongo/8533/2)
10. [MongoDB Data Validator: How to use the JSON Schema Validator](https://www.percona.com/blog/2018/08/16/mongodb-how-to-use-json-schema-validator/)

