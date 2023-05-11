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
            user = User(name=name,email=email,password=password,occupation=occupation,age=age,cmp=cmp,phone=phone,wardno=wardno,district=district)
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
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        occupation = 'ahaworker'
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')
        district = request.POST.get('district')
        wardno = request.POST.get('wardno')
        phone = request.POST.get('phone')
        cmp = request.POST.get('cmp')
        ashaid = request.POST.get('ashaid')

        if(password == re_password):
            print(occupation)
            user = User(name=name,email=email,password=password,occupation=occupation,cmp=cmp,phone=phone,wardno=wardno,district=district,ashaid=ashaid)
            user.save()
            email = [email]
            request.session['uname'] = name
            request.session['email'] = email
            request.session['occupation'] = occupation
            return ashahome(request)
    else:
        return render(request, 'ashaSignUp.html')

def ashalogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(email=email)
        print(user.occupation)
        occupation = user.occupation
        if user.password == password:
            request.session['email'] = email
            if occupation=='women':
                return whome(request)
            elif occupation=='ahaworker':
                return ashahome(request)
        else:
            data = {'status':"Incorrect Password!!!"}
            return render(request,'ashalogin.html',context=data)
    else:
        return render(request, 'ashalogin.html')
    
def ashahome(request):
    return render(request,'ashahome.html')

def wGuideline(request):
    return render(request,'wGuideline.html')

def wremainder(request):
    return render(request,'wremainder.html')

def wprofile(request):
    return render(request,'wprofile.html')

def ashaWomenInWard(request):
    return render(request,'ashaWomenInWard.html')