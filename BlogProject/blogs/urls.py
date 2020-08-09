from django.conf.urls import url
from . import views

app_name = 'blogs'

urlpatterns = [ url(r'^$',views.blog_post,name='blog_post'),
                url(r'^create/$',views.blog_create,name='blog_create'),
                url(r'^(?P<slug>[\w-]+)/$',views.blog_detail,name='blog_detail'),
                
                ]