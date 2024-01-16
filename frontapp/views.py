from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gridgallery(request):
    return render(request, 'grid-gallery.html')
