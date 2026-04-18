# Creating first web app

## Web Apps

You can create any number of web apps in a website.

## Steps to perform

1.  **Create project** (skip if already created)
    ```bash
    django-admin startproject firstproject
    ```
2.  **Create web app**
    ```bash
    python manage.py startapp testapp
    ```
    > **Note:** You can choose any name for your app. Run this command from inside the parent `firstproject` folder.

3.  **Update `settings.py`**
    In child project directory
     (its read by webserver to know the configuration setting of our website)

    Make an entry for this app.

    ```python
    INSTALLED_APPS = [
        'testapp',
        'django.contrib.admin',
        # ...
    ]
    ```

## App directory structure

```
firstproject/
├── Testapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── firstproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

