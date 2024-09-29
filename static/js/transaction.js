document.addEventListener('DOMContentLoaded', function () {
    // Загружаем категории при загрузке страницы
    let currentType = 'expense';
    loadCategories(currentType);

    // Обработчик события на кнопки типа транзакции
    document.querySelectorAll('.transaction-btn').forEach(button => {
        button.addEventListener('click', function () {
            const type = this.getAttribute('data-type');
            document.getElementById('transaction_type').value = type;
            loadCategories(type); // Загружаем категории для выбранного типа
        });
    });

    // Обработчик события для выбора категории
    $('#category-select').on('change', function () {
        const categoryId = $(this).val();
        $('#category').val(categoryId); // Устанавливаем значение скрытого поля
        loadSubcategories(categoryId); // Загружаем подкатегории для выбранной категории
    });

    // Обработчик события для выбора подкатегории
    $('#subcategory-select').on('change', function () {
        const subcategoryId = $(this).val();
        $('#subcategory').val(subcategoryId); // Устанавливаем значение скрытого поля
    });

    // Функция для загрузки категорий по типу транзакции
    function loadCategories(type) {
        fetch(`get_categories/${type}/`)
            .then(response => response.json())
            .then(data => {
                const categorySelect = $('#category-select');
                categorySelect.empty(); // Очищаем список категорий
                categorySelect.append('<option value="">Выберите категорию</option>'); // Добавляем заголовок

                data.forEach(category => {
                    categorySelect.append(new Option(category.name, category.id)); // Добавляем категорию в выпадающий список
                });

                // Очищаем подкатегории
                const subcategorySelect = $('#subcategory-select');
                subcategorySelect.empty(); // Очищаем список подкатегорий
                subcategorySelect.append('<option value="">Выберите подкатегорию</option>'); // Добавляем заголовок
                $('#subcategory').val(''); // Обнуляем скрытое поле подкатегории
            })
            .catch(error => console.error('Ошибка загрузки категорий:', error)); // Обработка ошибок
    }

    // Функция для загрузки подкатегорий по ID категории
    function loadSubcategories(categoryId) {
        if (!categoryId) {
            // Если категория не выбрана, очищаем подкатегории
            const subcategorySelect = $('#subcategory-select');
            subcategorySelect.empty(); // Очищаем список подкатегорий
            subcategorySelect.append('<option value="">Выберите подкатегорию</option>'); // Добавляем заголовок
            $('#subcategory').val(''); // Обнуляем скрытое поле подкатегории
            return; // Прерываем выполнение функции
        }

        fetch(`get_subcategories/${categoryId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Сеть не в порядке');
                }
                return response.json();
            })
            .then(data => {
                const subcategorySelect = $('#subcategory-select');
                subcategorySelect.empty(); // Очищаем список подкатегорий
                subcategorySelect.append('<option value="">Выберите подкатегорию</option>'); // Добавляем заголовок

                data.forEach(subcategory => {
                    subcategorySelect.append(new Option(subcategory.name, subcategory.id)); // Добавляем субкатегорию в выпадающий список
                });
            })
            .catch(error => console.error('Ошибка загрузки подкатегорий:', error)); // Обработка ошибок
    }

    // Обработчик отправки формы
    document.getElementById('transaction-form').addEventListener('submit', function (event) {
        const categoryId = document.getElementById('category').value;
        if (!categoryId) {
            event.preventDefault(); // Остановить отправку формы, если категория не выбрана
            alert('Пожалуйста, выберите категорию.');
        }
    });
});
