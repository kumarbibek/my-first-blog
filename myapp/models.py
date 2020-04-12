from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from hitcount.models import HitCountMixin, HitCount
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



"""
class Blog(models.Model):
	

"""
@python_2_unicode_compatible
class Blog(models.Model):
	name=models.ForeignKey(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	slug=models.SlugField(max_length=80)
	description=RichTextUploadingField()
	image=models.ImageField()
	hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
	catagory=models.ForeignKey("Blog_Catagory",on_delete=models.CASCADE)
	created_on=models.DateTimeField(default=timezone.now())
	active=models.BooleanField(default=True)
	def __str__(self):
		return self.title

	#get_absolute_url
	def get_absolute_url(self):
		return reverse("blog_detail", kwargs={"slug": self.slug})

	#get publish_date as date, month and year.
	def datepublished(self):
		return self.created_on.strftime('%b %d %Y')

	def get_pubdate(self):
		return self.created_on.strftime('%d')

	def get_pub_monthyear(self):
		return self.created_on.strftime('%b %Y')
	#publish_date end


class Blog_Catagory(models.Model):
	title=models.CharField(max_length=100)	
	slug=models.SlugField(max_length=80)
	image=models.ImageField(upload_to="catagory/")
	created_on=models.DateTimeField(default=timezone.now())
	active=models.BooleanField(default=True)
	def __str__(self):
		return self.title

	#get_absolute_url
	def get_absolute_url(self):
		return reverse("blog_catagory_detail", kwargs={"slug": self.slug})

	#get publish_date as date, month and year.
	def datepublished(self):
		return self.created_on.strftime('%b %d %Y')

	def get_pubdate(self):
		return self.created_on.strftime('%d')

	def get_pub_monthyear(self):
		return self.created_on.strftime('%b %Y')
	#publish_date end