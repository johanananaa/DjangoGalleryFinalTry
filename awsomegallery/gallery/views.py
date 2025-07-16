from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from gallery.models import Image


# Create your views here.

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user']

def overview(request):
    if request.user.is_authenticated:
        all_images = Image.objects.filter(user=request.user).all()
    else:
        all_images = Image.objects.all()
    return render(request, 'gallery/overview.html',
            {'images': all_images})

@login_required
def upload(request):
    if request.method == 'POST':
        #actually upload the image
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user #set the user to the currently logged-in user
            form.save()
            return redirect('overview')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload.html', {'form': form})