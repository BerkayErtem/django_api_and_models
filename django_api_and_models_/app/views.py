from django.shortcuts import render
from user import views as user_views
def app(request):
    code=user_views.iata_code(request)
    return render(request,'app/app.html',{'code':code})
