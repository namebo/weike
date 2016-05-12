#coding:utf-8
import os
from WeiKe.settings import MEDIA_ROOT
from django.db import models


# Create your models here.

	
class Classes(models.Model):
	className = models.CharField(max_length=100,verbose_name=u"班级")
	createDate = models.DateTimeField(auto_now=False,auto_now_add=True,verbose_name=u"创建时间")
        class Meta:
                verbose_name_plural = verbose_name = u"班级"
        def __unicode__(self):
                return self.className


class Users(models.Model):
	username = models.CharField(max_length=50,verbose_name=u"账号")
	password = models.CharField(max_length=50,verbose_name=u"密码")
	name = models.CharField(max_length=50,verbose_name=u"姓名")
	classname = models.ForeignKey(Classes,related_name='ReUserClass',verbose_name=u'班级')
	sex = models.CharField(max_length=50,null=True,blank=True,verbose_name=u"性别")
	phone = models.CharField(max_length=50,null=True,blank=True,verbose_name=u"手机号码")
	title = models.CharField(max_length=50,null=True,blank=True,verbose_name=u"称号")
	headAddr = models.FileField(upload_to='./static/images/',null=True,blank=True,verbose_name=u"头像地址")
	introduce = models.CharField(max_length=100,null=True,blank=True,verbose_name=u"简介")
	mail = models.CharField(max_length=100,null=True,blank=True,verbose_name=u"邮箱")
	isStudent = models.BooleanField(default=False,verbose_name=u"学生")
	isTeacher = models.BooleanField(default=False,verbose_name=u"老师")
#	isStaff = models.BooleanField(default=False,verbose_name=u"管理员")
        class Meta:
                verbose_name_plural = verbose_name = u"用户"
        def __unicode__(self):
                return self.name

class Record(models.Model):
	userId = models.ForeignKey(Users,related_name='ReRecordUser',verbose_name=u'姓名')
	action = models.CharField(max_length=100,null=True,blank=True,verbose_name=u"动作")
	createDate = models.DateTimeField(auto_now=False,auto_now_add=True,verbose_name=u"创建时间")
        class Meta:
                verbose_name_plural = verbose_name = u"操作记录"
        def __unicode__(self):
                return self.userId	



