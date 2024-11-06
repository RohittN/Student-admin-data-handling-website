from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from django.contrib import messages
import os
from .models import *
from .models import stdregister

def studentwebsite(request):
    return render(request,'studentin.html')


def websiteform(request):
    if request.method=="POST":
        name = request.POST.get('Name')
        phone =request.POST.get('Phone')
        email=request.POST.get('Email')
        message= request.POST.get('Message')
        fs= FileSystemStorage()
        reg= stdform(Name=name,Phonenumber=phone,Email=email,Message=message)
        reg.save()
        return redirect('studentwebsite')
    return render(request,'studentin.html')



def login_page(request):
    return render(request,'loginpage.html')

def adminn(request):
    res=stdregister.objects.all()
    return render(request,'clgadmin.html',{'result':res}) 


def log_ad_std(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print("Login attempt - Username:", username, "Password:", password)  

        # Admin login check
        if username == 'admin_123' and password == 'admin12':
            request.session['logindetails'] = username
            request.session['admin'] = 'admin'
            return redirect('adminpage')
     
        try:
            
            student_exists = stdregister.objects.filter(Username=username, Password=password).exists()
            print("Student exists:", student_exists)  
            
            if student_exists:
               
                student = stdregister.objects.get(Username=username, Password=password)
                print("Found student:", student.Username)  
                
               
                request.session['uid'] = student.id
                request.session['user'] = student.Username
                print("Session data set - ID:", student.id, "Username:", student.Username)  
                
                return redirect('studentwebsite')
            else:
                print("No matching student found")  
                return render(request, 'loginpage.html', {'status': 'Invalid username or password'})
                
        except Exception as e:
            print("Error during login:", str(e))  
            return render(request, 'loginpage.html', {'status': 'An error occurred during login'})
    
    return render(request, 'loginpage.html')


def register(request):
    return render(request,'stdreg.html')



def studentreg(request):
    if request.method == "POST":
       
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')    

        if stdregister.objects.filter(Username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'stdreg.html')
            
     
        if loginform.objects.filter(Username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'stdreg.html')
        
        # Check password in register model
        if stdregister.objects.filter(Password=password).exists():
            messages.error(request, 'Password already in use. Please choose a different password.')
            return render(request, 'stdreg.html')
        
        # Check password in login form
        if loginform.objects.filter(Password=password).exists():
            messages.error(request, 'Password already in use. Please choose a different password.')
            return render(request, 'stdreg.html')
        reg = stdregister(FirstName=firstname,LastName=lastname,Email=email,Phonenumber=phone,Username=username,Password=password)
        reg.save()
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login_page')
        
    return render(request, 'stdreg.html')


def delete_object(request, id):
    student = stdregister.objects.get(id=id)
    student.delete()
    return redirect('adminpage')



def stdprofile(request):
    std_id = request.session.get('uid')  # Retrieve 'uid' from session
    if std_id is None:
        return redirect('studentwebsite')  
    student = get_object_or_404(stdregister, id=std_id)
    return render(request, 'stdprofile.html', {'student': student})

def editprof(request,id):
    stdnid = stdregister.objects.get(id=id)
    return render(request,'editprofile.html',{'result':stdnid})

def edit_stdprofile(request,id):
    # Get the student ID from the session
    # std_id = request.session.get('uid')
    
    # Retrieve the student profile based on the ID
    student = stdregister.objects.get(id=id)
    
    if request.method == 'POST':
        # Update the student profile with the new data
        student.FirstName = request.POST['firstname']
        student.LastName = request.POST['lastname']
        student.Email = request.POST['email']
        student.Phonenumber = request.POST['phone']
        student.Username = request.POST['username']
        student.save()
        return redirect('stdprofile')  

    return render(request, 'stdprofile.html', {'student': student})


# def logout(request):
#     session_keys = list(request.session.keys())         #delete session dictionary conatining keys of login
#     for key in session_keys:
#         del request.session[key]
#     return redirect('login_page')

def logout(request):
    request.session.flush() 
    return redirect('login_page')




