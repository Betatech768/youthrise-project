from django.shortcuts import render, redirect, get_object_or_404
from blogpost.forms import BlogPostForm
from blogpost.models import BlogImage, BlogPost
from django.http import JsonResponse, HttpResponse
from speakers.models import Speakers, SpeakerImage
from speakers.forms import SpeakerForm, SpeakerImageForm
from sponsorship.forms import SponsorshipPackageForm
from sponsorship.models import Sponsors
from exhibition.models import Exhibition
from registration_app.models import Registration
from galleries.forms import  ImageForm
from galleries.models import Image, Gallery
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, SponsorForm
from galleries.forms import ImageForm, GalleryForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from Images.forms import ImageUploadForm
from Images.models import GalleryImage
from .models import Document, ViewingDays, ConferenceDate, ConferenceVenue
from .forms import DocumentForm, ViewingDaysForm, ConferenceVenueForm, ConferenceDateForm
import os
from django.http import FileResponse
from main.models import Sponsor
from sponsorship.models import SponsorshipPackage
import openpyxl
from Newsletter.models import Newsletter
from Contact_Us.models import ContactUs as ContactMessage
from main.models import stream,stories
from main.forms import StreamForm


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
              
                return redirect('admin_page')
            else:
                messages.error(request, 'Invalid username or password.')

    return render(request, 'admin/admin_signin.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')

# Create your views here.

def admin(request):
    if request.user.is_authenticated:
        return render(request, 'admin/admin.html')
    else:
        return redirect('login')

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


@login_required
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
@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'admin/upload_document.html', {
        'form': form,
        'documents': documents
    })
@login_required
def delete_document(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        doc.delete()
        return redirect('document_list')
    return render(request, 'admin/delete_programme.html', {'doc': doc})

@login_required
def sponsors_manage(request):
    """Upload and list sponsors"""
    if request.method == "POST":
        form = SponsorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("sponsorsimage_list")
    else:
        form = SponsorForm()

    sponsors = Sponsor.objects.all()
    return render(request, "admin/sponsors_list.html", {"form": form, "sponsors": sponsors})
@login_required
@require_POST
def delete_sponsor(request, pk):
    """Delete sponsor via AJAX"""
    sponsor = get_object_or_404(Sponsor, pk=pk)
    sponsor.delete()
    return JsonResponse({"success": True})



# Update sponsorship package (for admin/staff)
@login_required
def update_package(request):
    # package = get_object_or_404(SponsorshipPackage, pk=pk)
    if request.method == 'POST':
        form = SponsorshipPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = SponsorshipPackageForm()

    sponsors = SponsorshipPackage.objects.all()
    return render(request, 'admin/update_package.html', {'form': form, 'sponsors': sponsors})
@login_required
@require_POST
def delete_sponsor_package(request, pk):
    """Delete sponsor via AJAX"""
    sponsor = get_object_or_404(SponsorshipPackage, pk=pk)
    sponsor.delete()
    return JsonResponse({"success": True})


@login_required
def export_registrations_excel(request):
    # Create workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Registrations"

    # Get model fields
    fields = [field.verbose_name for field in Registration._meta.fields if field.name != "id"]

    # Write header row
    ws.append(fields)

    # Write data rows
    for reg in Registration.objects.all():
        row = []
        for field in Registration._meta.fields:
            if field.name == "id":
                continue
            value = getattr(reg, field.name)

            # Handle ForeignKey
            if field.many_to_one and value is not None:
                value = str(value)

            row.append(value)
        ws.append(row)

    # Response as Excel file
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = 'attachment; filename="registrations.xlsx"'
    wb.save(response)

    return response

@login_required
def contact_messages(request):
    contact = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'admin/contact_messages.html', {'contact': contact})
@login_required
def newsletter_registrations(request):
    newsletter = Newsletter.objects.all().order_by('-created_at')
    return render(request, 'admin/newsletter_registrations.html', {'newsletter': newsletter})





def export_newsletters_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Newsletter"

    # Headers
    ws.append(["Email", "Created At"])

    # Data
    for obj in Newsletter.objects.all():
        ws.append([obj.email, obj.created_at.strftime("%Y-%m-%d %H:%M:%S")])

    # Response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=newsletters.xlsx"
    wb.save(response)
    return response




def export_exhibitions_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Exhibitions"

    # Headers
    ws.append([
        "First Name", "Last Name", "Email", "Organization", 
        "Industry Segment", "Organization Description", 
        "Primary Contact", "What Exhibiting", "Registration Date"
    ])

    # Data
    for obj in Exhibition.objects.all():
        ws.append([
            obj.firstname,
            obj.lastname,
            obj.email,
            obj.organization,
            obj.industry_segment,
            obj.organization_description,
            obj.primary_contact,
            obj.what_exhibiting,
            obj.created_at
        ])

    # Response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=exhibitions.xlsx"
    wb.save(response)
    return response



def export_sponsors_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sponsors"

    # Headers
    ws.append([
        "First Name", "Last Name", "Email", "Contact", "Package", "Registration Date" 
    ])

    # Data
    for obj in Sponsors.objects.all():
        ws.append([
            obj.firstname,
            obj.lastname,
            obj.email,
            obj.contact,
            str(obj.package),  # package name
            obj.created_at,
        ])

    # Response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=sponsors.xlsx"
    wb.save(response)
    return response

@login_required
def streaming(request):
    streamId  = stream.objects.all()
    if request.method == "POST":
        form = StreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('streaming')
    else:
        form = StreamForm()
        
    context = {'streamId': streamId,
               'form': form}
    return render(request, 'admin/stream.html', context)


@login_required
@require_POST
def delete_stream(request, pk):
    """Delete stream via AJAX"""
    streaming = get_object_or_404(stream, pk=pk)
    streaming.delete()
    return JsonResponse({"success": True})


@login_required
def story_list(request):
    sponsors = stories.objects.all().order_by('-id')
    return render(request, 'admin/story.html', {'sponsors': sponsors})



def export_stories_excel(request):
    # Create a new Excel workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Stories"

    # Define headers
    headers = [
        "Full Name",
        "Organization",
        "Specify Others",
        "Location",
        "Implementing",
        "Contact Person",
        "Contact Email",
        "Contact Phone",
        "Work Impact",
        "Describe Story",
        "Make Difference",
        "Speak About",
        "Organization Website",
        "Portfolio Link",
        "Social Media",
        "Created At",
    ]
    ws.append(headers)

    # Query all stories
    for story in stories.objects.all():
        ws.append([
            story.fullname,
            story.content,
            story.specify_others,
            story.Location,
            story.implementing,
            story.contact_person,
            story.contact_person_email,
            story.contact_person_phone,
            str(story.work_impact),  # in case it's a FK
            story.specify_works,
            story.describe_story,
            story.make_difference,
            story.speak_about,
            story.organization_website,
            story.portfolio_link,
            story.social_media,
            story.created_at.strftime("%Y-%m-%d %H:%M"),
        ])

    # Set response headers
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="stories.xlsx"'

    # Save workbook to response
    wb.save(response)

    return response

@require_POST
@csrf_exempt  # ⚠️ remove this if you add CSRF token in AJAX
def clear_model(request):
    Sponsors.objects.all().delete()
    return JsonResponse({"message": "All records cleared successfully!"})



@require_POST
@csrf_exempt  # ⚠️ remove this if you add CSRF token in AJAX
def clear_registration_model(request):
    Registration.objects.all().delete()
    return JsonResponse({"message": "All records cleared successfully!"})




@require_POST
@csrf_exempt  # ⚠️ remove this if you add CSRF token in AJAX
def clear_exhibition_model(request):
    Exhibition.objects.all().delete()
    return JsonResponse({"message": "All records cleared successfully!"})


@require_POST
@csrf_exempt  # ⚠️ remove this if you add CSRF token in AJAX
def clear_impactstories_model(request):
    stories.objects.all().delete()
    return JsonResponse({"message": "All records cleared successfully!"})

@login_required
def conferencedate (request):
    streamId = ConferenceDate.objects.all()
    message = ""
    form = ConferenceDateForm()
    if request.method == "POST":
        form = ConferenceDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("conferencedate")
        else:
            message= "Error submitting form"
    else: 
        form = ConferenceDateForm()

    return render( request, 'admin/conferncedate.html', {"form": form, "message": message, "streamId":streamId})

@login_required
def conferencevenue(request):
    streamId = ConferenceVenue.objects.all()
    message = ""
    venue_form = ConferenceVenueForm()
    if request.method == "POST":
        venue_form = ConferenceVenueForm(request.POST)
        if venue_form.is_valid():
            venue_form.save()
            return redirect ("conferencevenue")
        else:
            message= "error submitting form"
    else: 
        venue_form = ConferenceVenueForm()

    return render( request, 'admin/conferncevenue.html', {"venue_form": venue_form, "message": message, "streamId": streamId})



@login_required
def viewingday(request):
    streamId = ViewingDays.objects.all()
    message = ""
    form = ViewingDaysForm()
    if request.method == "POST":
        form = ViewingDaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("viewingday")
        else:
            message= "error submitting form"
    else: 
        form = ViewingDaysForm()

    return render( request, 'admin/viewingday.html', {"form": form, "message": message, "streamId": streamId})


def delete_viewingday(request, pk):
    """Delete a ViewingDay via AJAX"""
    viewingday = get_object_or_404(ViewingDays, pk=pk)
    viewingday.delete()
    return JsonResponse({"success": True})


def delete_conferenceday(request, pk):
    """Delete a ViewingDay via AJAX"""
    viewingday = get_object_or_404(ConferenceDate, pk=pk)
    viewingday.delete()
    return JsonResponse({"success": True})



def delete_conferencevenue(request, pk):
    """Delete a ViewingDay via AJAX"""
    viewingday = get_object_or_404(ConferenceVenue, pk=pk)
    viewingday.delete()
    return JsonResponse({"success": True})