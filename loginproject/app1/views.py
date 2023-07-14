from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def homepage(request):
      if 'username' in request.session:
           
           return render(request,'home.html')
      else:
           return redirect('loginn')
      


def signuppage(request):
    if 'username' in request.session:
         return redirect('home')
         
    if request.method=='POST':
         uname= request.POST.get('username')
         email= request.POST.get('email')
         pass1= request.POST.get('password')
         pass2= request.POST.get('cpassword')

         if pass1!=pass2:
              return HttpResponse('password and confirmed passwords are incorrect')
         else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()

            return redirect('loginn')
    return render(request,'signup.html')

def loginpage(request):
      if 'username' in request.session:
           return redirect('home')
      if request.method=='POST':
           uname=request.POST.get('username')
           pass1=request.POST.get('pass') 
           user=authenticate(request,username=uname,password=pass1)
           print(user)
           if user is not None:
                login(request,user)
                request.session['username']=uname
                return redirect('home')
           else:
                return HttpResponse("username or password is incorrect  ")

      return render(request,'login.html')
def logoutpage(request):
     logout(request)
     if 'username' in request.session:
          logout(request)
          request.session.flush()
     
     return redirect('loginn')
     