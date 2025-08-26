from django.shortcuts import render, get_object_or_404, redirect
from galleries.models import Gallery, Image
from blogpost.models import BlogPost, BlogImage
from sponsorship.forms import SponsorsForm
from sponsorship.models import Sponsors
from exhibition.forms import ExhibitionForm 
from registration_app.forms import RegistrationForm
from Images.models import GalleryImage
from speakers.models import Speakers, SpeakerImage
def about(request):
    return render(request, 'main/about.html')


def faqs(request):
    return render(request, 'main/faqs.html')


def blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id= blog_id)
    blogs = BlogPost.objects.all().order_by('created_at')

    context = {
        'blog': blog,
        'blogs': blogs
    }
    return render(request, 'main/blog.html', context)


def index(request):
    speakers = Speakers.objects.prefetch_related('images').all()
    print("speakers found:", speakers) 
    gallery_items = Gallery.objects.prefetch_related('images').all()
    context = {'items': gallery_items,
               'speakers': speakers,}
    return render(request, 'main/index.html', context)


def bloglist(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    print("Blogs found:", blogs)  # debug
    return render(request, 'main/bloglist.html', {"blogs": blogs})

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
    speakers = Speakers.objects.prefetch_related('images').all()

    return render (request, 'main/speakers.html', {
            'speakers': speakers
    })

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


def speaker_details(request, speaker_id):
    speaker = get_object_or_404(Speakers, id=speaker_id)
    return render(request, 'main/speaker_details.html', {'speaker': speaker})