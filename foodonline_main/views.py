from django.http import HttpResponse




def home(request):
    return HttpResponse('<h1>hi , django </h1>')