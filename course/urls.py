from django.conf.urls import patterns, include, url
from course import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$',views.CourseDetail,name='CourseDetail'),
    url(r'^lesson/(?P<pk>\d+)$',views.LessonDetail,name='LessonDetail'),
    url(r'CourseAdd$',views.CourseAdd,name="CourseAdd"),
    url(r'GetLesson$',views.GetLesson,name="GetLesson"),
    url(r'Read$',views.Read,name="Read"),    
    url(r'Download/(?P<pk>\d+)$',views.Download,name="Download"),    
    url(r'DownloadVideo/(?P<pk>\d+)$',views.DownloadVideo,name="DownloadVideo"),        
)
