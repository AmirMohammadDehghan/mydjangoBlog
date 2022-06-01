# from django.shortcuts import HttpResponse
from django.shortcuts import render


def about(request):
    # return HttpResponse('hello?1')
    return render(request, 'about.html', )


def Home(request):
    # return HttpResponse('amir')
    return render(request, 'Home.html', )
