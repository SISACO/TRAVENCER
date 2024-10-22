from django.shortcuts import render

# Create your views here.
def login_view(request):
  return render(request, 'pages/login-page.html')

def password_lost(request):
  return render(request, 'registration/forgot-password.html')

def User_registeration(request):
  return render(request, 'registration/registration.html')