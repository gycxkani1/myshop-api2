from apps.goods.models import *
from django import forms
from django.core.exceptions import ValidationError
import re
from apps.goods.views import *

def sort_validate(value):
    sort_re = re.compile(
        r'^[1-9]\d*$')
    if not sort_re.match(value):
        raise ValidationError('排序必须为正整数')

class GoodsCategoryForm(forms.Form):
    name = forms.CharField(label="分类名称", min_length=2, required=True,
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': "请输入分类名称"}),
                               error_messages={
                                   'required': '分类名称不能为空',
                                   'min_length': '长度最少2位',
                               })
    parent_id = forms.CharField(label="选择父类", max_length=20, required=True,
                               widget=forms.widgets.Select(
                                   attrs={'class': 'form-control custom-select', 'placeholder': "请选择父类"}),
                               error_messages={
                                   'required': '请选择父类',
                               })

    sort = forms.CharField(label="排序", validators=[sort_validate], required=True,
                                widget=forms.widgets.TextInput(
                                   attrs={'class': 'form-control','placeholder': "请输入数字"}),
                                error_messages={
                                    'required': '排序值不能为空',
                                })
    logo = forms.ImageField(label="分类图片",required=False, widget=forms.widgets.FileInput(
                                   attrs={'class': 'custom-file-input'}))
    
    def __init__(self, *args, **kwargs):
        
        super(GoodsCategoryForm, self).__init__(*args, **kwargs)
        cates_all=GoodsCategory.objects.all()
        self.alist=[('','请选择...')]
        self.fields['parent_id'].widget.choices = self.binddata(cates_all,0,1)
        

    def binddata(self,datas,id,n):
        if id==0:
            datas=datas.filter(parent__isnull = True)
        else:
            datas=datas.filter(parent_id = id)
        for data in datas:
            #列表中添加元组
            self.alist.append((data.id,self.spacelength(n)+data.name))
            #递归处理
            self.binddata(datas,data.id,n+2)
        return self.alist
    
    def spacelength(self,i):
        space=''
        for j in range(1,i):
            space+="--"
        return space+"|--"
    

class GoodsModelForm(forms.ModelForm):
    class Meta:
         # 定义关联模型
        model = Goods
        # 定义需要在表单中展示的字段。
        fields = ['name', 'category', 'market_price', 'price', 'main_img', 'goods_desc']
        # 如果要显示全部字段，可以如下设置
        # fields="__all__"
         # 如果Models中定义了名称，这里不用再定义
        labels = {
           
        }
        widgets = {

            "main_img": forms.widgets.FileInput(attrs={'class': 'custom-file-input'}),
            "goods_desc": forms.widgets.Textarea(attrs={"class": "form-control","name":"content"})
            
        }
        error_messages = {
            "name": {
                'required': '商品名不能为空',
                'max_length': '长度最多50位',
                'invalid': '输入正确的商品名'
            },
            "category": {
               'required': '商品分类不能为空',
            },
            "market_price": {
                'required': '市场价格不能为空',
            },
            "price": {
                'required': '实际价格不能为空',
            },
            "main_img": {
                'required': '用户主图不能为空',
            },
            "goods_desc": {
                'required': '商品详情不能为空',
            }
        }
    # 校验手机号码的局部钩子函数
    # def clean_mobile(self):
    #     mobile = self.cleaned_data.get('mobile')
    #     print(mobile)
    #     mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    #     if not mobile_re.match(mobile):
    #         raise ValidationError('手机号码格式错误')
    #     return mobile
    
    # 校验年龄的局部钩子函数
    # def clean_age(self):
    #     age = self.cleaned_data.get('age')
    #     print(age)
    #     if age < 1 or age > 120:
    #         raise ValidationError('年龄只能在1-120之间')
    #     return age
    
    # 校验用户名的局部钩子函数
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     print(username)
    #     if len(username) < 6 or len(username) > 30:
    #         raise ValidationError('用户名的长度只能在6-30之间')
    #     return username
    
    # 校验密码的局部钩子函数
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     print(password)
    #     if len(password) < 6 or len(password) > 20:
    #         raise ValidationError('密码的长度只能在6-20之间')
    #     return password
    
     # 校验确认密码的局部钩子函数
    # def clean_confirm_password(self):
    #     # password =  self.cleaned_data.get("password")
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     print(confirm_password)
    #     if len(confirm_password) < 6 or len(confirm_password) > 20:
    #         raise ValidationError('确认密码的长度只能在6-20之间')
    #     # if password != confirm_password:
    #     #     raise forms.ValidationError("二次密码输入不一致")
    #     return confirm_password

    # 全局钩子函数
    # def clean(self):
    #     password =  self.cleaned_data.get("password")
    #     confirm_password = self.cleaned_data.get("confirm_password")
    #     if password != confirm_password:
    #         raise forms.ValidationError("二次密码输入不一致")

