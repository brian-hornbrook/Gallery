from django.shortcuts import render, get_object_or_404
from .models import Gallery

def index(request):
    images = Gallery.objects.all()
    # i = get_object_or_404(Gallery, pk=1)
    return render(request, 'index.html')

def addImage(request):
    if request.method == 'POST':
        photo = Item()
        photo.image = request.POST.get('image')
        return render('index.html')