from django.db import models
from common.models import CreatedUpdatedDateModel
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser, CreatedUpdatedDateModel):
    ROLE_CHOICES = (("user", "User"), ("manager", "Manager"))
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    type = models.CharField(choices=ROLE_CHOICES)
    cover_img = models.ImageField(
        upload_to="cover_img/", height_field=None, width_field=None, max_length=100
    )

User.groups.related_name = 'authen_user_groups'
User.user_permissions.related_name = 'authen_user_permissions'
AbstractUser.groups.related_name = 'auth_user_groups'
AbstractUser.user_permissions.related_name = 'auth_user_permissions'