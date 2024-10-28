from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import timezone

from datetime import timedelta, date

from transactions.models import *


@login_required
def test(request):
    return render(request, 'index.html')


@login_required
def list_transactions(request):
    return render(request, 'dashboard/dashboard.html')


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


@login_required
def expenses_filter_transactions(request, filter_type):
    today = timezone.now().date()
    expenses = Transaction.objects.none()

    if filter_type == 'day':
        expenses = Transaction.objects.filter(type='expense', created_at=today)

    elif filter_type == 'week':
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)

        expenses = Transaction.objects.filter(type='expense',
                                              created_at__range=[start_date,
                                                                 end_date])

    elif filter_type == 'month':
        expenses = Transaction.objects.filter(type='expense',
                                              created_at__year=today.year,
                                              created_at__month=today.month)

    elif filter_type == 'year':
        expenses = Transaction.objects.filter(type='expense',
                                              created_at__year=today.year)

    elif filter_type == 'period':
        date_range = request.GET.get('date_range')
        if date_range:
            start_date, end_date = date_range.split(',')
            expenses = Transaction.objects.filter(type='expense',
                                                  created_at__range=[start_date,
                                                                     end_date])
    context = {'expenses': expenses}

    html = render_to_string(
        'dashboard/filter_transactions/expenses_filter_transaction.html',
        context)

    return JsonResponse({'html': html})


def incomes_filter_transactions(request, filter_type):
    today = timezone.now().date()
    incomes = Transaction.objects.none()

    if filter_type == 'day':
        incomes = Transaction.objects.filter(type='income', created_at=today)

    elif filter_type == 'week':
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
        incomes = Transaction.objects.filter(type='income',
                                             created_at__range=[start_date,
                                                                end_date])

    elif filter_type == 'month':
        incomes = Transaction.objects.filter(type='income',
                                             created_at__year=today.year,
                                             created_at__month=today.month)

    elif filter_type == 'year':
        incomes = Transaction.objects.filter(type='income',
                                             created_at__year=today.year)

    elif filter_type == 'period':

        date_range = request.GET.get('date_range')

        if date_range:
            start_date, end_date = date_range.split(',')

            incomes = Transaction.objects.filter(type='income',

                                                 created_at__range=[start_date,
                                                                    end_date])

    context = {'incomes': incomes}

    html = render_to_string(
        'dashboard/filter_transactions/incomes_filter_transaction.html',
        context)

    return JsonResponse({'html': html})
