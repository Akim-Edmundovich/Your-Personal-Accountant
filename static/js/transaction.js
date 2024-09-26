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
    const categoryGrid = document.querySelector('.category-grid');

    // Убедимся, что у нас есть сетка категорий
    categoryGrid.addEventListener('click', function (event) {
        const clickedButton = event.target.closest('.category-button');
        if (clickedButton) {
            // Убираем класс active у всех кнопок
            categoryGrid.querySelectorAll('.category-button').forEach(btn => btn.classList.remove('active'));
            // Добавляем класс active к нажатой кнопке
            clickedButton.classList.add('active');

            // Получаем ID категории из атрибута data-id
            const categoryId = clickedButton.getAttribute('data-id');

            // Устанавливаем значение скрытого поля
            document.getElementById('category').value = categoryId;

            // Загружаем подкатегории для выбранной категории
            loadSubcategories(categoryId);
        }
    });

    // Функция для загрузки категорий по типу транзакции
    function loadCategories(type) {
        fetch(`get_categories/${type}/`)
            .then(response => response.json())
            .then(data => {
                const categoryGrid = document.querySelector('.category-grid');
                categoryGrid.innerHTML = ''; // Очищаем список категорий

                data.forEach(category => {
                    const button = document.createElement('div');
                    button.classList.add('category-button');
                    button.setAttribute('data-id', category.id);
                    button.textContent = category.name;
                    categoryGrid.appendChild(button); // Добавляем категорию в сетку

                    // Очищаем субкатегории
                    const subcategoryGrid = document.querySelector('.subcategory-grid');
                    subcategoryGrid.innerHTML = ''; // Очищаем список подкатегорий
                });
            });
    }


    // Функция для загрузки подкатегорий по ID категории
    function loadSubcategories(categoryId) {
        fetch(`get_subcategories/${categoryId}/`)
            .then(response => response.json())
            .then(data => {
                const subcategoryGrid = document.querySelector('.subcategory-grid');
                subcategoryGrid.innerHTML = ''; // Очищаем список подкатегорий

                // Убираем значение подкатегории, если подкатегорий нет
                const subcategoryInput = document.getElementById('subcategory');
                if (data.length === 0) {
                    subcategoryInput.value = ''; // Убираем значение, если нет подкатегорий
                    return; // Прерываем выполнение, если подкатегорий нет
                }

                data.forEach(subcategory => {
                    const button = document.createElement('div');
                    button.classList.add('category-button'); // Используем тот же класс для стилизации
                    button.setAttribute('data-id', subcategory.id);
                    button.textContent = subcategory.name;
                    subcategoryGrid.appendChild(button); // Добавляем субкатегорию в сетку
                });

                // Если подкатегории загружены, назначаем значение первой подкатегории
                subcategoryInput.value = data[0].id; // Устанавливаем это значение в скрытое поле
            });
    }

    // Обработчик отправки формы
    document.getElementById('form-rows').addEventListener('submit', function (event) {
        const categoryId = document.getElementById('category').value;
        const subcategoryId = document.getElementById('subcategory').value; // Получаем значение подкатегории
        if (!categoryId) {
            event.preventDefault(); // Остановить отправку формы, если категория не выбрана
            alert('Please select a category.');
        } else if (data.length > 0 && !subcategoryId) { // Проверяем, если есть подкатегории
            event.preventDefault(); // Остановить отправку формы, если подкатегория не выбрана
            alert('Please select a subcategory.');
        }
    });


// Функция для получения категорий
    function fetchCategories(type) {
        // Отправляем GET-запрос на сервер для получения категорий по типу
        fetch(`/transaction/get_categories/${type}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                const categoryGrid = document.querySelector('.category-grid');
                if (!categoryGrid) {
                    console.error('Element with id "id_category" not found');
                    return; // Прерываем выполнение, если элемент не найден
                }

                // Очищаем текущие опции и добавляем новые
                categoryGrid.innerHTML = '';
                data.forEach(category => {
                    const button = document.createElement('div');
                    button.classList.add('category-button');
                    button.value = category.id;
                    button.textContent = category.name;
                    categoryGrid.appendChild(button);
                });

                // Очищаем подкатегории
                const subcategoryGrid = document.getElementById('.subcategory-grid');
                if (subcategoryGrid) {
                    subcategoryGrid.innerHTML = '';
                }
            })
            .catch(error => console.error('Error fetching categories:', error));
    }
})
