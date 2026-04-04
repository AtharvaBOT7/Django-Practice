from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, You are at the home page!")