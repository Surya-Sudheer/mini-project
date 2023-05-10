from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User

def home(request):
    return render(request,'home.html')

def womenSignUp(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        occupation = 'women'
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')
        district = request.POST.get('district')
        wardno = request.POST.get('wardno')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        cmp = request.POST.get('cmp')

        if(password == re_password):
            print(occupation)
            user = User(name=name,email=email,password=password,occupation=occupation,age=age,cpm=cmp,phone=phone,wardno=wardno,district=district)
            user.save()
            email = [email]
            request.session['uname'] = name
            request.session['email'] = email
            request.session['occupation'] = occupation
            return whome(request)
    else:
        return render(request, 'womenSignUp.html')

def whome(request):
    return render(request,'whome.html')



def ashaSignUp(request):
    return render(request,'ashaSignUp.html')

def ashalogin(request):
    return render(request,'ashalogin.html')



