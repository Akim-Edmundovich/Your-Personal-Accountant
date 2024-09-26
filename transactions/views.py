from django.shortcuts import render, redirect
from .forms import TransactionForm
from django.http import HttpResponseBadRequest, JsonResponse
from .models import Category, Subcategory
from django.contrib.auth.decorators import login_required


@login_required
def add_transaction(request):
    # Проверяем, является ли запрос POST
    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.type = transaction_type  # Добавляем тип транзакции

            category_id = request.POST.get('category')

            if not category_id:
                return HttpResponseBadRequest('Category id is required.')

            try:
                category = Category.objects.get(id=category_id,
                                                user=request.user)
                subcategory = Subcategory.objects.get(category=category)
                transaction.category = category
                transaction.subcategory = subcategory
            except Category.DoesNotExist:
                return HttpResponseBadRequest('Category does not exist.')

            transaction.save()
            return redirect('add_transaction')

    else:
        form = TransactionForm()  # Создаём пустую форму для GET-запроса

    categories = Category.objects.filter(user=request.user)
    return render(request, 'add_transaction.html', {
        'form': form,
        'categories': categories,

    })


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
