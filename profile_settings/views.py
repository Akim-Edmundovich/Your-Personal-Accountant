from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

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
def edit_email(request):
    user_email = request.user.email

    if request.method == 'POST':
        form = UpdateEmailForm(request.POST)

        if form.is_valid():
            new_email = form.cleaned_data.get('email')

            if CustomUser.objects.filter(email=new_email).exists():
                messages.warning(request, 'Email already exists')
            else:
                CustomUser.objects.filter(id=request.user.id).update(
                    email=new_email)
                print('Email was changed on: ' + new_email)
                return redirect('settings:profile_edit_page')
    else:
        form = UpdateEmailForm()

    return render(request, 'profile/edit_email.html', {
        'form': form,
        'messages': messages.get_messages(request)
    })


@login_required
def check_password_page(request):
    if request.method == 'POST':
        entered_password = request.POST.get('password')
        user = request.user

        if user.check_password(entered_password):
            return redirect('settings:edit_email')
        else:
            messages.warning(request, 'Incorrect password')
    return render(request, 'profile/check_password.html')


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
