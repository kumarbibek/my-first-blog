"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from myapp import views 
from myapp.views import (homeblog,homeblog_details) 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^blog/', views.blog,name="url2"),
    url(r'^blog_search/', views.blog_search,name="blog_search"),
    url(r'^test/', homeblog.as_view(),name="url3"),
    url(r'^test_detail/(?P<slug>[-\w]+)/', homeblog_details.as_view(),name="blog_detail"),
    url('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    url('ckeditor/', include('ckeditor_uploader.urls')),
] 
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)