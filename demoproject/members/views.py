from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def loginUser(request):
    return render(request, 'authenticate/login.html', {})