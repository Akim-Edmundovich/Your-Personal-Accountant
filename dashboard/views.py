from django.shortcuts import get_object_or_404, redirect, render
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
        amount = request.POST.get('amount')
        quantity = request.POST.get('quantity')
        quantity_type = request.POST.get('quantity_type')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')

        print(f'{type} - {category_id} - {subcategory_id} - {amount} - '
              f'{quantity} - {quantity_type} - {description} - {created_at}')

        try:
            Transaction.objects.filter(id=pk).update(
                type=type,
                amount=amount,
                category=category_id,
                subcategory=subcategory_id,
                quantity=quantity,
                quantity_type=quantity_type,
                description=description,
                created_at=created_at
            )

            print(
                f'Category - {transaction.category}, '
                f'subcategory - {transaction.subcategory}, '
                f'amount - {transaction.amount}')

            return redirect('dashboard:list_transactions')

        except Exception as e:
            print(f'Error while updating transaction: {e}')

    return redirect('dashboard:list_transactions')


@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, id=pk)

    if request.method == 'POST':
        try:
            transaction.delete()
            return redirect('dashboard:list_transactions')

        except transaction.DoesNotExist as e:
            print(f'Cannot delete transaction. Detail: {e}')

    context = {'transaction': transaction}
    return render(request, 'transaction/delete_transaction.html', context)
