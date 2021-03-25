from user.models import Company, Subsidiaries
from django.contrib import admin
from user.forms import *
from django.contrib.auth.models import Group

class companyview(admin.ModelAdmin):
    list_display=('id','company_name')
    search_fields=('id','company_name')
class userview(admin.ModelAdmin):
    list_display=('username','first_name','last_name','email','is_active','is_admin')
    search_fields=('username','first_name','last_name','email')
    list_filter=('is_admin','company_name')
class Subsidiariesview(admin.ModelAdmin):
    list_display=('id','name','city','company')
    search_fields=('id','name','city','company__company_name')
    list_filter=('city','company')

    
admin.site.register(MyUser,userview)
admin.site.register(Company, companyview)
admin.site.register(Subsidiaries, Subsidiariesview)




