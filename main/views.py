from django.shortcuts import render, get_object_or_404, redirect
from galleries.models import Gallery, Image
from blogpost.models import BlogPost, BlogImage
from sponsorship.forms import SponsorsForm
from sponsorship.models import Sponsors
from exhibition.forms import ExhibitionForm 
from registration_app.forms import RegistrationForm
from Images.models import GalleryImage
def about(request):
    return render(request, 'main/about.html')


def faqs(request):
    return render(request, 'main/faqs.html')


def bloglist(request):
    return render(request, 'main/bloglist.html')


def index(request):
    gallery_items = Gallery.objects.prefetch_related('images').all()
    return render(request, 'main/index.html', {'items': gallery_items})


def blog(request):
    # blog_post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'main/bloglist.html')

def sponsor(request):
    return render(request, 'main/sponsor.html')

def exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exhibitions')  # or your desired success URL
    else:
        form = ExhibitionForm()
    return render(request, 'main/exhibition.html', {'form': form})



def contact (request):
    return render (request, 'main/contact.html')

def registration (request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration')
    else:
        form = RegistrationForm()
    return render(request, 'main/registration.html', {'form': form})
    

def speakers (request):
    return render (request, 'main/speakers.html')

def gallery (request):
    return render (request, 'main/gallery.html')

def sponsorship_form_view(request):
    if request.method == 'POST':
        form = SponsorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sponsors_list')
    else:
        form = SponsorsForm()
    
    return render(request, 'main/sponsor.html', {'form': form})
def gallery_list(request):
    images = GalleryImage.objects.exclude(image='')  # Only images with files
    return render(request, 'main/gallery.html', {
            'images': images
    })