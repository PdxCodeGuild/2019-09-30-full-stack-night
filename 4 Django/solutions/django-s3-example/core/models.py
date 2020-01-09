from django.db import models
from django.contrib.auth import get_user_model

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add = True)
    file = models.FileField()
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    
