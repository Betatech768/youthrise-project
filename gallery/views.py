from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import GalleryForm, ImageForm
from .models import Image, Gallery

def upload_gallery(request):
    if request.method == 'POST':
        gallery_form = GalleryForm(request.POST)
        files = request.FILES.getlist('image')

        if gallery_form.is_valid():
            gallery = gallery_form.save()

            for f in files:
                Image.objects.create(gallery=gallery, image=f)

            return redirect('gallery_success')
    else:
        gallery_form = GalleryForm()

    return render(request, 'gallery/upload.html', {
        'gallery_form': gallery_form
    })

def gallery_success(request):
    return render(request, 'gallery/success.html')


def gallery_list(request):
    galleries = Gallery.objects.prefetch_related('images').all()
    return render(request, 'gallery/gallery_list.html', {'galleries': galleries})
