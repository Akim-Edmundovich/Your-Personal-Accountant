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
    const categorySelect = document.getElementById('category-select');
    categorySelect.addEventListener('change', function () {
        const categoryId = this.value;
        document.getElementById('category').value = categoryId; // Устанавливаем значение скрытого поля
        loadSubcategories(categoryId); // Загружаем подкатегории для выбранной категории
    });

    // Обработчик события для выбора подкатегории
    const subcategorySelect = document.getElementById('subcategory-select');
    subcategorySelect.addEventListener('change', function () {
        const subcategoryId = this.value;
        document.getElementById('subcategory').value = subcategoryId; // Устанавливаем значение скрытого поля
    });

    // Функция для загрузки категорий по типу транзакции
    function loadCategories(type) {
        fetch(`get_categories/${type}/`)
            .then(response => response.json())
            .then(data => {
                const categorySelect = document.getElementById('category-select');
                categorySelect.innerHTML = '<option value="">Выберите категорию</option>'; // Очищаем список категорий и добавляем заголовок

                data.forEach(category => {
                    const option = document.createElement('option');
                    option.value = category.id;
                    option.textContent = category.name;
                    categorySelect.appendChild(option); // Добавляем категорию в выпадающий список
                });

                // Очищаем подкатегории
                const subcategorySelect = document.getElementById('subcategory-select');
                subcategorySelect.innerHTML = '<option value="">Выберите подкатегорию</option>'; // Очищаем список подкатегорий
                document.getElementById('subcategory').value = ''; // Обнуляем скрытое поле подкатегории
            });
    }

    // // Обработчик события на кнопки типа транзакции
    // document.querySelectorAll('.transaction-btn').forEach(button => {
    //     button.addEventListener('click', function () {
    //         const type = this.getAttribute('data-type');
    //         document.getElementById('transaction_type').value = type;
    //         loadCategories(type); // Загружаем категории для выбранного типа
    //     });
    // });
    //
    // // Обработчик события для выбора категории
    // const categorySelect = document.getElementById('category-select');
    // categorySelect.addEventListener('change', function () {
    //     const categoryId = this.value;
    //
    //     if (categoryId) {
    //         // Показываем подкатегории и поля ввода
    //         document.getElementById('subcategory-container').style.display = 'block';
    //         document.getElementById('transaction-fields').style.display = 'block';
    //         loadSubcategories(categoryId); // Загружаем подкатегории
    //     } else {
    //         // Скрываем подкатегории и поля ввода, если категория не выбрана
    //         document.getElementById('subcategory-container').style.display = 'none';
    //         document.getElementById('transaction-fields').style.display = 'none';
    //     }
    // });
    //
    // // Функция для загрузки категорий по типу транзакции
    // function loadCategories(type) {
    //     fetch(`get_categories/${type}/`)
    //         .then(response => response.json())
    //         .then(data => {
    //             const categorySelect = document.getElementById('category-select');
    //             categorySelect.innerHTML = '<option value="">Выберите категорию</option>'; // Очищаем список категорий
    //
    //             data.forEach(category => {
    //                 const option = document.createElement('option');
    //                 option.value = category.id;
    //                 option.textContent = category.name;
    //                 categorySelect.appendChild(option);
    //             });
    //
    //             // Скрываем подкатегории и поля при изменении типа
    //             document.getElementById('subcategory-container').style.display = 'none';
    //             document.getElementById('transaction-fields').style.display = 'none';
    //         });
    // }

    // Функция для загрузки подкатегорий по ID категории
    function loadSubcategories(categoryId) {
        fetch(`get_subcategories/${categoryId}/`)
            .then(response => response.json())
            .then(data => {
                const subcategorySelect = document.getElementById('subcategory-select');
                subcategorySelect.innerHTML = '<option value="">Выберите подкатегорию</option>'; // Очищаем список подкатегорий

                data.forEach(subcategory => {
                    const option = document.createElement('option');
                    option.value = subcategory.id;
                    option.textContent = subcategory.name;
                    subcategorySelect.appendChild(option); // Добавляем субкатегорию в выпадающий список
                });
            });
    }

    // Обработчик отправки формы
    document.getElementById('form-rows').addEventListener('submit', function (event) {
        const categoryId = document.getElementById('category').value;
        if (!categoryId) {
            event.preventDefault(); // Остановить отправку формы, если категория не выбрана
            alert('Пожалуйста, выберите категорию.');
        }
    });
});
