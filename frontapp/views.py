from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gridgallery(request):
    return render(request, 'grid-gallery.html')

def err404(request):
    return render(request, '404-page.html')