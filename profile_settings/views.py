from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from transactions.forms import CategoryForm, SubcategoryForm
from transactions.models import Category, Subcategory


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})


@login_required
def settings(request):
    return render(request, 'settings.html')


# ------------ Categories ------------

@login_required
def category_edit(request, pk):
    category = Category.objects.get(id=pk, user=request.user)
    subcategories = Subcategory.objects.filter(category=category)

    SubcategoryFormSet = modelformset_factory(Subcategory,
                                              form=SubcategoryForm,
                                              extra=0)
    subcategory_forms = SubcategoryFormSet(queryset=subcategories)
    form = CategoryForm(request.POST or None, instance=category)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        subcategory_forms = SubcategoryFormSet(request.POST)
        if subcategory_forms.is_valid():
            subcategory_forms.save()

        return redirect('settings:category_edit', pk=pk)

    return render(request, 'category_edit.html',
                  {'form': form,
                   'subcategory_forms': subcategory_forms,
                   'category': category})


@login_required
def categories_list(request):
    categories = Category.objects.all()

    return render(request, 'category_settings.html',
                  {'categories': categories})


# ------------ Subcategories ------------

@login_required
def subcategory_edit(request, subcategory_pk, category_pk):
    subcategory = Subcategory.objects.get(category=category_pk,
                                          id=subcategory_pk,
                                          user=request.user)
    form = SubcategoryForm(request.POST or None,
                           instance=subcategory)

    if form.is_valid():
        form.save()
        return redirect('settings:category_edit')

    return render(request, 'subcategory_edit.html',
                  {'form': form})


@login_required
def subcategory_delete(request, subcategory_pk):
    try:
        subcategory = Subcategory.objects.get(id=subcategory_pk)
        subcategory.delete()
        return JsonResponse({'success': True})

    except Subcategory.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Subcategory not found'},
                            status=404)

