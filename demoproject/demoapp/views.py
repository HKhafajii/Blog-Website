from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import UserForm, LoginForm, MemoryForm

def homepage(request):
    # return HttpResponse("Hello, world. You're learning Django with me.")
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')

def drinks(request, drinkName):
    drink = {
        "coffee": "Regular coffee to keep you up",
        "tea": "Tea to keep you nice and relaxed",
        "water": "For all you broke ass niggas"
    }
    choiceOfDrink = drink[drinkName]

    return HttpResponse(f"<h1>{drinkName}</h1> " + choiceOfDrink)

def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request, 'register.html', {'form': form})

def login(request):
    form = LoginForm()

    return render(request, 'login.html', {'form' : form})

def memory(request):
    memoryForm = MemoryForm
    if request.method == 'POST':
        memoryForm = MemoryForm(request.POST)
        if memoryForm.is_valid:
            memoryForm.save
    return render(request, 'memoryUpload.html', {'form' : memoryForm})
