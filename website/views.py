from django.shortcuts import HttpResponse, render


# Create your views here.
def home(request):
    return render(request, "website/homepage.html")

def about(request):
    return render(request, "website/about.html")

def previous_work(request):
    return render(request, "website/previous-work.html")

def projects(request):
    return render(request, "website/projects.html")
