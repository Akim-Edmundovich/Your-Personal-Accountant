from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Category, Subcategory
from .forms import TransactionForm


@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        transaction_type = request.POST.get('transaction_type')

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.type = transaction_type

            transaction.quantity_type = request.POST.get('quantity_type')
            category_id = request.POST.get('category')
            subcategory_id = request.POST.get('subcategory')

            if not category_id:
                form.add_error('category', 'Category ID is required')
                return render(request, 'add_transaction.html', {'form': form})

            try:
                transaction.category = Category.objects.get(
                    id=category_id,
                    user=request.user)

                if subcategory_id:
                    transaction.subcategory = Subcategory.objects.get(id=subcategory_id, user=request.user)

            except ObjectDoesNotExist:
                form.add_error('category',
                               'Selected category does not exist.')
                return render(request, 'add_transaction.html', {'form': form})

            transaction.save()

            print(transaction.type + 'SAVED')
            return redirect('transaction:add-transaction')

    else:
        form = TransactionForm()

    return render(request, 'add_transaction.html', {'form': form})


@login_required
def get_categories(request, type_name):
    categories = Category.objects.filter(type=type_name,
                                         user=request.user)
    data = [{"id": category.id, "name": category.name} for category in
            categories]
    return JsonResponse(data, safe=False)


@login_required
def get_subcategories(request, category_id):
    subcategories = Subcategory.objects.filter(category_id=category_id,
                                               category__user=request.user)
    data = [{'id': subcategory.id, 'name': subcategory.name} for subcategory in
            subcategories]
    return JsonResponse(data, safe=False)
