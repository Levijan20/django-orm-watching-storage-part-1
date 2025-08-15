from dotenv import load_dotenv
import os
load_dotenv()
Engine = os.getenv("engine")
Host = os.getenv("host")
Port = os.getenv("port")
Name = os.getenv("name")
User = os.getenv("user")
Password  = os.getenv("password")



DATABASES = {
    'default': {
        'ENGINE': 'Engine',
        'HOST': 'Host',
        'PORT': 'Port',
        'NAME': 'Name',
        'USER': 'User',
        'PASSWORD': 'Password ',
    }
}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
