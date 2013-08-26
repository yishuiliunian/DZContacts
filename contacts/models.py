from django.db import models

# Create your models here.
class DZContact(models.Model):
	firstName = models.CharField(max_length = 30)
	midleName = models.CharField(max_length = 30)
	lastName = models.CharField(max_length = 30)



