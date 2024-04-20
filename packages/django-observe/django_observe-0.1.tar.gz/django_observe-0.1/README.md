# Django Observe

## What this is
This is a server-side-only Django app that provides visualizations for your routes, how often they are hit, and their status codes.

The goal is to be a minimal setup solution for getting basic traffic information for low-scale websites.

## What this isn't
This isn't a replacement for true monitoring. Nor should it ever be used for a website with any level of scale.

### Considerations
This app lives in the middleware and creates a row in a database for each request. It does not currently have any database cleanup, so if you have 1000 requests per day, you'll be adding 1000 rows to a database table per day. 

## Usage
### How to Install
To install this app into your Django project:
1. `pip install django-observe`
2. Add `"django_observe"` to your `INSTALLED_APPS`
3. Add `"django_observe.middleware.MonitoringMiddleware"` to your MIDDLEWARE
4. Add `path("observe", include("django_observe.urls"))` to your base routes. (Change "observe" to whatever path you want it at)
5. View the new route as a staff user

### Configuration
You can set `DJANGO_OBSERVE_SAMPLE_RATE` in your settings to a value between `0` and `1` to set the sampling rate. 


## Supported versions
This has only been tested on the following versions:

Django 5.0
Python 3.10