#coding:utf-8
from django.shortcuts import render
from course.models import *
import simplejson
from django.http import HttpResponseRedirect,HttpResponse
from accounts.views import check
from accounts.models import *
from course.models import *
from comment.models import *
import json
import time
import datetime

 
class JsonResponse(HttpResponse):
    def __init__(self,
            content={},
            mimetype=None,
            status=None,
            content_type='application/json'):
 
        super(JsonResponse, self).__init__(
            json.dumps(content),
            mimetype=mimetype,
            status=status,
            content_type=content_type)

def List(request):
	result = []
	user = check(request)    
	if request.POST.has_key('id'):
		lessonId = request.POST['id'] 
		lesson = Lesson.objects.get(pk=lessonId)
		comms = Comment.objects.filter(lessonId=lesson).order_by('-createDate')[:20]
		for comm in comms:
			time = datetime.datetime.strftime(comm.createDate,'%Y-%m-%d %H:%M:%S')
			data={'comment':comm.comment,'user':comm.userId.name,'userId':comm.userId.id,'time':time}
			result.append(data)
	return JsonResponse(result)


def Comm(request):
	result = {}
	user = check(request)    
	if request.POST.has_key('lessonId'):
		lessonId = request.POST['lessonId'] 
		lesson = Lesson.objects.get(pk=lessonId)
	if request.POST.has_key('text'):
		text = request.POST['text']
		comment = Comment.objects.create(userId=user,lessonId=lesson)
		print comment
		comment.comment = text
		comment.save()
		result = [{'result':'successed'}]
		result=simplejson.dumps(result)
	return HttpResponse(result,mimetype='applicaton/javascript')


def log(request):
	result=[{'result':'fail'}]
	print request.GET
	if request.GET.has_key('username'):
		username = request.GET['username']
	else:
		result=[{'result':'fail1'}]
	if request.GET.has_key('password'):
		password = request.GET['password']
	else:
		result=[{'result':'fail2'}]	
	print username	
	print password
	if username==password:
		result=[{'result':'successed'}]	
	return HttpResponse(result,mimetype='applicaton/javascript')