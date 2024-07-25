from django.shortcuts import render

from django.shortcuts import render

def menu(request, page):
    return render(request, 'page.html', {'page': page})
