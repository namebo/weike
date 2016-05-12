#coding:utf-8
import os
from WeiKe.settings import MEDIA_ROOT
from django.db import models
from accounts.models import *

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=50,verbose_name=u"课程名字")
	teacherId = models.ForeignKey(Users,related_name='ReUserCourse',verbose_name=u"授课教师")
	picAddr = models.FileField(upload_to='static/images',verbose_name=u"图片地址")
	introduction = models.CharField(max_length=200,verbose_name=u"简介")
	state = models.CharField(default=u"更新中",max_length=50,verbose_name=u"状态")
	studentNumber = models.IntegerField(null=True,blank=True,default=0,verbose_name=u"学员数")
	createDate = models.DateField(auto_now=False,auto_now_add=True,verbose_name=u"创建时间")
	isDown = models.BooleanField(default=False,verbose_name=u"允许下载")
	class Meta:
		verbose_name_plural = verbose_name = u"课程"
		ordering=['-createDate']
		ordering=['name']
	def __unicode__(self):
		return self.name

class Chapter(models.Model):
        courseId = models.ForeignKey(Course,related_name='ReChapterCourse',verbose_name=u"所属课程")
        number = models.IntegerField(verbose_name=u"章节序号")
        name = models.CharField(max_length=50,verbose_name=u"章节名字")
        class Meta:
                verbose_name_plural = verbose_name = u"章节"
		ordering=['courseId__name','number']
#		ordering=['number']
        def __unicode__(self):
                return self.name


class Lesson(models.Model):
	chapterId = models.ForeignKey(Chapter,related_name='ReLessonChapter',verbose_name=u'所属章节')
	number = models.IntegerField(verbose_name=u"课时序号")
	name = models.CharField(max_length=50,verbose_name=u"课时名字")
	videoAddr = models.FileField(upload_to='static/images/video',verbose_name=u"视频地址")
	videoLen = models.CharField(max_length=50,verbose_name=u"视频长度")
        class Meta:
                verbose_name_plural = verbose_name = u"课时"
		ordering=['chapterId__name']
        def __unicode__(self):
                return self.name


	
class CourseStudy(models.Model):
	userId = models.ForeignKey(Users)
	courseId = models.ForeignKey(Course)
	studyTime = models.DateTimeField(auto_now=False,auto_now_add=True)
	isFinished = models.BooleanField(default=False)
	
class LessonStudy(models.Model):
	userId = models.ForeignKey(Users)
	lessonId = models.ForeignKey(Lesson)
	studyTime = models.DateTimeField(auto_now=True,auto_now_add=True)
	isFinished  = models.IntegerField(default=0)
	
	
class Datas(models.Model):
	lessonId = models.ForeignKey(Lesson)
	name = models.CharField(max_length=50,verbose_name=u"资料名称")
	Addr = models.FileField(upload_to='static/data',verbose_name=u"地址")
	createDate = models.DateTimeField(auto_now=False,auto_now_add=True,verbose_name=u"上传时间")
        class Meta:
                verbose_name_plural = verbose_name = u"课时资料"
		ordering=['-createDate']
        def __unicode__(self):
                return self.name

