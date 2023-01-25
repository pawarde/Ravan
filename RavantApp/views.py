from django.shortcuts import render, redirect

import mysql.connector as sql
from django.contrib import messages
from django.http import HttpResponse
from .models import LoginDetails,MachinevisionCamera
from .filters import machineFilter


# from .forms import UserRegisterForm

# def login_page(request):
#     m = LoginDetails.objects.get(user_name=request.POST['username'])
#     if m.password(request.POST['password']):
#         request.session['user'] = m.id
#         return HttpResponse("You're logged in.")
#     else:
#         return HttpResponse("Your username and password didn't match.")



def home(request):
    context={
        'machines':machines,"user_name":user_name
    }
    return render(request, 'html_tags/login.html',context)

user_name=''
password=''
machine_name=''
def login_page(request):
    global user_name,password
    if request.method =="POST":
        m=sql.connect(host="localhost",user="root",password="insightzz123",database='ravandata')
        cursor=m.cursor()
        d=request.POST
        print(d.items())
        for key,value in d.items():
            if key=="username":
                user_name=value
            if key=="password":
                password=value
        print("username",user_name,"password",password)
        c="SELECT * FROM ravandata.login_Details where User_name='{}' and Password='{}'".format(user_name,password)
        
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            # return render(request,'html_tags/report.html')
            return HttpResponse(" Please Enter Valid User Details ")
        else:
            # return render(request,'html_tags/users.html')
            response=redirect('/users/')
            return response
            
            
    return render(request,'html_tags/login.html')

       

    

def users(request):
    login=LoginDetails.objects.all()
    context={
        'login':login,"user_name":user_name
    }      
    return render(request, 'html_tags/users.html',context)

# def MachineVision(request):
#     m=sql.connect(host="localhost",user="root",password="insightzz123",database='ravandata')
#     cursor=m.cursor()
#     c="select * from MachineVision_Camera;"
#     cursor.execute(c)
#     machine=cursor.fetchall()
#     context={
#             'machine':machine
#     }
#     print(context)
#     return render(request, 'html_tags/machines.html',context)  

def MachineVision(request):
    machines =MachinevisionCamera.objects.all()
    machinecount=machines.count()
    print("machinecourn",machinecount)
    context={
        'machines':machines,"user_name":user_name
    }
    return render(request, 'html_tags/machines.html',context )  



def add_machine(request):
    return render(request,'html_tags/add_machines.html')

def logot(request):
    return render(request,'/')

def IP_Camera(request):
    return render(request, 'html_tags/report.html')

def Downloads(request):
    return render(request, 'html_tags/image_tagging.html')    

# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Hi {username}, your account was created successfully')
#             return redirect('home')
#     else:
#         form = UserRegisterForm()

#     return render(request, 'users/register.html', {'form': form})


# @login_required()
# def profile(request):
#     return render(request, 'users/profile.html')







