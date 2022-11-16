from django.db import models

# Create your models here.
class Department(models.Model):
    """"部门表"""
    """"id django会自动新建并新增"""
    title = models.CharField(verbose_name="部门名称",max_length= 32)
    description = models.CharField(verbose_name="部门描述",max_length=64)

class Profession(models.Model):
    title = models.CharField(verbose_name="行业类型", max_length=32)
    description = models.CharField(verbose_name="行业描述", max_length=64)


class Employee(models.Model):
    """"员工表"""
    job =  models.IntegerField(verbose_name="工号",)
    name = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=32)
    iphone =  models.CharField(verbose_name="手机号",max_length=11)
    create_time = models.DateTimeField(verbose_name="创建时间")
   #级联删除 depart = models.ForeignKey(to="Department", to_field="id",  on_delete=models.CASCADE)
    depart = models.ForeignKey(to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL) #关联部门表id 生成depat_id 并运行为空，部门删除设置人员部门为空
    gender_choices = (
        (1,"男"),
        (2,"女")
    )
    identity_choices = (
        (1, "员工"),
        (2, "管理员")
    )
    gender=models.SmallIntegerField(verbose_name="性别",choices=gender_choices)
    identit=models.SmallIntegerField(verbose_name="身份",choices=identity_choices)

class CustomerInfo(models.Model):
    """"客户表"""
    name = models.CharField(verbose_name="姓名", max_length=32)
    iphone = models.CharField(verbose_name="手机号", max_length=11)
    create_time = models.DateTimeField(verbose_name="创建时间")

    profession = models.ForeignKey(to="Profession", to_field="id", null=True, blank=True,
                               on_delete=models.SET_NULL)  # 关联部门表id 生成depat_id 并运行为空，部门删除设置人员部门为空
    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    address = models.CharField(verbose_name="地址",max_length=120)
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)