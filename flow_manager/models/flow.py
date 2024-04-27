from django.db import models
from common.models.base_models import CreatedUpdatedDateModel
# Create your models here.


class FLow(CreatedUpdatedDateModel):
    name = models.TextField(null=False, blank = False,  unique=True)
    flow_chart = models.JSONField(null=True, blank = True)
    IPScan = models.TextField(null=True, blank =True, default='')
    loop_time = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return str(self.id)