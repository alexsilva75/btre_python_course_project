from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/listings.html')

def listing(request):
    return render(request, 'pages/listing.html')