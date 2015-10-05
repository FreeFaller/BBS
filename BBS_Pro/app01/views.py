from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
import models
from django.contrib import auth
# Create your views here.


def index(request):

    bbs_list = models.BBS.objects.all()
    return render_to_response('index.html',{'bbs_list':bbs_list})


def bbs_detail(request,bbs_id):
        bbs = models.BBS.objects.get(id=bbs_id)

        return render_to_response('bbs_detail.html',{'bbs_obj':bbs})


def sub_comment(request):
    print request.POST
    bbs_id = request.POST.get('bbs_id')

    return HttpResponseRedirect('/detail/%s' %bbs_id)


def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    print username,password
    if user is not None: #and user.is_active:
        #correct password and user is marked "active"
        auth.login(request,user)
        content = '''
        Welcome %s !!!

        <a href='/logout/' >Logout</a>

         ''' % user.username
        #return HttpResponse(content)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})


def logoutview(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/index/'>Re-login</a>" % user)


def Login(request):
    return render_to_response('login.html')