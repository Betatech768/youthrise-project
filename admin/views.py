from django.shortcuts import render, redirect, get_object_or_404
from blogpost.forms import BlogPostForm
from blogpost.models import BlogImage, BlogPost
from django.http import JsonResponse
from speakers.models import Speakers, SpeakerImage
from speakers.forms import SpeakerForm, SpeakerImageForm
from sponsorship.forms import SponsorsForm
from sponsorship.models import Sponsors
from exhibition.models import Exhibition
from registration_app.models import Registration
from galleries.forms import  ImageForm
from galleries.models import Image, Gallery
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm
from galleries.forms import ImageForm, GalleryForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from Images.forms import ImageUploadForm
from Images.models import GalleryImage
def user_login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')  # Already logged in

    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('admin_page')
            else:
                messages.error(request, 'Invalid username or password.')

    return render(request, 'admin/admin_signin.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')

# Create your views here.
@login_required
def admin(request):
    return render(request, 'admin/admin.html')

@login_required
def admin_gallery(request):
    return render (request, 'admin/admin_gallery.html')

@login_required
def create_and_list_blog_posts(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            images = request.FILES.getlist('images')
            if len(images) > 2:
                form.add_error('images', 'You can only upload up to 2 images.')
            else:
                for image in images:
                    BlogImage.objects.create(blog=post, image=image)

                return redirect('blog_success')  # Or your desired redirect target
    else:
        form = BlogPostForm()

    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'admin/admin_blog.html', {'form': form, 'posts': posts})

@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        files = request.FILES.getlist('images')

        if form.is_valid():
            if len(files) > 2:
                return render(request, 'blog/admin_edit_blog.html', {
                    'form': form,
                    'post': post,
                    'error': 'You can upload a maximum of 2 images.',
                    'images': post.images.all()
                })

            form.save()

            if files:
                post.images.all().delete()
                for image in files:
                    BlogImage.objects.create(blog=post, image=image)

            return redirect('blog_post')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'admin/admin_edit_blog.html', {
        'form': form,
        'post': post,
        'images': post.images.all()
    })
    
    

@login_required
# Delete speaker
def delete_speaker(request, speaker_id):
    speaker = get_object_or_404(Speakers, pk=speaker_id)
    if request.method == 'POST':
        speaker.delete()
        return redirect('create_speaker')
    return render(request, 'admin/admin_delete.html', {'speaker': speaker})


@login_required
def create_speaker(request):
    speakers = Speakers.objects.all().order_by('-created_at')
    images = SpeakerImage.objects.all()

    if request.method == 'POST':
        speaker_form = SpeakerForm(request.POST)
        image_form = SpeakerImageForm(request.POST, request.FILES)

        if speaker_form.is_valid() and image_form.is_valid():
            speaker = speaker_form.save()
            image = image_form.save(commit=False)
            image.blog = speaker  # Link the image to the speaker
            image.save()
            return redirect('speaker_success')

    else:
        speaker_form = SpeakerForm()
        image_form = SpeakerImageForm()

    return render(request, 'admin/admin_speaker.html', {
        'speaker_form': speaker_form,
        'image_form': image_form,
        'speakers': speakers,
        'images': images
    })
@login_required
def edit_speaker(request, speaker_id):
    speaker = get_object_or_404(Speakers, pk=speaker_id)
    
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES, instance=speaker)
        files = request.FILES.getlist('images')

        if form.is_valid():
            updated_speaker = form.save()

            if files:
                # Delete old images
                speaker.images.all().delete()

                # Save new images
                for img in files:
                    SpeakerImage.objects.create(blog=updated_speaker, image=img)

            return redirect('create_speaker')
    else:
        form = SpeakerForm(instance=speaker)
    
    return render(request, 'admin/admin_speaker_edit.html', {
        'form': form,
        'speaker': speaker,
        'images': speaker.images.all(),
    })
@login_required
def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        post.delete()  # This will also delete images if `on_delete=models.CASCADE` is used
        return redirect('blog_post')

    return render(request, 'admin/admin_delete_blog.html', {'post': post})



    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('term', '')
        posts = BlogPost.objects.filter(title__icontains=query)[:10]
        results = [post.title for post in posts]
        return JsonResponse(results, safe=False)
    
    # Always return a fallback response if not AJAX
    return JsonResponse({'error': 'Invalid request'}, status=400)

def sponsors_list_view(request):
    sponsors = Sponsors.objects.all().order_by('-id')
    return render(request, 'admin/adminsponsor.html', {'sponsors': sponsors})

@login_required
def exhibition_list_view(request):
    exhibitions = Exhibition.objects.all().order_by('-id')
    return render(request, 'admin/admin_exhibition.html', {'exhibitions': exhibitions})
@login_required
def registration_list_view(request):
    registrations = Registration.objects.all()
    return render(request, 'admin/admin_registration.html', {'registrations': registrations})

@login_required
def gallery_success(request):
    return render(request, 'admin/gallery_success.html')


@login_required
def speaker_success(request):
    return render(request, 'admin/speaker_success.html')

@login_required
def blog_success(request):
    return render(request, 'admin/blog_success.html')


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
    return render(request, 'admin/admin_gallery.html', {
        'form': form,
        'images': images
    })
