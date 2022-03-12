from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def bootstrap_index(request):
    return render(request, 'index.html',{})

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def addData(request):
    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('customer_name')
        email = data.get('customer_email')
        tel = data.get('customer_tel')
        print(name,email,tel)
        
        new = Post()
        new.name = name
        new.email = email
        new.tel = tel
        new.save()


    name = request.POST['customer_name']
    email = request.POST['customer_email']
    tel = request.POST['customer_tel']
    return render(request, 'result.html',{'name':name,'email':email})