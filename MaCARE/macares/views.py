from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from datetime import datetime

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
    if 'email' in request.session:
        users  = User.objects.get(email=request.session['email'])
        my_dict = {
            'name': users.name,
            'email':users.email,
            'wardno' : users.wardno,
            'district': users.district,
            'phone':users.phone,
            'panchayath':users.cmp,
            'rchid'   : users.uid  
        }
        return render(request,'wprofile.html',{'my_dict':my_dict})
    else:
        data = {'status':'You need to login first'}
        return render(request,'womenSignUp.html',context=data)


def reverse(s):
    date_str = s
    original_format = "%Y-%m-%d"
    desired_format = "%Y-%m-%d"
    original_date = datetime.strptime(date_str, original_format)

    desired_date_str = original_date.strftime(desired_format)

    print(desired_date_str)
    return desired_date_str
    
def reversed(s):
    date_str = s
    original_format = "%Y-%m-%d"
    desired_format = "%Y-%m-%d"
    original_date = datetime.strptime(date_str, original_format)

    desired_date_str = original_date.strftime(desired_format)

    print(desired_date_str)
    return desired_date_str

def wupdate(request):
    if 'email' in request.session:
        users  = User.objects.get(email=request.session['email'])
        my_dict = {
            'name': users.name,
            'email':users.email,
            'wardno' : users.wardno,
            'district': users.district,
            'phone':users.phone,
            'panchayath':users.cmp,
            'rchid'   : users.uid ,
            'lastmen' : users.lastmen,
            'lastpg':users.lastpg,
            'bg':users.bg
            }
        if request.method == 'POST':
            users  = User.objects.get(email=request.session['email'])
            print(users.name)
            name = request.POST.get('new_name')
            district = request.POST.get('newdistric')
            panchayath = request.POST.get('newpanchayath')
            wardno = request.POST.get('newwardno')
            phone = request.POST.get('newphone')
            lastmen = request.POST.get('newlastmen')
            lastpg = request.POST.get('newlastpg')
            bg = request.POST.get('newbg')
            # rchid = request.POST.get('newrchid')
         
            print(name,district,panchayath,wardno,phone,lastmen,lastpg,bg)
            users.name=name
            users.district=district
            users.cmp=panchayath
            users.wardno=wardno
            users.phone=phone
            users.lastmen=reverse(lastmen)
            users.lastpg=reversed(lastpg)  
            # users.lastmen=lastmen
            # users.lastpg=lastpg
            users.bg=bg
            users.save()
            return redirect('wprofile')

        user = User.objects.get(email=request.session['email'])
        return render(request,'wupdate.html',{'my_dict':my_dict})
    else:
        data = {'status':'You need to login first'}
        return render(request,'ashalogin.html',context=data)

def ashaWomenInWard(request):
    return render(request,'ashaWomenInWard.html')

def ashaprofile(request):
    return render(request,'ashaprofile.html')

def ashaupdate(request):
    return render(request,'ashaupdate.html')