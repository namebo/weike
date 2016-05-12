#coding:utf-8
import xadmin
from accounts.models import *

class UsersAdmin(object):
	list_display = ('username','name','sex','classname')

class RecordAdmin(object):
	list_display = ('userId','action','createDate')

class ClassesAdmin(object):
	list_display = ('className','createDate')

xadmin.site.register(Classes,ClassesAdmin)	
xadmin.site.register(Users,UsersAdmin)	
xadmin.site.register(Record,RecordAdmin)