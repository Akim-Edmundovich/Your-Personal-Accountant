from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics

from transactions.models import Transaction
from account.models import CustomUser
from .forms import CustomUserCreationForm
from account.serializers import CustomUserSerializer


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
