from django.db import models
from common.models.base_models import CreatedUpdatedDateModel
from .flow import FLow

class IP(CreatedUpdatedDateModel):
    flow = models.ForeignKey(FLow , on_delete=models.CASCADE)
    ip = models.TextField(blank=False, null=False, default='')
    
    