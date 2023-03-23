from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def lostandFound(request):
    return HttpResponse("lostandFound")
def adoption(request):
    return HttpResponse("adoption")
def contact(request):
    return HttpResponse("contact")
