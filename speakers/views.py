# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SpeakerForm, SpeakerImageForm
from .models import Speakers, SpeakerImage
from django.http import JsonResponse
def create_speaker(request):
    if request.method == 'POST':
        speaker_form = SpeakerForm(request.POST)
        image_form = SpeakerImageForm(request.POST, request.FILES)

        if speaker_form.is_valid() and image_form.is_valid():
            speaker = speaker_form.save()
            image = image_form.save(commit=False)
            image.blog = speaker  # Link the image to the speaker
            image.save()
            return redirect('speaker_list')

    else:
        speaker_form = SpeakerForm()
        image_form = SpeakerImageForm()

    return render(request, 'speakers/create_speaker.html', {
        'speaker_form': speaker_form,
        'image_form': image_form,
    })

def speaker_list(request):
    speakers = Speakers.objects.all().order_by('-created_at')
    return render(request, 'speakers/speaker_list.html', {'speakers': speakers})

# Edit speaker
def edit_speaker(request, speaker_id):
    speaker = get_object_or_404(Speakers, pk=speaker_id)
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES, instance=speaker)
        files = request.FILES.getlist('images')

        if form.is_valid():
            updated_speaker = form.save()
            for img in files:
                SpeakerImage.objects.create(blog=updated_speaker, image=img)
            return redirect('speaker_list')
    else:
        form = SpeakerForm(instance=speaker)
    
    return render(request, 'speakers/edit_speaker.html', {
        'form': form,
        'speaker': speaker,
        'images': speaker.images.all(),
    })


# Delete speaker
def delete_speaker(request, speaker_id):
    speaker = get_object_or_404(Speakers, pk=speaker_id)
    if request.method == 'POST':
        speaker.delete()
        return redirect('speaker_list')
    return render(request, 'speakers/delete_speaker_confirm.html', {'speaker': speaker})



