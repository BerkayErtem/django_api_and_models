
from os import name
from django.contrib import auth
from django.core.checks.messages import Error
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db.models.deletion import CASCADE           
from django.urls import reverse 

class Company(models.Model):
    id= models.CharField(max_length=20,primary_key=True, serialize=False, verbose_name='Company Code')
    company_name=models.CharField(max_length=80, blank=False)
    #sub=models.ManyToManyField('Subsidiaries', related_name='Company_sub')
    date=models.DateField(blank=True)
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)   
    def __str__(self):
        return self.company_name

class Subsidiaries(models.Model):
    id=models.CharField(max_length=20,primary_key=True, serialize=False, verbose_name='Subsidiaries Code')
    name=models.CharField(max_length=80, blank=False)
    city=models.CharField(max_length=80, blank=False)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    date=models.DateField(blank=True)

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)   
    def __str__(self):
        return self.name
# class Branches():
#     id= models.CharField(max_length=20,primary_key=True, serialize=False, verbose_name='Branch Code')
#     name=models.CharField(max_length=50)
    

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user
class MyUser(AbstractBaseUser,PermissionsMixin): 
    username=models.CharField(max_length=50, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, blank=True,)
    first_name = models.CharField(max_length=30,blank=True,)
    last_name = models.CharField(max_length=30,blank=True,)
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE, blank=True)
    subsidiary=models.ForeignKey(Subsidiaries,on_delete=models.CASCADE,blank=True, default=None)
    date_of_birth = models.DateField(default='1900-01-01', blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_arranger=models.BooleanField(default=False)
    is_worker=models.BooleanField(default=False)
    is_kk=models.BooleanField(default=False)
    
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=()
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label): 
        return True
    @property
    def is_staff(self):
        return self.is_admin

    