from django.db import models
from common.models.base_models import CreatedUpdatedDateModel
import random
import string

def generate_random_string():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=16))

key_gen = generate_random_string

class KeyActive(CreatedUpdatedDateModel):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    name = models.CharField(null=False, blank=False, unique=True, default=key_gen)
    key = models.TextField(null=False, blank=False, default=key_gen, unique=True)
    is_login = models.BooleanField(default=False)
    expire = models.DateTimeField(null=True, blank=True)
    project = models.ManyToManyField('flow_manager.Flow', related_name='flow')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        if self.name:
            return self.name
        return str(self.id)