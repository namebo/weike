#coding:utf-8
import xadmin
from comment.models import *


class NoticeAdmin(object):
	list_display = ('UserId','notice','createDate')

xadmin.site.register(Notice,NoticeAdmin)	

xadmin.site.register(Comment)	