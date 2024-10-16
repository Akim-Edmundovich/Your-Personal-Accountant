from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed

from transactions.forms import CategoryForm, SubcategoryForm
from transactions.models import Transaction, Category, Subcategory


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})


@login_required
def settings(request):
    return render(request, 'settings.html')


def categories_by_type(request):
    return render(request, 'categories/categories_by_type.html', )


# ------------ Categories ------------

@login_required
def categories_list(request, type_name):
    type_instance = Category.objects.get(type=type_name)
    categories = Category.objects.filter(type=type_instance)

    return render(request, 'categories/category_list.html',
                  {'categories': categories,
                   'type': type_instance})


@login_required
def category_create(request):
    form = CategoryForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user

            try:
                category.save()
                return redirect('categories_list', category.type.name)
            except IntegrityError:
                form.add_error('name', 'Category already exist.')
        else:
            return render(request, 'categories/category_form.html',
                          {'form': form})

    context = {
        'form': form,
    }
    return render(request,
                  'categories/category_form.html',
                  context)


@login_required
def update_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    form = CategoryForm(request.POST or None, instance=category)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('categories_list', type_name=category.type.name)

    return render(request,
                  'categories/category_update.html',
                  {'form': form,
                   'category': category})


@login_required
def delete_category(request, category_pk):
    category = get_object_or_404(Category, id=category_pk)

    if request.method == 'POST':
        category.delete()
        return HttpResponse('')

    return HttpResponseNotAllowed('Not Allowed')


@login_required
def detail_category(request, category_pk):
    category = Category.objects.get(id=category_pk)

    return render(request, 'categories/category_detail.html',
                  {'category': category})


@login_required
def category_form(request):
    form = CategoryForm()
    context = {
        'form': form
    }

    return render(request,
                  'categories/category_form.html',
                  context)


@login_required
def category_settings(request):
    return render(request, 'category_settings.html')


# ------------ Subcategories ------------

@login_required
def subcategories_list(request, category_pk):
    category = Category.objects.get(id=category_pk)
    subcategories = Subcategory.objects.filter(category=category)

    context = {
        'category': category,
        'subcategories': subcategories
    }
    return render(request,
                  'subcategories/subcategory_list.html',
                  context)


@login_required
def subcategory_create(request, category_pk):
    category = Category.objects.get(id=category_pk)
    form = SubcategoryForm(request.POST or None,
                           initial={'category': category})

    if request.method == 'POST':
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.category = category
            subcategory.user = request.user
            subcategory.save()
            return redirect('subcategories_list', category.id)

        else:
            return render(request, 'subcategories/subcategory_form.html',
                          {'form': form})

    context = {
        'category': category,
        'form': form
    }
    return render(request, 'subcategories/subcategory_form.html', context)


@login_required
def subcategory_detail(request, category_pk):
    category = Category.objects.get(id=category_pk)

    form = SubcategoryForm(request.POST or None, initial={'category': category})

    return render(request, 'categories/category_detail.html',
                  {'category': category,
                   'form': form})


@login_required
def subcategory_update(request, category_pk):
    subcategory = Subcategory.objects.get(id=category_pk)
    form = SubcategoryForm(request.POST or None, instance=subcategory)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('subcategories_list', subcategory.category.id)

    context = {
        'subcategory': subcategory,
        'form': form
    }
    return render(request,
                  'subcategories/subcategory_update.html',
                  context)


@login_required
def subcategory_delete(request, category_pk):
    subcategory = get_object_or_404(Subcategory, id=category_pk)

    if request.method == 'POST':
        subcategory.delete()
        return HttpResponse('')

    return HttpResponseNotAllowed('Not Allowed')


@login_required
def subcategory_form(request):
    form = SubcategoryForm()
    return render(request,
                  'subcategories/subcategory_form.html',
                  {'form': form})
