from django.shortcuts import render, redirect 
from .forms import ExhibitionForm 
from .models import Exhibition
# Create your views here.
def exhibition_view(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exhibition')  # or your desired success URL
    else:
        form = ExhibitionForm()
    return render(request, 'exhibition/exhibition.html', {'form': form})


def exhibition_list_view(request):
    exhibitions = Exhibition.objects.all().order_by('-id')
    return render(request, 'exhibition/exhibition_list.html', {'exhibitions': exhibitions})
