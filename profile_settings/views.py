from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

from transactions.forms import CategoryForm, SubcategoryForm
from transactions.models import *


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})


@login_required
def settings(request):
    return render(request, 'settings.html')


# ------------ Categories ------------

@login_required
def list_categories(request):
    categories = Category.objects.all()

    return render(request, 'category/list_categories.html',
                  {'categories': categories})


@login_required
def create_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('settings:list_categories')

    context = {'form': form}
    return render(request, 'category/create_category.html', context)


@login_required
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    subcategories = Subcategory.objects.filter(category=category)

    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('settings:list_categories')

    context = {'form': form, 'subcategories': subcategories}
    return render(request, 'category/update_category.html', context)


@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('settings:list_categories')

    context = {'category': category}
    return render(request, 'category/delete_category.html', context)


# ------------ Subcategories ------------


@login_required
def create_subcategory(request, pk):
    category = Category.objects.get(id=pk)
    form = SubcategoryForm()

    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.category = category
            subcategory.user = request.user
            subcategory.save()
            return redirect('settings:update_category', category.id)

    context = {
        'form': form,
        'category': category
    }

    return render(request, )




@login_required
def update_subcategory(request, pk):
    ...


@login_required
def delete_subcategory(request, pk):
    ...
