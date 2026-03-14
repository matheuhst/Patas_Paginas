from django.http import HttpResponse

def home(request):
    return HttpResponse("rota home criada, hello, world!")