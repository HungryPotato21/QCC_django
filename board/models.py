from django.db import models
from django.utils import timezone
# Create your models here.

class DjangoBoard(models.Model):
    subject = models.CharField(max_length=50,blank=True)
    created_date = models.DateTimeField(default = timezone.now)
    content = models.TextField()
    hits = models.IntegerField(null=True, blank=True)
    