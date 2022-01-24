# Mookit-Downloader
Mookit Downloader is a Django app to download course content from MOOKIT of IIT Kanpur.

## Prerequisites
* Python3.8 or later.
* pip

## Setting Up Django
Django needs to be setup only once, after that all you need to do is start the server to use the app.

1. Clone this repository and navigate to it.

2. Install the dependecies by running `pip install -r requirements.txt` in your shell. This includes Django 4.0.


3. Start a Django project in the cloned repository by running `django-admin startproject myproject .`. _myproject_ can be replaced by any valid python identifier. Although, you’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like _django_ (which will conflict with Django itself) or _test_ (which conflicts with a built-in Python package).

4. In the file `myproject/setting.py`, add `'mookit_downloader'` to the list `INSTALLED_APPS`. The final list looks like this:
  ```python3
  INSTALLED_APPS = [
      'mookit_downloader',
      ...
  ]
  ```

5. In the file `myprojects/urls.py`, add `from django.urls import include` at the top of the file and `path('mookit_downloader/', include('mookit_downloader.urls')),` in the `urlpatterns` list. The final file looks like:
```python3
"""
...
"""
from django.urls import include
...

urlpatterns = [
  path('mookit_downloader/', include('mookit_downloader.urls')),
  ...
]
```

## Running the Application
Django comes with a built-in, light-weight development server which can be used to run the app without setting up a server application.

Just navigate to the project directory and run `python manage.py runserver` in your shell. You would see something like `Starting development server at <URL>`. Open `<URL>/mookit_downloader/` in your favourite browser to use the app.
