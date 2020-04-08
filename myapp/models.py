from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# Create your models here.



"""
class Blog(models.Model):
	

"""
class Blog(models.Model):
	name=models.ForeignKey(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	slug=models.SlugField(max_length=80)
	description=models.TextField(max_length=1000)
	image=models.ImageField()
	catagory=models.CharField(max_length=30)
	created_on=models.DateTimeField(default=timezone.now())
	def __str__(self):
		return self.title

	#get_absolute_url
	def get_absolute_url(self):
		return reverse("url4", kwargs={"slug": self.slug})

	#get publish_date as date, month and year.
	def datepublished(self):
		return self.created_on.strftime('%b %d %Y')

	def get_pubdate(self):
		return self.created_on.strftime('%d')

	def get_pub_monthyear(self):
		return self.created_on.strftime('%b %Y')
	#publish_date end