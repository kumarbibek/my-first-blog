from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from myapp.models import Blog
from hitcount.views import HitCountDetailView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

#class myblog(ListView):
 
def home(request):
	return render(request,"index.html")


def blog(request):
	return render(request,"blog.html")
 
class homeblog(ListView):
	models = Blog
	queryset = Blog.objects.all()
	template_name = "myapp/blog_list.html"
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super(homeblog, self).get_context_data(**kwargs)
		context.update({
    	'popular_posts': Blog.objects.order_by('-hit_count_generic__hits')[:4],
		})
		return context


class homeblog_details(HitCountDetailView):
	models = Blog
	queryset = Blog.objects.all()
	#lookup_field = "slug"
	template_name = "myapp/blog_detail.html"
	count_hit = True

	def get_context_data(self, **kwargs):
		context = super(homeblog_details, self).get_context_data(**kwargs)
		context.update({
    	'popular_posts': Blog.objects.order_by('-hit_count_generic__hits')[:4],
		})
		return context
		

#search_for_all_blogs
def blog_search(request):
    queryset = None
    query = request.GET.get('q')
    if query:
        if query.startswith('#'):
            queryset = Blog.objects.all().filter(
                Q(tags__icontains=query)
                ).distinct()
        else:
            queryset = Blog.objects.all().filter(
                Q(title__icontains=query)|
                Q(slug__icontains=query)|
                Q(description__icontains=query)
                ).distinct()

    context = {
        'blogs': queryset
    }
    return render(request, "myapp/search.html", context)
