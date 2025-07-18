from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
from .models import GalleryImage

def gallery_view(request):
    if request.method == 'POST':
        if 'upload' in request.POST:
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('gallery')
        elif 'delete' in request.POST:
            image_id = request.POST.get('image_id')
            image = get_object_or_404(GalleryImage, id=image_id)
            if image.image:  # Check if image file exists before deleting
                image.image.delete(save=False)
            image.delete()
            return redirect('gallery')
    else:
        form = ImageUploadForm()

    images = GalleryImage.objects.exclude(image='')  # Only images with files
    return render(request, 'images/gallery.html', {
        'form': form,
        'images': images
    })
