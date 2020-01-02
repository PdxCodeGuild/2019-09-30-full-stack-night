from django.db import models

class Url(models.Model):
    url = models.CharField(max_length = 500)
    url_hash = models.CharField(max_length = 100)

    def __str__(self):
        return self.url
