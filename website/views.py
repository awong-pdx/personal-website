from django.shortcuts import HttpResponse, render

# Create your views here.
def home(request):
    return render(
        request,
        'website/homepage.html'
    )

def about(request):
    return render(
        request,
        "website/about.html"
    )

def contact(request):
    return render(
        request,
        "website/contact.html"
    )