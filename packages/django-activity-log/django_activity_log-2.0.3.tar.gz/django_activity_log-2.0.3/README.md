# django-activity-log

Forked from : 
[scailer/django-user-activity-log](https://github.com/scailer/django-user-activity-log)
__________________________________________________________
## Owner's Expressions :
This django app intended for writing HTTP log to database and/or watch last user activity.

Features:
- DB router for writing logs to another database.
- Filters for ignoring some queries by URL, HTTP methods and response codes.
- Saving anonymous activity as fake user.
- Autocreation log DB (for postgresql)

Install:

[deprecated]:

$ pip install django-user-activity-log 

[new library]:
```
pip install django-activity-log 
```

settings.py:


```python
INSTALLED_APPS = (
    ...
    'activity_log',
)

MIDDLEWARE_CLASSES = (
    ...
    'activity_log.middleware.ActivityLogMiddleware',
)

# For writing log to another DB

DATABASE_ROUTERS = ['activity_log.router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {'activity_log': 'logs'}

# If you set up DATABASE_APPS_MAPPING, but don't set related value in
# DATABASES, it will created automatically using "default" DB settings
# as example.
DATABASES = {
    'logs': {
        ...
    },
}

# Create DB automatically (for postgres, and may be mysql).
# We create log database automatically using raw SQL in pre_migrate signal.
# You must insure, that DB user has permissions for creation databases. 
# Tested only for postgresql
ACTIVITYLOG_AUTOCREATE_DB = False

# App settings

# Log anonimus actions?
ACTIVITYLOG_ANONIMOUS = True

# Update last activity datetime in user profile. Needs updates for user model.
ACTIVITYLOG_LAST_ACTIVITY = True

# Only this methods will be logged
ACTIVITYLOG_METHODS = ('POST', 'GET')

# List of response statuses, which logged. By default - all logged.
# Don't use with ACTIVITYLOG_EXCLUDE_STATUSES
ACTIVITYLOG_STATUSES = (200, )

# List of response statuses, which ignores. Don't use with ACTIVITYLOG_STATUSES
# ACTIVITYLOG_EXCLUDE_STATUSES = (302, )

# URL substrings, which ignores
ACTIVITYLOG_EXCLUDE_URLS = ('/admin/activity_log/activitylog', )
```

account/models.py:

```python
from django.contrib.auth.models import AbstractUser
from activity_log.models import UserMixin

# Only for LAST_ACTIVITY = True
class User(AbstractUser, UserMixin):
    pass
```

$ python manage.py migrate & python manage.py migrate --database=logs

If you use ACTIVITYLOG_AUTOCREATE_DB migrations to logs database 
will be run automatically.

__________________________________________________________
## Changelogs of this fork :

#### 1. ```ACTIVITYLOG_MAIN_IP_KEY_VALUE```:
You can set this string in the settings.py file. When you have a specific CDN or there are changes in headers of requests from the user on the frontend side, this key value takes the highest priority to set the IP address from the headers.

#### 2. ```ACTIVITYLOG_MAXIMUM_RECORD_SIZE```:
You can set this integer in the settings.py file. 
This constraint controls the number of saved records by removing the oldest records.

#### 3. ```EXCLUDE_IP_LIST```:
You can set this list in the settings.py file. 
This is a list of IP addresses that you do not want to log.

#### 4. ```IP_ADDRESS_HEADERS```:
I changed the priority to find the IP address better. When you have a CDN, the previous library saves the IP address of the CDN, which is not useful.

#### 5. ```headers```:
There is a new field in the changelog model that saves headers of requests from the user as a pretty string.

#### 6. ```payload```:
There is a new field in the changelog model that saves the payload of requests from the user as a pretty string.

#### 7. Test on django version 4.0.1:
It works well with Django version 4.0.1.

#### 8. change migration files:
Delete old migrations and create one file to migrate models of this library.

#### 9. IP Management:
In admin panel , Model BlackListIPAdress you can archive or block every ip address would you like with its network address or not.

Repository : 
[HosseinSayyedMousavi/django-user-activity-log](https://github.com/HosseinSayyedMousavi/django-user-activity-log/)