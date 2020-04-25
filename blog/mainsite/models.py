from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	body = models.TextField()
	pub_data = models.DateTimeField(default=timezone.now)

class Meta:
	ordering = ('-pub_data',)

def __str__(self):
	return self.title