from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
      return render(request,'home.html')

def signuppage(request):
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

            return redirect('login')
    return render(request,'signup.html')

def loginpage(request):
      if request.method=='POST':
           email=request.POST.get('email')
           pass1=request.POST.get('pass') 
           user=authenticate(request,username=email,password=pass1)
           if user is not None:
                login(request,user)
                return redirect('home')
           else:
                return HttpResponse("username or password is incorrect  ")

      return render(request,'login.html')
