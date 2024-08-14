from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class PhoneNumberField(models.IntegerField):
	default_validators = [
		MinValueValidator(1000000000),
		MaxValueValidator(9999999999),
		RegexValidator(r'^[0-9]*$', 'only numeric characters are allowed.'),
	]

class Contact(models.Model):
	name = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	phone = PhoneNumberField(null = True)
	query = models.TextField()
	
	def __str__(self):
		return f"{self.name}"

class Register(models.Model):
	username = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	password = models.CharField(max_length = 255)
