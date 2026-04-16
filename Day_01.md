# Creating first Website/Project

project -> website
web app -> application

one website can have any number of applications

## e-magazine

- News update
- Events
- Articles
- Quiz
- Chat
- ....

Django is an application in itself.

With the help of django you can create a project instance

# How to use Django?

Django is a framework. You can create your project with simple command

Create a workspace directory

On cmd (on windows), or terminal (on mac) and type following command.

go to your workspace directory(with the held of cd command we change folder)

> django-admin startproject firstproject

" it created project instance which means a folder with files created and necessary default settings all done with a small ready project"

Now you can check created project on IDE
Project name can be anything but django or test.

# Project Directory

Inside (parent)project folder
- (child)project folder
    - \__init\__.py
    - settings.py
    - urls.py
    - wsgi.py
    - asgi.py
- manage.py

# About Child project files

__init__.py is an empty file, its presence make the folder as python package

settings.py contains project related setting statements

urls.py contains url patterns of web pages

wsgi.py is webserver gateway interface, it is a special file, no modification in the file is required

(updated version of wsgi)
asgi.py is asynchronous server gateway interface. Like wsgi.py, it describes a common interface between a python web app and the web server.

manage.py is a program to do some initial stuff. Never edit this file.

# How to run server?

Django comes with a webserver for testing your project in development phase.

Default port number is 8000

> python manage.py runserver [port no]

# Test run your project

Yes you have created your first project, now its time to test it.

Open browser, type url
http://127.0.0.1:8000

or
http://localhost:8000

# Default database

Sqlite is default inbuilt database but you can use (mysql,oracle etc.)anydatabase management syatem