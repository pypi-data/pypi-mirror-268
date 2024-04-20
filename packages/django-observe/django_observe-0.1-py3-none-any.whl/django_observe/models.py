from django.db import models


class Event(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=256)
    status_code = models.IntegerField()
    remote_addr = models.CharField(max_length=46)
    user_agent = models.CharField(max_length=200)
    timestamp = models.DateTimeField(db_index=True)
