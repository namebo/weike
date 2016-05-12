from django.conf.urls import patterns, include, url
from django.contrib import admin
import xadmin
from course.models import *
from django.contrib.auth import urls as auth_urls
from course import views
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',  views.Index,name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^xadmin/', include(xadmin.site.urls),name='xadmin'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^course/', include('course.urls'),name='course'),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^comment/',include('comment.urls')),
)
