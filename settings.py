from dotenv import load_dotenv
import os
load_dotenv()
engine = os.getenv("engine")
host = os.getenv("host")
port = os.getenv("port")
name = os.getenv("name")
user = os.getenv("user")
password  = os.getenv("password")



DATABASES = {
    'default': {
        'ENGINE': 'engine',
        'HOST': 'host',
        'PORT': 'port',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password ',
    }
}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
