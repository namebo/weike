#coding:utf-8
from django.shortcuts import render
from course.models import *
import simplejson
from django.http import HttpResponseRedirect,HttpResponse
from accounts.views import check
from accounts.models import *
from comment.models import *
from django.http import StreamingHttpResponse
import os
import string
import urllib,sys
# Create your views here.

def Index(request):
    template_name = "index.html"
    courseList = Course.objects.all()
    user =  check(request)
    notice = Notice.objects.all()[:8]
    records = Record.objects.all().order_by('-createDate')[:8]
    return render(request,"index.html",locals())

def CourseDetail(request,pk):
    course = Course.objects.get(pk=pk)
    chapters = course.ReChapterCourse.all() 
    teacher = course.teacherId
    user =  check(request)
    lessons=[]
    for chapter in chapters:
        lessons.append(Lesson.objects.filter(chapterId=chapter.id))
    CS = CourseStudy.objects.filter(courseId=course)[:12]
    return render(request,"courseDetail.html",locals())

def LessonDetail(request,pk):
    user =  check(request)
    if not user:
        return HttpResponseRedirect('/accounts/login/',)    
    lesson = Lesson.objects.get(pk=pk)   
    chapter = lesson.chapterId
    course = chapter.courseId
    chapters = course.ReChapterCourse.all() 
    lessons=[]
    comms = Comment.objects.filter(userId=user,lessonId=lesson)
    length = 0
    try :
        CourseStudy.objects.get(userId=user,courseId=course)
    except CourseStudy.DoesNotExist:
        cs  = CourseStudy.objects.create(userId=user,courseId=course)
        cs.save()            
    try :
        l = LessonStudy.objects.get(userId=user,lessonId=lesson)
    except LessonStudy.DoesNotExist:
        l  = LessonStudy.objects.create(userId=user,lessonId=lesson)
        l.isFinished=1
        l.save()            
    else:
        if l.isFinished==0:
            l.isFinished=1
            l.save()
    for chapter in chapters:
        cl =[]
        for l in Lesson.objects.filter(chapterId=chapter.id):
            length = length+1
            try :
                cl.append(LessonStudy.objects.get(userId=user,lessonId=l))
            except LessonStudy.DoesNotExist:
                ls  = LessonStudy.objects.create(userId=user,lessonId=l)
                ls.save()
                cl.append(ls)
        lessons.append(cl)
    datas = Datas.objects.filter(lessonId=lesson)
    action = u'开始学习:'+course.name+u'>>'+chapter.name+u'>>'+lesson.name
    try:
        Record.objects.get(userId=user,action=action)
    except Record.DoesNotExist:        
        record = Record .objects.create(userId=user,action=action)        
        record.save()
    return render(request,"video-js/lessonDetail.html",locals())

def CourseAdd(request):
    result = {}
    if request.POST.has_key('Id'):
        id = request.POST['Id']
        course = Course.objects.get(pk=id)
        user = check(request)
        if CourseStudy.objects.filter(userId=user,courseId=course):
            result=[{'result':u'你已添加该课程！'}]
            result=simplejson.dumps(result)
            return HttpResponse(result,mimetype='applicaton/javascript')
        else:
            CS = CourseStudy.objects.create(userId=user,courseId=course)
            CS.save()
            course.studentNumber = course.studentNumber +1
            course.save()
            for chapters in course.ReChapterCourse.all() :
                for lesson in chapters.ReLessonChapter.all():
                    LS = LessonStudy.objects.create(userId=user,lessonId=lesson)
                    LS.save()
            result=[{'result':'successed'}]
            result=simplejson.dumps(result)
            return HttpResponse(result,mimetype='applicaton/javascript')
    result=[{'result':u'添加失败，未知错误！'}]
    result=simplejson.dumps(result)
    return HttpResponse(result,mimetype='applicaton/javascript')

def GetLesson(request):
    result = {}
    if request.POST.has_key('name'):
        name = request.POST['name'] 
        result=[{u'gao':u'你号'},{u'bo':'我好'}]
        result=simplejson.dumps(result)
    if request.POST.has_key('password'):
        password = request.POST['password']
        result="0"
        result=simplejson.dumps(result)
    return HttpResponse(result,mimetype='applicaton/javascript')

def Read(request):
    result = {}
    user = check(request)    
    if request.POST.has_key('id'):
        lId = request.POST['id'] 
        lesson = Lesson.objects.get(pk=lId)
        print lesson
        print user
        ls = LessonStudy.objects.get(userId=user,lessonId=lesson)
        print ls.isFinished
        ls.isFinished = 2
        ls.save()
        result = [{'result':'successed'}]
        result=simplejson.dumps(result)
    return HttpResponse(result,mimetype='applicaton/javascript')

def Download(request,pk):
    # do something...
    user = check(request)    
    data = Datas.objects.get(pk=pk)
    def file_iterator(file_name, chunk_size=1024):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name = data.Addr.url
    the_file_name = urllib.unquote(the_file_name)
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    record = Record .objects.create(userId=user)        
    record.action = u'下载了:'+data.name
    record.save()
    return response


def DownloadVideo(request,pk):
    # do something...
    user = check(request)    
    data = Lesson.objects.get(pk=pk)
    def file_iterator(file_name, chunk_size=1024):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name = data.videoAddr.url
    the_file_name = urllib.unquote(the_file_name)
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    record = Record .objects.create(userId=user)        
    record.action = u'下载了:'+data.name
    record.save()
    return response
