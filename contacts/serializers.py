from django.forms import widgets
from rest_framework import serializers
from contacts.models import DZContact

class DZContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = DZContact
		fields = ('firstName', 'midleName', 'lastName')





