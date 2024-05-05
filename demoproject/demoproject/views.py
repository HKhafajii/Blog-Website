from django.http import HttpResponse
from django.shortcuts import render

def handler404(request, exception):
    # return render(request, '404.html', status=404)
    return HttpResponse("404: Page not found! ")