from django.shortcuts import render, get_object_or_404, redirect
from galleries.models import Gallery, Image
from blogpost.models import BlogPost, BlogImage
from sponsorship.forms import SponsorsForm
from sponsorship.models import Sponsors, SponsorshipPackage
from exhibition.forms import ExhibitionForm 
from registration_app.forms import RegistrationForm
from Images.models import GalleryImage
from speakers.models import Speakers, SpeakerImage
from django.http import JsonResponse
from admin.models import Document
from .models import Sponsor
from registration_app.models import RegistrationCategory
from Newsletter.forms import NewsletterForm
from Contact_Us.forms import ContactUsForm
from . models import stream, stories 
from django.views.decorators.http import require_POST
from django.db.models import Q
from . forms import  StoriesForm



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
    sponsors = Sponsor.objects.all() 
    gallery_items = Gallery.objects.prefetch_related('images').all()
    context = {'items': gallery_items,
               'speakers': speakers,
               'sponsors': sponsors
               }
    return render(request, 'main/index.html', context)


def bloglist(request):
    blogs = BlogPost.objects.all()
    query = ""
    if 'q' in request.GET:
        query = request.GET['q']
        blogs = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(paragraph_1__icontains=query) | Q(paragraph_2__icontains=query) | Q(paragraph_3__icontains=query) | Q(paragraph_4__icontains=query) | Q(Keynote__icontains=query)
        ).order_by('-created_at')
        print(f"Search query: {query}")  # debug
    else:
        blogs = BlogPost.objects.all().order_by('-created_at')
    print("Blogs found:", blogs)  # debug
    return render(request, 'main/bloglist.html', {"blogs": blogs, 'query': query})

def sponsor(request):
    packages = SponsorshipPackage.objects.all()
    if request.method == 'POST':
        form = SponsorsForm(request.POST)
        if form.is_valid():
            form.save()

              # If Quform AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "type": "success",
                    "message": "Registration successful! Thank you for Becoming a Sponsor."
                })

            # Normal POST (non-AJAX)
            return redirect('sponsor')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                element_errors = {}
                for field, errors in form.errors.items():
                    element_errors[field] = {"errors": list(errors)}

                return JsonResponse({
                    "type": "error",
                    "error": ["Validation failed. Please check the form."],
                    "elementErrors": element_errors
                })
           
    else:
        form = SponsorsForm()
    return render(request, 'main/sponsor.html',   {'form': form,
        'packages': packages})

def exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)

        if form.is_valid():
            form.save()

            # If AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "type": "success",
                    "message": "Thank you for registering to become an exhibitor! Your registration has been submitted successfully."
                })

            # Normal POST
            return redirect('exhibitions')

        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                element_errors = {}
                for field, errors in form.errors.items():
                    element_errors[field] = {"errors": list(errors)}

                return JsonResponse({
                    "type": "error",
                    "error": ["Validation failed. Please check the form."],
                    "elementErrors": element_errors
                })

    else:
        form = ExhibitionForm()

    return render(request, 'main/exhibition.html', {'form': form})


def contact (request):
    return render (request, 'main/contact.html')

def registration(request):
    categories = RegistrationCategory.objects.all() 
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            # If Quform AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "type": "success",
                    "message": "Registration successful! Thank you."
                })

            # Normal POST (non-AJAX)
            return redirect('registration')

        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                element_errors = {}
                for field, errors in form.errors.items():
                    element_errors[field] = {"errors": list(errors)}

                return JsonResponse({
                    "type": "error",
                    "error": ["Validation failed. Please check the form."],
                    "elementErrors": element_errors
                })

    else:
        form = RegistrationForm()

    return render(request, 'main/registration.html', {'form': form, 'categories': categories})

def speakers (request):
    speakers = Speakers.objects.prefetch_related('images').all()

    return render (request, 'main/speakers.html', {
            'speakers': speakers
    })

def gallery (request):
    return render (request, 'main/gallery.html')


def gallery_list(request):
    images = GalleryImage.objects.exclude(image='')  # Only images with files
    return render(request, 'main/gallery.html', {
            'images': images
    })


def speaker_details(request, speaker_id):
    speaker = get_object_or_404(Speakers, id=speaker_id)
    return render(request, 'main/speaker_details.html', {'speaker': speaker})



def programme(request):
    streamId = stream.objects.all()
    # If Url Exist load the iframe else don't load it
    if streamId:
        video = streamId[0].streaming_url
        print(streamId[0].streaming_url)
    else:
        video = None

    documents = Document.objects.all().order_by('-uploaded_at')
    context = {
        "video": video,
        'documents': documents,
        "streamId": streamId                   # None if no stream
    }
    
    return render(request, 'main/programs.html', context)


def FAQs(request):
    return render(request, 'main/faqs.html')




@require_POST
def newsletter_signup(request):
    form = NewsletterForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({
            "type": "success",
            "message": "Newsletter registration successful"
        })
    return JsonResponse({
        "type": "error",
        "errors": form.errors
    }, status=400)

    
    
    
# main/views.py


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            
            print("Contact form submission successful")

            # If AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "type": "success",
                    "message": "Message sent successfully! Thank you."
                })

            # Normal POST (non-AJAX)
            return redirect('contact')

        else:
            # Handle AJAX validation errors
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                element_errors = {}
                for field, errors in form.errors.items():
                    element_errors[field] = {"errors": list(errors)}

                return JsonResponse({
                    "type": "error",
                    "error": ["Validation failed. Please check the form."],
                    "elementErrors": element_errors
                })

    else:
        form = ContactUsForm()

    return render(request, 'main/contact.html', {'form': form})
def stories (request):
    
    if request.method == 'POST':
        form = StoriesForm(request.POST)

        if form.is_valid():
            form.save()

            # If Quform AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "type": "success",
                    "message": "Story submitted successfully! Thank you."
                })

            # Normal POST (non-AJAX)
            return redirect('stories')

        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                element_errors = {}
                for field, errors in form.errors.items():
                    element_errors[field] = {"errors": list(errors)}

                return JsonResponse({
                    "type": "error",
                    "error": ["Validation failed. Please check the form."],
                    "elementErrors": element_errors
                })

    else:
        form = StoriesForm()

    return render(request, 'main/stories.html', {'form': form})
