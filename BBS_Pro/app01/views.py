from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
import models
import django_comments.models
from django.contrib import auth
from django.contrib.contenttypes.models import ContentType
# Create your views here.


def index(request):
    bbs_list = models.BBS.objects.all()
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html',{
                                            'bbs_list':bbs_list,
                                            'user':request.user,
                                            'bbs_category':bbs_categories,
                                            })


def bbs_detail(request,bbs_id):

        bbs = models.BBS.objects.get(id=bbs_id)
        bbs_categories = models.Category.objects.all()
        cata_id = bbs.category.id
        return render_to_response('bbs_detail.html',{
                                                     'bbs_obj':bbs,
                                                     'user':request.user,
                                                     'bbs_category':bbs_categories,
                                                     'cata_id':int(cata_id)
                                                     })


def sub_comment(request):
    print request.POST
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment_content')
    django_comments.models.Comment.objects.create(
            content_type_id = 7,
            object_pk = bbs_id,
            site_id = 1,
            user = request.user,
            comment = comment,
    )
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
        return render_to_response('login.html',{'login_err':'Wrong username or password!: )'})


def logoutview(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return render_to_response('logout.html')


def Login(request):
    return render_to_response('login.html')


def bbs_pub(request):
    bbs_categories = models.Category.objects.all()
    return render_to_response('bbs_pub.html',{
                                                     'user':request.user,
                                                     'bbs_category':bbs_categories,
                                                     })


def bbs_sub(request):
    print '===>',request.POST.get('content')
    bbs_categories = models.Category.objects.all()
    content = request.POST.get('content')
    author = models.BBS_user.objects.get(user__username = request.user)
    models.BBS.objects.create(
    title = 'TEST TITLE',
    summary = 'HAHA',
    content = content,
    author = author,
    view_count = 1,
    ranking = 1,
                                )

    return render_to_response('bbs_detail.html',{
                                                     'user':request.user,
                                                     'bbs_category':bbs_categories,
                                                     })


def category(request,cata_id):
    bbs_list = models.BBS.objects.filter(category__id = cata_id)
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html',{
                                            'bbs_list':bbs_list,
                                            'user':request.user,
                                            'bbs_category':bbs_categories,
                                            'cata_id':int(cata_id),
                                            })