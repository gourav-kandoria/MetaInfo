from django.db import models as m

# Create your models here.

class MetaData(m.Model):
  url = m.CharField(max_length=500, primary_key=True)
  title = m.CharField(max_length=500)
  description = m.CharField(max_length=500, null=True, blank=True)
  keyWords = m.CharField(max_length=1000, null=True, blank=True)