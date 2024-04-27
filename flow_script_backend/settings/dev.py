from .base import *
from dotenv import load_dotenv

load_dotenv()  

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),  #
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': '5432',
    }
}
