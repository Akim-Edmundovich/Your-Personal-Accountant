from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed

from transactions.forms import CategoryForm, SubcategoryForm
from transactions.models import Transaction, Category, Subcategory, Type


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})


@login_required
def settings(request):
    return render(request, 'settings.html')


def categories_by_type(request, type_name='expense'):
    type_instance = Type.objects.get(name=type_name)
    categories = Category.objects.filter(type=type_name)

    context = {
        'type': type_instance,
        'categories': categories
    }

    return render(request, 'categories_by_types.html', context)


# ------------ Categories ------------

@login_required
def categories_list(request):
    categories = Category.objects.all()

    return render(request, 'categories/category_list.html',
                  {'categories': categories})


@login_required
def create_category(request, type_name):
    type = Type.objects.get(name=type_name)
    form = CategoryForm(request.POST or None, initial={'type': type})

    if request.method == 'POST':
        if form.is_valid():
            category = form.save(commit=False)
            # category.type = form.cleaned_data['type']
            category.type = type
            category.save()
            return redirect('categories_list', pk=type.id)

        else:
            return render(request, 'categories/category_form.html',
                          {'form': form})

    context = {
        'form': form,
        'type': type,
    }
    return render(request,
                  'categories/category_form.html',
                  context)


@login_required
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=category)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('categories_list')

    return render(request,
                  'categories/category_form.html',
                  {'form': form})


@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, id=pk)

    if request.method == 'POST':
        category.delete()
        return HttpResponse('')

    return HttpResponseNotAllowed('Not Allowed')


@login_required
def detail_category(request, pk):
    category = Category.objects.get(id=pk)

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


# ------------ Subcategories ------------

@login_required
def subcategories_list(request, pk):
    category = Category.objects.get(id=pk)
    subcategories = Subcategory.objects.filter(category=category)

    return render(request,
                  'subcategories/subcategory_list.html',
                  {'category': category,
                   'subcategories': subcategories})


@login_required
def subcategory_create(request, pk):
    category = Category.objects.get(pk)
    form = SubcategoryForm(request.POST or None,
                           initial={'category': category})

    if request.method == 'POST':
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.category = category
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
def subcategory_detail(request, pk):
    category = Category.objects.get(id=pk)
    form = SubcategoryForm(request.POST or None, initial={'category': category})

    if request.method == 'POST':
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.category = category
            subcategory.save()
            return redirect('subcategories_list', category.id)

        else:
            return render(request, 'subcategories/subcategory_form.html',
                          {'form': form})

    context = {
        'category': category,
        'form': form
    }
    return render(request,
                  'subcategories/subcategory_form.html',
                  context)


@login_required
def subcategory_update(request, pk):
    subcategory = Subcategory.objects.get(id=pk)
    form = SubcategoryForm(request.POST or None, instance=subcategory)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('subcategories_list', pk=subcategory.category.id)

    context = {
        'category': subcategory,
        'form': form
    }
    return render(request,
                  'subcategories/subcategory_update.html',
                  context)


@login_required
def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, id=pk)

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
