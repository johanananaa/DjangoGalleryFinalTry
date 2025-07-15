from django.shortcuts import render

from gallery.models import Image


# Create your views here.
def overview(request):
    all_images = Image.objects.all()
    return render(request, 'gallery/overview.html',
            {'images': all_images})


def upload(request):
    return render(request, 'gallery/upload.html')