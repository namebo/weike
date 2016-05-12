#coding:utf-8
import os
from WeiKe.settings import MEDIA_ROOT
from django.db import models
from accounts.models import *
from course.models import *

# Create your models here.

class Comment(models.Model):
	userId = models.ForeignKey(Users,related_name='ReUserComm',verbose_name=u"发表评论的人")
	courseId = models.ForeignKey(Course,null=True,blank=True,related_name='ReCourseComm',verbose_name=u"评论的课程")
	lessonId = models.ForeignKey(Lesson,null=True,blank=True,related_name='ReLessonComm',verbose_name=u"评论的课时")
	comment = models.CharField(max_length=500,verbose_name=u"评论内容")
	createDate = models.DateTimeField(auto_now=False,auto_now_add=True,verbose_name=u"发表时间")
	class Meta:
		verbose_name_plural = verbose_name = u"评论"
		ordering=['-createDate']
		ordering=['userId']
	def __unicode__(self):
		return self.comment


class ReComment(models.Model):
	fUserId = models.ForeignKey(Users,related_name='RefUserComm',verbose_name=u"发表评论的人")
	tUserId = models.ForeignKey(Users,related_name='RetUserComm',verbose_name=u"被评论的人")
	courseId = models.ForeignKey(Course,null=True,blank=True,related_name='ReCourseReComm',verbose_name=u"评论的课程")
	lessonId = models.ForeignKey(Lesson,null=True,blank=True,related_name='ReLessonReComm',verbose_name=u"评论的课时")
	toComment = models.ForeignKey(Comment,verbose_name=u"回复的评论")
	comment = models.CharField(max_length=500,verbose_name=u"评论内容")
	createDate = models.DateTimeField(auto_now=False,auto_now_add=True,verbose_name=u"发表时间")
	class Meta:
		verbose_name_plural = verbose_name = u"回复评论"
		ordering=['-createDate']
		ordering=['fUserId']
	def __unicode__(self):
		return self.comment


class Notice(models.Model):
	UserId = models.ForeignKey(Users,related_name='RefUserNotice',verbose_name=u"发公告的人")
	notice = models.CharField(max_length=500,verbose_name=u"公告内容")
	createDate = models.DateTimeField(auto_now=False,auto_now_add=True,verbose_name=u"发表时间")
	class Meta:
		verbose_name_plural = verbose_name = u"公告"
		ordering=['-createDate']
		ordering=['UserId']
	def __unicode__(self):
		return self.notice