from django.conf.urls import patterns, include, url
from comment import views

urlpatterns = patterns('',
	url(r'List$',views.List,name="List"),
	url(r'Comm$',views.Comm,name="Comm"),	
	url(r'log$',views.log,name="log"),
)
