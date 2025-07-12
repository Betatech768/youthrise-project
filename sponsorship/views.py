from django.shortcuts import render, redirect
from .forms import SponsorsForm
from .models import Sponsors

# View to handle sponsor form
def sponsorship_form_view(request):
    if request.method == 'POST':
        form = SponsorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sponsors_list')
    else:
        form = SponsorsForm()
    
    return render(request, 'sponsorship/sponsor_form.html', {'form': form})

# View to display list of sponsors
def sponsors_list_view(request):
    sponsors = Sponsors.objects.all().order_by('-id')
    return render(request, 'sponsorship/sponsorship_list.html', {'sponsors': sponsors})
