from django.http import HttpResponse



def hola_mundo(requests):
    return HttpResponse("hola mundo")