from django.shortcuts import render , redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
def home_view(request):
  return render(request , 'home.html')

def login_view(request):
  if request.method == 'POST':
    uemail = request.POST.get('email1')
    upass = request.POST.get('password1')
    user = authenticate(request , email = uemail , password = upass)
    if user is not None:
      print('user validated')
      login(request , user)
      return redirect('home')
    else:
      print('user did not validate')
    return redirect('login')
  return render(request , 'auth/login.html')

def logout_view(request):
  logout(request)
  return redirect('home')

def select_account_type(request):
  return render(request , 'register/account-type.html')

def student_registration(request):
  return render(request , 'register/student-registration.html')

def professor_registration(request):
  return render(request , 'register/professor-registration.html')
