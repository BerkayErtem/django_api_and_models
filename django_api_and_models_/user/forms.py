from django.contrib.auth import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models import fields
from django.forms import widgets
from django.contrib.auth.models import  User
from django.core.exceptions import ValidationError
from django.forms.forms import Form
from user.models import MyUser, Subsidiaries, Company
from django import forms

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name','date_of_birth', 'password1', 'password2','is_admin','is_arranger','is_worker','is_kk','company_name','subsidiary')
        widgets={
            'username':widgets.TextInput(attrs={'placeholder':'This field is required',
            'password1':'password'})
        }
        help_texts={
            'username':'Username',
        }
        # def clean_password2(self):
        #     # Check that the two password entries match
        #     password1 = self.cleaned_data.get("password1")
        #     password2 = self.cleaned_data.get("password2")
        #     if password1 and password2 and password1 != password2:
        #         raise ValidationError("Passwords don't match")
        #     return password2
        
        # def save(self,request, commit=True):
        #     user = super().save(commit=False)
        #     user.set_password(self.cleaned_data["password1"])
        #     if commit:
        #         user.save()
        #     return user

class EditProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=MyUser
        fields=(
            'email',
            'first_name',
            'last_name',
            'date_of_birth',
            'company_name',
            'subsidiary'
            )
        widgets={'first_name':widgets.TextInput(attrs={'value':''})}
        def save(self, commit=True):
            user = super(EditProfileForm, self).save(commit=False)
            user.save()
class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=('id','company_name','date')
 