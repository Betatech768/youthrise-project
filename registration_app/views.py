from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration_app/register.html', {'form': form})

def registration_list_view(request):
    registrations = Registration.objects.all()
    return render(request, 'registration_app/registration_list.html', {'registrations': registrations})
