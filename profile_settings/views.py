from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, inlineformset_factory

from transactions.forms import *
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
def categories_page(request):
    form = CategoryForm(initial={'type': 'expense'})
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            if not Category.objects.filter(name=category.name).exists():
                category.save()
                return redirect('settings:categories_page')
            else:
                form.add_error('name', 'Category already exists!')

    categories = Category.objects.filter(user=request.user)
    context = {'form': form,
               'categories': categories}
    return render(request, 'category/categories_page.html', context)


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

    context = {'form': form,
               'subcategories': subcategories,
               'category': category}

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
    SubcategoryFormSet = formset_factory(SubcategoryForm,
                                         extra=2,
                                         can_delete=True,
                                         can_delete_extra=True,
                                         )
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        formset = SubcategoryFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    if form.instance.pk:
                        form.instance.delete()
                else:
                    subcategory = form.save(commit=False)
                    subcategory.category = category
                    subcategory.user = request.user
                    if form.cleaned_data:
                        if form.cleaned_data[
                            'name'
                        ] not in Subcategory.objects.filter(
                            category=category
                        ):
                            subcategory.save()
            return redirect('settings:update_category', category.id)

    formset = SubcategoryFormSet()

    context = {
        'formset': formset,
        'category': category
    }

    return render(request, 'subcategory/create_subcategory.html', context)


@login_required
def update_subcategory(request, pk):
    subcategory = Subcategory.objects.get(id=pk)
    form = SubcategoryForm(instance=subcategory)

    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('settings:update_category', subcategory.category.id)

    context = {'form': form,
               'subcategory': subcategory}
    return render(request, 'subcategory/update_subcategory.html', context)


@login_required
def delete_subcategory(request, pk):
    subcategory = get_object_or_404(Subcategory, id=pk)

    if request.method == 'POST':
        subcategory.delete()
        return redirect('settings:update_category', subcategory.category.id)

    context = {
        'subcategory': subcategory
    }
    return render(request, 'subcategory/delete_subcategory.html', context)


@login_required
def form_subcategory(request):
    form = SubcategoryForm()
    context = {'form': form}
    return render(request, 'subcategory/form_subcategory.html', context)
