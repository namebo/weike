from django.conf.urls import patterns, include, url
from accounts import views

urlpatterns = patterns('',
	url(r'^login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^register/$',views.register,name='register'),
	url(r'^information/$',views.information,name='information'),	
	url(r'^learn/$',views.learn,name='learn'),	
	url(r'^teacher/$',views.teacher,name='teacher'),	
)
