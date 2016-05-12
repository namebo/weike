#coding:utf-8
import xadmin
from course.models import *

class ChapterInline(object):
	model = Chapter
	extra = 3

class CourseAdmin(object):
	list_display = ('name','teacherId','state','studentNumber','createDate')
	inlines = [ChapterInline]

class LessonAdmin(object):
        list_display = ('chapterId','name','videoLen')

class ChapterAdmin(object):
	list_display = ('courseId','number','name')

class DatasAdmin(object):
	list_display = ('name','lessonId','Addr')

xadmin.site.register(Course,CourseAdmin)	
xadmin.site.register(Chapter,ChapterAdmin)	
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Datas,DatasAdmin)