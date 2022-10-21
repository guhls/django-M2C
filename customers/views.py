from django.shortcuts import render


def home(request):
    return render(request, 'customers/pages/home.html')
