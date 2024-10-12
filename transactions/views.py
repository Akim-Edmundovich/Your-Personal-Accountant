from django.shortcuts import render, redirect
from .forms import TransactionForm
from django.http import HttpResponseBadRequest, JsonResponse
from .models import Category, Subcategory, Type, Transaction
from django.contrib.auth.decorators import login_required


@login_required
def choose_transaction_type(request, type_name):
    type_instance = Type.objects.get(name=type_name)

    return render(request, 'partials/transaction_type.html',
                  {'type': type_instance})


@login_required
def add_transaction(request, transaction_type: str):
    type = Transaction.objects.get(type=transaction_type)
    form = TransactionForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.type = type

            category_id = request.POST.get('category')

            category = Category.objects.get(id=category_id,
                                            user=request.user)

            subcategory_id = request.POST.get('subcategory')

            if subcategory_id:
                transaction.subcategory = Subcategory.objects.get(
                    id=subcategory_id
                )
            transaction.category = category
            transaction.save()

            return redirect('add_transaction')

    else:
        form = TransactionForm()

    categories = Category.objects.filter(user=request.user)

    return render(request, 'add_transaction.html', {
        'form': form,
        'categories': categories,
    })


# @login_required
# def add_transaction(request):
#     if request.method == 'POST':
#         transaction_type = request.POST.get('transaction_type')
#         form = TransactionForm(request.POST)
#
#         if form.is_valid():
#             transaction = form.save(commit=False)
#             transaction.user = request.user
#             transaction.type = transaction_type
#
#             category_id = request.POST.get('category')
#
#             if not category_id:
#                 return HttpResponseBadRequest('Category id is required.')
#
#             try:
#                 category = Category.objects.get(id=category_id,
#                                                 user=request.user)
#                 subcategory_id = request.POST.get('subcategory')
#
#                 # Проверка на подкатегорию
#                 if subcategory_id:
#                     transaction.subcategory = Subcategory.objects.get(
#                         id=subcategory_id)
#
#                 transaction.category = category
#             except Category.DoesNotExist:
#                 return HttpResponseBadRequest('Category does not exist.')
#             except Subcategory.DoesNotExist:
#                 # Если подкатегория не найдена, можем оставить её пустой
#                 transaction.subcategory = None
#
#             transaction.save()
#             return redirect('add_transaction')
#
#     else:
#         form = TransactionForm()
#
#     categories = Category.objects.filter(user=request.user)
#     return render(request, 'add_transaction.html', {
#         'form': form,
#         'categories': categories,
#     })


@login_required
def get_categories(request, type):
    categories = Category.objects.filter(type=type)
    data = [{"id": category.id, "name": category.name} for category in
            categories]
    return JsonResponse(data, safe=False)


@login_required
def get_subcategories(request, category_id):
    subcategories = Subcategory.objects.filter(category_id=category_id).values(
        'id', 'name')
    return JsonResponse(list(subcategories), safe=False)
