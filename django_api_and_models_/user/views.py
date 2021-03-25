from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib import auth
from .models import Company, MyUser
from user.forms import CompanyForm, SignUpForm, EditProfileForm
from django.core.exceptions import ValidationError
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


def error_404_view(request,exception):
    return render(request, '404.html')

def register(response):

    if response.method=='POST':
        
        form=SignUpForm(response.POST)
        if form.is_valid():
           
            user=form.save()
            auth.login(response,user,backend='django.contrib.auth.backends.ModelBackend')     
            return redirect('/home')
            
        
    else:
        form=SignUpForm()
    return render(response, 'register.html', {'form':form,'title':'Register'})

def company(response):
    if response.method=='POST':
        form=CompanyForm(response.POST)
        if form.is_valid():
            form=form.save()
        return redirect('/home')
    else:
        form=CompanyForm()
    return render(response, 'addcompany.html', {'form':form,'title':'Company'})

def login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                    # correct username and password login the user
                    auth.login(request, user)
                    return redirect('/home')
            
        except:
            return redirect('registration/login.html')
            
    return render(request, 'registration/login.html',{'title':'LogIn'})

@user_passes_test(lambda user:user.is_active)
def home(request):
    company=Company.objects.all()
    context={'company':company,
            'title':'Home'}
    return render(request, 'home.html',context)

def logout(request):
    kk = i()
    auth.logout(request)
    return render(request,'logout.html',{'text':kk,'title':'LogOut'})

#variable transfer between funtions
def i():

    kk='Logged Out!'
    return kk 

@login_required(login_url='login')
def view_profile(request):
    args={'user':request.user,'title':request.user}
    return render(request, 'profile.html', args)
    
#permission_required
def edit_profile(request):
    form=EditProfileForm(request.POST, instance=request.user)
    if request.method == 'POST':
        form=EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
               
    return render(request, 'edit_profile.html', {'form':form,'title':'EditProfile'})
    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form, 'title':'Change Password'})

#get data 
@login_required(login_url='login')
def users(request):
    
    data=MyUser.objects.filter(first_name='').values('username')
    data2=MyUser.objects.all().order_by('id')
    data3=MyUser.objects.all().values('username','email').order_by('id')
    is_worker=MyUser.objects.filter(is_worker=1).values('username').order_by('id')
    company=Company.objects.all().order_by('id'),
    company1=MyUser.objects.filter(company_name_id='1').order_by('id')
    data2=list(data2)
    data3=list(data3)
    data4=list(is_worker)
    
    
    
    context={
        'data':data,
        'data2':data2,
        'data3':data3,
        'data4':data4,
        'company':company,
        'company1':company1,
        'title':'User Table'
    }
    return render (request, 'users.html',context)

def users_detail(request,pk):
    instance=get_object_or_404(MyUser, pk=pk)
    context={
        'i':instance
    }
    return render(request, 'user_details.html', context)

@login_required(login_url='login')
def get_iata(request):
    

    import requests
    import json
    code=iata_code(request)
    
    if request.method=='POST':
        iata=request.POST.get('iata')
        
        if not iata:
            return render(request, 'iata.html')

        import requests
        from requests.models import Response

        url = "https://iata-and-icao-codes.p.rapidapi.com/airline"
        
        parameters = {"iata_code":iata}


        headers = {
            'x-rapidapi-key': "a16f783100mshfee2bb51833953fp1bc127jsneee2389ae7ec",
            'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=parameters)
        res=response.json()[0]
        
        
        
        
        
        
        context={
                'res':res, 
                'title':'API',
                } 
        return render(request, 'iata.html',context)
    return render(request, 'iata.html', {'title':'API','code':code}) 

def iata_code(request):
    import requests
    import json
    url = "https://iata-and-icao-codes.p.rapidapi.com/airlines"

    headers = {
        'x-rapidapi-key': "a16f783100mshfee2bb51833953fp1bc127jsneee2389ae7ec",
        'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    
    
    code=[]

    for i in range(len(response.json())):
        
        code1=response.json()[i]['icao_code']
        code.append(code1)
        
    
    return code

def hotel_bycity(request):
    import requests
    import json
    if request.method=='POST':
        
        city=request.POST.get('city')
        country=request.POST.get('country')
        url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"
        querystring = {"cityName":city,"countryName":country}
        headers = {
        'x-rapidapi-key': "a16f783100mshfee2bb51833953fp1bc127jsneee2389ae7ec",
        'x-rapidapi-host': "best-booking-com-hotel.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response_json=response.json()

        code=iata_code(request)
        context={'code':code,
                'hotel':response_json,

                } 
    
        return render(request, 'hotelbycity.html',context)
    return render(request, 'hotelbycity.html',{'title':'API'}) 

