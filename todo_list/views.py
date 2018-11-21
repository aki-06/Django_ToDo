from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    context = {'name': 'Akihiro'}
    return render(request, 'about.html', context)
