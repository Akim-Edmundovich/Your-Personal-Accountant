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
def create_category(request):
    ...


@login_required
def update_category(request):
    ...


@login_required
def delete_category(request):
    ...


@login_required
def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    subcategories = Subcategory.objects.filter(category=category)
    form = CategoryForm(request.POST or None, instance=category)

    context = {
        'form': form,
        'category': category,
        'subcategories': subcategories
    }

    return render(request, 'category_edit.html', context)


@login_required
def categories_list(request):
    categories = Category.objects.all()

    return render(request, 'category_settings.html',
                  {'categories': categories})


# ------------ Subcategories ------------

@login_required
def create_subcategory(request, pk):
    SubcategoryFormSet = inlineformset_factory(Category,
                                               Subcategory,
                                               fields=['name'],
                                               extra=2,
                                               can_delete=True)
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        formset = SubcategoryFormSet(request.POST, instance=category)
        if formset.is_valid():
            return redirect('settings:category_edit', pk=pk)

    else:
        formset = SubcategoryFormSet()
    return render(request, 'test.html', {'formset': formset})


@login_required
def update_subcategory(request, pk):
    ...


@login_required
def delete_subcategory(request, pk):
    ...
