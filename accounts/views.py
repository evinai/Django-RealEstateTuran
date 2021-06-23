from django.shortcuts import render, redirect

def register(request):
  return render(request, 'accounts/register.html')


def login(request):
  return render(request, 'accounts/login.html')


def logout(request):
  return redirect('index')


def dashoard(request):
  return render(request, 'accounts/dashoard.html' )