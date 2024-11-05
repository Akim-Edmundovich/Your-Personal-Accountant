from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from transactions.forms import *
from transactions.models import *
from account.forms import *


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})


@login_required
def settings(request):
    return render(request, 'settings.html')


# ------------ Profile settings -----------

@login_required
def profile_edit_page(request):
    user = request.user
    email = user.email

    return render(request, 'profile/profile_edit_page.html', {'email': email})


@login_required
def email_edit(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('settings:email_edit')

    form = UserForm(instance=user)
    return render(request, 'profile/edit_email.html')


# ------------ Categories ------------

@login_required
def page_categories(request):
    form = CategoryForm(initial={'type': 'expense'})
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            if not Category.objects.filter(name=category.name).exists():
                category.save()
                return redirect('settings:page_categories')
            else:
                form.add_error('name', 'Category already exists!')

    categories = Category.objects.filter(user=request.user)
    context = {'form': form,
               'categories': categories}
    return render(request, 'category/page_categories.html', context)


@login_required
def page_update_category(request, pk):
    category = Category.objects.get(id=pk)
    subcategories = Subcategory.objects.filter(category=category)

    context = {
        'category': category,
        'subcategories': subcategories
    }
    return render(request, 'category/page_update_category.html', context)


@login_required
def update_category(request, pk):
    category = Category.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        name = request.POST.get('category_name')
        type = request.POST.get('type')

        print(f'Category name: {name}, type: {type}')

        try:
            if not Category.objects.filter(user=request.user,
                                           name=name,
                                           type=type).exclude(
                id=category.id).exists():
                category.name = name
                category.type = type
                category.save()
                print(f'Category "{name}" was updated')
            else:
                print(f'Category "{name}" already exists.')

        except Exception as e:
            print(f'Error while updating category {e}')

    return redirect('settings:page_categories')


@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('settings:page_categories')

    context = {'category': category}
    return render(request, 'category/delete_category.html', context)


# ------------ Subcategories ------------


@login_required
def create_subcategory(request):
    if request.method == 'POST':
        name = request.POST.get('subcategory_name')
        category_id = request.POST.get('category_id')

        try:
            category = Category.objects.get(id=category_id)
            subcategory_obj = Subcategory.objects.create(name=name,
                                                         category=category,
                                                         user=request.user)

            subcategory_obj.save()
        except Exception as e:
            print(f'Error while creating subcategory {e}')

    return redirect('settings:page_update_category', pk=category_id)


@login_required
def update_subcategory(request, pk):
    subcategory = Subcategory.objects.get(id=pk)
    category = Category.objects.get(subcategory=subcategory)
    form = SubcategoryForm(instance=subcategory)

    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('settings:page_update_category',
                            subcategory.category.id)

    context = {'form': form,
               'subcategory': subcategory,
               'category': category}
    return render(request, 'subcategory/update_subcategory.html', context)


@login_required
def delete_subcategory(request, pk):
    subcategory = get_object_or_404(Subcategory, id=pk)

    if request.method == 'POST':
        subcategory.delete()
        return redirect('settings:page_update_category',
                        subcategory.category.id)

    context = {
        'subcategory': subcategory
    }
    return render(request, 'subcategory/delete_subcategory.html', context)


@login_required
def form_subcategory(request):
    form = SubcategoryForm()
    context = {'form': form}
    return render(request, 'subcategory/form_subcategory.html', context)
