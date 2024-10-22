from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from transactions.models import *


@login_required
def list_transactions(request):
    expenses = Transaction.objects.filter(type='expense')
    incomes = Transaction.objects.filter(type='income')

    context = {'expenses': expenses,
               'incomes': incomes}

    return render(request, 'dashboard/dashboard.html', context)


@login_required
def test(request):
    return render(request, 'index.html')


@login_required
def detail_transaction(request, pk):
    transaction = Transaction.objects.get(id=pk)
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    context = {
        'transaction': transaction,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'transaction/detail_transaction.html', context)


@login_required
def update_transaction(request, pk):
    transaction = Transaction.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        type = request.POST.get('transaction_type')
        category_id = request.POST.get('category')
        subcategory_id = request.POST.get('subcategory')
        quantity = request.POST.get('quantity')
        quantity_type = request.POST.get('quantity_type')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')

        try:

            transaction.type = type
            # transaction.category = category
            # transaction.subcategory = subcategory
            transaction.quantity = quantity
            transaction.quantity_type = quantity_type
            transaction.description = description
            transaction.created_at = created_at

            transaction.save()
            return redirect('dashboard:list_transactions')

        except Exception as e:
            print(f'Error while updating transaction: {e}')

    return redirect('dashboard:list_transactions')
