#coding: utf-8
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import *
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from accounts.models import *
from course.models import *
import simplejson

def login(request):
	errors=""
	user =  check(request)
	if request.method == 'POST':
		if request.POST.get('username'):
			username = request.POST.get('username')
		else:
			errors = errors+u"请输入用户名 !"
			return render(request,'login.html',locals())
		if request.POST.get('password'):
			password =  request.POST.get('password')
		else:
			errors = errors+u" 请输入密码!"
			return render(request,'login.html',locals())
		try:
			user = Users.objects.get(username=username,password=password)

		except Users.DoesNotExist:
			errors = u"账号或密码错误"
			return render(request,'login.html',locals())
		if user:
			request.session['user_id']=user.id
			return HttpResponseRedirect('/',)
		record = Record	.objects.create(userId=user)		
		record.action = u'登陆'
		record.save()
	return render(request,'login.html',locals())

def logout(request):
	user =  check(request)
	try:
		del request.session['user_id']
		record = Record	.objects.create(userId=user)		
		record.action = u'退出登陆'
		record.save()
	except KeyError:
		pass		
	return HttpResponseRedirect('/',)      

def register(request):
	errors = ""
	success = "false"
	classes = Classes.objects.all()
	user =  check(request)	
	print classes
	if request.method == 'POST':
		if request.POST.get('username'):
			username = request.POST.get('username')
		else:
			errors = errors+u"请输入用户名 !"
			return render(request,'register.html',locals())	
		if request.POST.get('password'):
			password = request.POST.get('password')
		else:
			errors = errors+u"请输入密码!"
			return render(request,'register.html',locals())		
		if request.POST.get('password2'):
			password2 = request.POST.get('password2')
		else:
			errors = errors+u"请再次输入密码!"
			return render(request,'register.html',locals())
		if request.POST.get('classname'):
			classname = request.POST.get('classname')
			try:
				classname = Classes.objects.get(className=classname)
			except Classes.DoesNotExist:
				errors = errors+u"请选择班级!"
				return render(request,'register.html',locals())	
		else:
			errors = errors+u"请选择班级!"
			return render(request,'register.html',locals())				
		if request.POST.get('name'):
			name = request.POST.get('name')
		else:
			errors = errors+u"请输入姓名 !"
			return render(request,'register.html',locals())
		try:
			user = Users.objects.get(username=username)
		except Users.DoesNotExist:
			pass
		else:
			errors = u"用户名已存在！"
			return render(request,'register.html',locals())
		if password!=password2:
			errors = u"两次输入密码不同!"
			return render(request,'register.html',locals())
		print username
		print password
		user = Users.objects.create(username = username,password = password,name=name,classname=classname)
		if request.POST.get('sex'):
			user.sex = request.POST.get('sex')
		if request.POST.get('mail'):
			user.mail = request.POST.get('mail')			
		if request.POST.get('phone'):
			user.phone = request.POST.get('phone')
		if request.POST.get('introduce'):
			user.introduce = request.POST.get('introduce')	
		user.isStudent = True	
		user.save()	
		success = "true"
		record = Record	.objects.create(userId=user)		
		record.action = u'注册'
		record.save()
	return render(request,'register.html',locals())

def information(request):
	errors = ""
	success1 = ""
	success2 = ""
	classes = Classes.objects.all()
	user =  check(request)
	if not user:
		return HttpResponseRedirect('/accounts/login/',)
	if  request.method == 'POST':
		if request.POST.get('name'):
			user.name = request.POST.get('name')		
		if request.POST.get('sex'):
			user.sex = request.POST.get('sex')
		if request.POST.get('mail'):
			user.mail = request.POST.get('mail')			
		if request.POST.get('phone'):
			user.phone = request.POST.get('phone')
		if request.POST.get('introduce'):
			user.introduce = request.POST.get('introduce')	      
		if request.POST.get('classname'):
			classname = request.POST.get('classname')	
			try:
				user.classname = Classes.objects.get(className=classname)
			except Classes.DoesNotExist:
				pass				
        		user.save()
        		success1="用户信息修改成功！"
		if request.POST.get('password'):
			password = request.POST.get('password')
			if password==user.password:
				if request.POST.get('password1'):
					password1 = request.POST.get('password1')
				else:
					errors = errors+u"请输入新密码!"
					return render(request,'register.html',locals())		
				if request.POST.get('password2'):
					password2 = request.POST.get('password2')
				else:
					errors = errors+u"请再次输入密码!"
					return render(request,'register.html',locals())
				if password1 == password2 :
					user.password = password1
					user.save()
					success2="密码修改成功！"
				else:
					errors = errors+u"两次输入密码不相同!"
			else:
				errors = errors+u"输入的密码错误!"
	return render(request,'information.html',locals())

def learn(request):
	user =  check(request)
	print user
	if not user:
		return HttpResponseRedirect('/accounts/login/',)
	CS = CourseStudy.objects.filter(userId=user)
	return render(request,'learn.html',locals())

def teacher(request):
	user =  check(request)
	teacher = Users.objects.filter(isTeacher=True)
	return render(request,"teacher.html",locals())
def check(request):
	user_id = request.session.get('user_id',default=None)
	if user_id:
		user = Users.objects.get(pk=user_id)
		return user
	else:
		return False

