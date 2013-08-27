from django.db import models

# Create your models here.
class DZContact(models.Model):
	firstName = models.CharField(max_length = 30)
	midleName = models.CharField(max_length = 30)
	lastName = models.CharField(max_length = 30)
	phoneNumber = models.CharField(max_length = 14)
	email = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.firstName + ' ' + self.midleName + ' ' + self.lastName
	class Meta:
		ordering = ['firstName']

class DZUser(models.Model):
	guid = models.CharField(max_length = 36)


