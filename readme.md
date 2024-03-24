
# Django Framwork

A brief description of what this project does and who it's for


## Python Setup

Check python version

```python
python
```
or 

```python
py --version
```
check the installed package
```python
pip freeze
```


## Django Setup

Installed Django

```python
pip install django
```
or 
```python
pip i django
```

Create a Django Project
```python
djano-admin startproject <ProjectName>
```

Navigae to your project directory
```bash
cd <ProjectDirectory>
```

Run Server
```python
python manage.py runserver
```

Run Server on Specific port if you want..
```python
python manage.py runserver <YOUR_PORT_NUMBER>
```


# Project Structure

See admin panel on browser once server runs
`http://127.0.0.1:8000/admin` if you are using custom port replace   `8000` with your port number
- This admin panel is created by default.

## /template
- Created by you.
- This directory is used to store HTML templates for the project. It contains files that define the structure and layout of web pages.

## /static
- Created by you.
- The static directory is used to store static files such as CSS, JavaScript, images, and other resources that are served directly to the web browser.

## /media
- Created by you.
- This directory is used to store user-uploaded files such as images, videos, and other media assets.

## /manage.py
-  By default.
- The manage.py file is a command-line utility that helps with various aspects of Django project management, including running development servers, creating migrations, and more.

## /db.sqlite3
- By default.
- This file contains the SQLite database for the project, which is the default database used by Django for local development.

## /<PROJECT_NAME>

- By default.
- This represents the main directory of the Django project, containing settings, URLs, and other configurations.
- It contains These file:

- `__init__.py` This file is required to treat the directory as a package, allowing for the import of other modules within the project
- `settings.py` This file includes all the project settings, such as database configurations, middleware settings, installed apps, static files setup, and more.
- `urls.py` URLs.py contains the URL patterns for the project, mapping the paths to the views within the project.
- `wsgi.py` WSGI (Web Server Gateway Interface) is an entry-point for the web servers to serve the project. This file enables the project to be deployed on WSGI-compliant servers
- `asgi.py` ASGI (Asynchronous Server Gateway Interface) is used for handling asynchronous code and allows Django to communicate with web servers and other protocols that support asynchronous Python.
- `/__pycache__`This directory contains Python bytecode cache files, which are automatically generated and used by Python to optimize performance during subsequent runs of the application.








# Django Project `settings.py` File Documentation

## Introduction
The `settings.py` file in a Django project contains all the project settings and configurations. It is a crucial file where various parameters such as database settings, middleware configurations, installed apps, static files setup, and more are defined.

## File Structure
Within the `settings.py` file, you will find the following key sections:

1. **Basic Configuration:**
   - This section includes essential project configurations like `DEBUG` mode, `ALLOWED_HOSTS`, and project's `SECRET_KEY`.

2. **Database Configuration:**
   - Contains database-related settings such as `DATABASES` dictionary with details like `ENGINE`, `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`, etc.

3. **Apps Configuration:**
   - Defines the list of installed apps for the project in the `INSTALLED_APPS` setting.

4. **Middleware Configuration:**
   - Lists the middleware classes that Django will use to process requests in the `MIDDLEWARE` setting.

5. **Static Files Configuration:**
   - Includes settings related to serving static files like `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS`.

## Code Reference
Here is a basic code reference illustrating a sample `settings.py` file structure:

```python
"""
Django settings for wscubetech project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g0na$&eay@bqc)ytq5=xkmwpe0-*h2nulm+%&_*h$d*qcic_b2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wscubetech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wscubetech.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

```
## Database migration