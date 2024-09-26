from django.shortcuts import render, redirect
from .froms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def dashboard(request):
    return render(request,
                  'account/dashboard.html')
