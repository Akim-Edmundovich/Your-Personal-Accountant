document.addEventListener('DOMContentLoaded', function () {
    const currentType = document.getElementById('transaction_type').value;
    const expenseBtn = document.getElementById('expense-btn');
    const incomeBtn = document.getElementById('income-btn');

    // Установка начального состояния кнопок на основе текущего типа транзакции
    if (currentType === 'expense') {
        expenseBtn.classList.add('expense-btn');
        loadCategories(currentType);  // Загружаем категории при загрузке страницы
    } else if (currentType === 'income') {
        incomeBtn.classList.add('income-btn');
        loadCategories(currentType);  // Загружаем категории при загрузке страницы
    }

    document.querySelectorAll('.transaction-btn').forEach(button => {
        button.addEventListener('click', function () {
            const type = this.getAttribute('data-type');
            document.getElementById('transaction_type').value = type;
            loadCategories(type);

            // Обновление классов кнопок
            if (type === 'expense') {
                expenseBtn.classList.add('expense-btn');
                incomeBtn.classList.remove('income-btn');
            } else {
                incomeBtn.classList.add('income-btn');
                expenseBtn.classList.remove('expense-btn');
            }
        });
    });

    $('#category-select').on('change', function () {
        const categoryId = $(this).val();
        loadSubcategories(categoryId);
    });

    $('#subcategory-select').on('change', function () {
        const subcategoryId = $(this).val();
        $('#subcategory').val(subcategoryId);
    });

    function loadCategories(type) {
        axios.get(`/transaction/get_categories/${type}/`)
            .then(response => {
                const data = response.data;
                const categorySelect = document.getElementById('category-select');
                categorySelect.innerHTML = ''; // Очищаем список категорий

                // Создаем и добавляем опцию "Выберите категорию"
                const defaultOption = document.createElement('option');
                defaultOption.value = '';
                defaultOption.textContent = 'Category';
                categorySelect.appendChild(defaultOption);

                data.forEach(category => {
                    const option = document.createElement('option');
                    option.value = category.id;
                    option.textContent = category.name;
                    categorySelect.appendChild(option);
                });

                // После загрузки категорий подгружаем соответствующие подкатегории
                const selectedCategoryId = categorySelect.value;
                loadSubcategories(selectedCategoryId);
            })
            .catch(error => {
                console.error('Ошибка загрузки категорий:', error);
                alert('Ошибка загрузки категорий. Попробуйте еще раз.');
            });
    }

    function loadSubcategories(categoryId) {
        if (!categoryId) {
            const subcategorySelect = document.getElementById('subcategory-select');
            subcategorySelect.innerHTML = ''; // Очищаем подкатегории
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.textContent = 'Subcategory';
            subcategorySelect.appendChild(defaultOption);
            $('#subcategory').val('');
            return;
        }

        axios.get(`/transaction/get_subcategories/${categoryId}/`)
            .then(response => {
                const data = response.data;
                const subcategorySelect = document.getElementById('subcategory-select');
                subcategorySelect.innerHTML = ''; // Очищаем подкатегории
                const defaultOption = document.createElement('option');
                defaultOption.value = '';
                defaultOption.textContent = 'Subcategory';
                subcategorySelect.appendChild(defaultOption);

                data.forEach(subcategory => {
                    const option = document.createElement('option');
                    option.value = subcategory.id;
                    option.textContent = subcategory.name;
                    subcategorySelect.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Ошибка загрузки подкатегорий:', error);
                alert('Ошибка загрузки подкатегорий. Попробуйте еще раз.');
            });
    }

    // Настройка select2
    $(document).ready(function () {
        $('.select2').select2({
            width: '100%',
            placeholder: 'Select',
            allowClear: true
        });
    });

    // Установка даты и ограничений по дате
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;
    document.getElementById('created-at-input').max = formattedDate;

    // Обработка отправки формы
    document.getElementById('transaction-form').addEventListener('submit', function (event) {
        const alertField = document.getElementById('alert-field');
        const amountField = document.querySelector('input[name="amount"]');
        const categoryField = document.getElementById('category-select');

        alertField.innerText = '';

        if (!amountField.value) {
            event.preventDefault();
            alertField.innerText = 'Enter amount';
            alertField.style.color = 'red';
            return;
        }

        if (!categoryField.value) {
            event.preventDefault();
            alertField.innerText = 'Select category';
            alertField.style.color = 'red';
            return;
        }
    });

});
