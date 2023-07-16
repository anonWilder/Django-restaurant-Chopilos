from django.db import models

# Create your models here.

#ABOUT PAGE TEXT
class AboutSection(models.Model):
    #title = models.CharField(max_length=200)
    content = models.TextField()
#END