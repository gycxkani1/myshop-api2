import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
#from notebook.auth.security import set_password
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.users.models import MyUser
from apps.users.serializers import *
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import authentication
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from common.custommodelviewset import CustomModelViewSet
from common.permissions import IsOwnerOrReadOnly

class MyUserViewSet(CacheResponseMixin,CustomModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserRegSerializer

    #lookup_field = "pk"
    #lookup_url_kwarg = None
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if  self.action=="create":
            return MyUserRegSerializer
        elif self.action=="retrieve":
            return MyUserUpdateSerializer
        elif self.action=="update":
            return MyUserUpdateSerializer
        
        return MyUserUpdateSerializer

    def get_permissions(self):
        if  self.action=="retrieve":
            print("retrieve")
            return [permissions.IsAuthenticated()]
        elif self.action=="update":
            print("update")
            return [permissions.IsAuthenticated()]
        else:
        #return []
            return []
    #获取当前用户
    def get_object(self):
        return self.request.user



class MyUserDetailViewSet(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserUpdateSerializer

    #authentication_classes = (permissions.IsAuthenticated,authentication.TokenAuthentication)


myuser=get_user_model()
class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 根据用户名或手机号查询用户
            myuser = MyUser.objects.get(Q(username=username)|Q(mobile=username))
            if myuser.check_password(password): #验证密码
                return myuser
        except Exception as e:
            return None


def user_reg(request):
    if request.method=="GET":
        form_obj=forms.UserRegForm()
        return render(request,'shop/user_reg.html',{"form_obj":form_obj})
    if request.method=="POST":
        form_obj=forms.UserRegForm(request.POST,request.FILES)
        if form_obj.is_valid():
            uname=request.POST.get("username",'')
            users=MyUser.objects.filter(username=uname)
            if users:
                for user in users:
                    user_img=user.user_img
                info='用户已经存在'
            else:
                form_obj.cleaned_data.pop("re_password")
                form_obj.cleaned_data["is_staff"]=1 
                form_obj.cleaned_data["is_superuser"]=0 #非管理员
                #接收页面传递过来的参数，进行用户新增
                user=MyUser.objects.create_user(**form_obj.cleaned_data)
                user_img=user.user_img
                info='注册成功,请登陆'
            return render(request,'shop/user_reg.html',{"form_obj":form_obj,"info":info,"user_img":user_img})
        else:
            errors = form_obj.errors
            print(errors)
            return render(request, "shop/user_reg.html", {'form_obj': form_obj, 'errors': errors})
        #return render(request,'shop/user_reg.html',{"form_obj":form_obj})

def user_login(request):
    return render(request,"shop/user_login.html")

def user_logout(request):
    logout(request)
    return redirect(reverse("user_login"))


def ajax_login_data(request):
    if request.method=="POST":
        uname=request.POST.get("username",'')
        pwd=request.POST.get("password",'')
        json_dict={}
        if uname and pwd:  ## 不为空的情况下，查询数据库
            if MyUser.objects.filter(username=uname): #判断用户是否存在
                #如果存在，进行验证
                user=authenticate(username=uname,password=pwd)
                if user: #如果验证通过
                    if user.is_active: #如果用户状态为激活
                        login(request,user) #进行登陆操作，完成session的设置
                        json_dict["code"]=1000
                        json_dict["msg"]="登陆成功"
                    else:
                        json_dict["code"]=1001
                        json_dict["msg"]="用户还未激活"
                else:
                    json_dict["code"]=1002
                    json_dict["msg"]="账号密码不对，请重新输入"
            else:
                json_dict["code"]=1003
                json_dict["msg"]="用户账号有误，请查询"
        else:
            json_dict["code"]=1004
            json_dict["msg"]="用户名或者密码为空"
        return JsonResponse(json_dict)



from django.shortcuts import redirect
def diy_loginView(request):
    if request.method=="GET":
        return render(request,'shop/user_login.html')
    if request.method=="POST":
        uname=request.POST.get("username",'')
        pwd=request.POST.get("password",'')
        if MyUser.objects.filter(username=uname): #判断用户是否存在
            #如果存在，进行验证
            user=authenticate(username=uname,password=pwd)
            if user: #如果验证通过
                if user.is_active: #如果用户状态为激活
                    login(request,user) #进行登陆操作，完成session的设置
                    info="登陆成功"
                    return redirect('/userbaseinfo_add')
                    #next=request.GET.get("next")
                    #if next:
                    #    print("http://"+request.get_host()+next)
                    #    return HttpResponseRedirect("http://"+request.get_host()+next)
                else:
                    info="用户还未激活"
            else:
                info="账号密码不对，请重新输入"
        else:
            info='用户账号不存在，请查询'
        return render(request,'shop/user_login.html',{"info":info})

from django.contrib.auth.decorators import login_required, permission_required
from apps.users import forms
@login_required
@permission_required("add_userbaseinfo")
def userbaseinfo_add(request):
    if request.method=="GET":
        return HttpResponse("进行新增操作")
    if request.method=="POST":
        #接收数据
        #保存
        pass


def test(request):
    return HttpResponse("我也执行了")
