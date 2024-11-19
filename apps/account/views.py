from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework import generics

from apps.account.models import CustomUser
from apps.account.serializers import CustomUserSerializer
from apps.transactions.models import Transaction

from .forms import CustomUserCreationForm


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


@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).values(
        'created_at',
        'category__name',
        'subcategory__name',
        'amount',
        'description')
    return render(request, 'account/dashboard.html',
                  {'transactions': transactions})


class CustomUserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().prefetch_related('user')
    serializer_class = CustomUserSerializer
