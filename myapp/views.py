from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from myapp.models import Blog
# Create your views here.

#class myblog(ListView):
 
def home(request):
	return render(request,"index.html")


def blog(request):
	return render(request,"blog.html")
 
class homeblog(ListView):
	models = Blog
	queryset = Blog.objects.all()
	template_name = "myapp/test2.html"


class homeblog_details(DetailView):
	models = Blog
	queryset = Blog.objects.all()
	#lookup_field = "slug"
	template_name = "myapp/test2_detail.html"
	"""docstring for ClassName"""
	"""def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg"""
		
