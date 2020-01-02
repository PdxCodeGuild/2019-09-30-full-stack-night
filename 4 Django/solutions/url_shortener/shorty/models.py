from django.db import models
from datetime import datetime

class Url(models.Model):
    url = models.CharField(max_length=200)
    url_hash = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=datetime.now)
    clicks = models.IntegerField(default=0)
    repeat_addition = models.IntegerField(default=0)
    last_ip = models.CharField(default='', max_length=20)

    def __str__(self):
        return self.url_hash

