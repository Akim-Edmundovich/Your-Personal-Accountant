document.addEventListener('DOMContentLoaded', function () {
    let currentType = 'expense';
    loadCategories(currentType);

    const expenseBtn = document.getElementById('expense-btn')
    const incomeBtn = document.getElementById('income-btn')


    expenseBtn.classList.add('expense-btn')

    const alertField = document.getElementById('alert-field')


    document.querySelectorAll('.transaction-btn').forEach(button => {
        button.addEventListener('click', function () {
            const type = this.getAttribute('data-type');
            document.getElementById('transaction_type').value = type;
            loadCategories(type);


            if (type === 'expense') {
                expenseBtn.classList.add('expense-btn')
                incomeBtn.classList.remove('income-btn')
            } else {
                incomeBtn.classList.add('income-btn')
                expenseBtn.classList.remove('expense-btn')
            }


        });
    });

    $('#category-select').on('change', function () {
        const categoryId = $(this).val();
        $('#category_id').val(categoryId);
        loadSubcategories(categoryId);
    });

    $('#subcategory-select').on('change', function () {
        const subcategoryId = $(this).val();
        $('#subcategory').val(subcategoryId);
    });

    function loadQuantityType() {
        const quantityField = document.querySelector('input[name="quantity"]')
        const quantityTypeField = document.querySelector('select[name="quantity_type"]')

        if (!quantityField.value) {
            quantityTypeField.disabled = true
        }
        // Слушатель изменений для поля количества
        quantityField.addEventListener('input', function () {
            quantityTypeField.disabled = !quantityField.value;
        });
    }

    loadQuantityType();

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

                const subcategorySelect = document.getElementById('subcategory-select');
                subcategorySelect.innerHTML = ''; // Очищаем список подкатегорий
                const defaultSubOption = document.createElement('option');
                defaultSubOption.value = '';
                defaultSubOption.textContent = 'Subcategory';
                subcategorySelect.appendChild(defaultSubOption);
                $('#subcategory').val('');
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

    // ----------- Local Storage -------------
    let formData = {}
    const form = document.getElementById('transaction-form')
    // const LS = localStorage
    //
    // form.addEventListener('input', function (event) {
    //     formData[event.target.name] = event.target.value
    //     LS.setItem('formData', JSON.stringify(formData))
    // })
    //
    // // Восстановление данных
    // if (LS.getItem('formData')) {
    //     formData = JSON.parse(LS.getItem('formData'))
    //     console.log(formData)
    //
    //     for (let key in formData) {
    //         if ('button' in formData) {
    //
    //         } else {
    //             form.elements[key].value = formData[key]
    //         }
    //     }
    //     // Очистка формы и данных
    //     document.getElementById('clear-btn').addEventListener('click', function () {
    //         LS.removeItem('formData')
    //         formData = {}
    //         form.reset()
    //     })
    // }

    // ------------ Обработка формы -------------

    form.addEventListener('submit', function (event) {

        const categoryId = document.getElementById('category_id');
        const dateField = document.querySelector('input[name="created_at"]')
        const amountField = document.querySelector('input[name="amount"]')

        if (!amountField.value) {
            event.preventDefault();
            alertField.innerText = 'Enter amount'
            alertField.style.color = 'red'

        }
        if (!categoryId.value) {
            event.preventDefault();
            alertField.innerText = 'Select category'
            alertField.style.color = 'red'
        }

        if (!dateField.value) {
            event.preventDefault();
            alertField.innerText = 'Select date'
            alertField.style.color = 'red'
        }

        // if (amountField.value && categoryId.value && dateField.value) {
        //     LS.removeItem('formData')
        //     formData = {}
        //     form.reset()
        // }


    });

    $(document).ready(function () {
        $('.select2').select2({
            width: '100%', // Задаем ширину
            placeholder: 'Select',
            allowClear: true
        });
        $('#category-select').select2({
            width: '100%',
            placeholder: 'Category',
            allowClear: true,
        });
        $('#subcategory-select').select2({
            width: '100%',
            placeholder: 'Subcategory',
            allowClear: true
        });
    });

    // Получаем текущую дату
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0'); // Месяцы начинаются с 0
    const day = String(today.getDate()).padStart(2, '0');

    // Форматируем дату в формате YYYY-MM-DD
    const formattedDate = `${year}-${month}-${day}`;

    // Устанавливаем значение поля
    document.getElementById('created-at-input').value = formattedDate;
    document.getElementById('created-at-input').max = formattedDate;


    document.querySelector('input[name="quantity"]').addEventListener('keydown', function (e) {
        // Запрещаем ввод запятой
        if (e.key === ',') {
            e.preventDefault();
        }
    });
});
