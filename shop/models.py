from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 255)
	image = models.ImageField()
	description = models.TextField()
	created_at = models.DateTimeField()
	price = models.FloatField()

	def __str__(self):
		return self.title

