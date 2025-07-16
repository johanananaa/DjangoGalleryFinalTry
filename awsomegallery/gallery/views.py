from django import forms
from django.shortcuts import render, redirect

from gallery.models import Image


# Create your views here.

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = []

def overview(request):
    all_images = Image.objects.all()
    return render(request, 'gallery/overview.html',
            {'images': all_images})


def upload(request):
    if request.method == 'POST':
        #actually upload the image
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('overview')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload.html', {'form': form})