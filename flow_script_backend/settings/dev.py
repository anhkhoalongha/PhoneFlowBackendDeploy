from .base import *
from dotenv import load_dotenv

load_dotenv()  

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': 'postgres.yquarzfbjstjxaofgqnp',
        'PASSWORD': os.getenv("DATABASE_PASSWORD"), #
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
        'PORT': '5432',
    }
}