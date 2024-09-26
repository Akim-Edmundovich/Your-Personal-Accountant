// document.addEventListener('DOMContentLoaded', function () {
//     // Загружаем категории при загрузке страницы
//     let currentType = 'expense';
//     loadCategories(currentType);
//
//     // Обработчик события на кнопки типа транзакции
//     document.querySelectorAll('.transaction-btn').forEach(button => {
//         button.addEventListener('click', function () {
//             const type = this.getAttribute('data-type');
//             document.getElementById('transaction_type').value = type;
//             loadCategories(type); // Загружаем категории для выбранного типа
//         });
//     });
//
//
//     // Обработчик события для выбора категории
//     document.getElementById('category').addEventListener('change', function () {
//         const categoryId = this.value;
//         if (!categoryId) {
//             const subcategorySelect = document.getElementById('subcategory');
//             subcategorySelect.innerHTML = '<option value=""></option>';
//             return;
//         }
//
//
//         loadSubcategories(categoryId); // Загружаем подкатегории для выбранной категории
//     });
//
//
//     // Функция для загрузки категорий по типу транзакции
//     function loadCategories(type) {
//         fetch(`get_categories/${type}/`)
//             .then(response => response.json())
//             .then(data => {
//                 const categorySelect = document.getElementById('category');
//                 categorySelect.innerHTML = '<option value=""></option>'; // Сбрасываем список
//
//                 data.forEach(category => {
//                     const option = document.createElement('option');
//                     option.value = category.id;
//                     option.textContent = category.name;
//                     categorySelect.appendChild(option); // Добавляем категорию в список
//                 });
//             });
//     }
//
//     // Функция для загрузки подкатегорий по ID категории
//     function loadSubcategories(categoryId) {
//         fetch(`get_subcategories/${categoryId}/`)
//             .then(response => response.json())
//             .then(data => {
//                 const subcategorySelect = document.getElementById('subcategory');
//                 subcategorySelect.innerHTML = '<option value=""></option>'; // Сбрасываем список
//
//                 data.forEach(subcategory => {
//                     const option = document.createElement('option');
//                     option.value = subcategory.id;
//                     option.textContent = subcategory.name;
//                     subcategorySelect.appendChild(option); // Добавляем подкатегорию в список
//                 });
//             });
//     }
// });

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
            document.getElementById('selected_category').value = categoryId;

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
                });
            });
    }

    // Функция для загрузки подкатегорий по ID категории
    function loadSubcategories(categoryId) {
        fetch(`get_subcategories/${categoryId}/`)
            .then(response => response.json())
            .then(data => {
                const subcategorySelect = document.getElementById('subcategory');
                subcategorySelect.innerHTML = '<option value=""></option>'; // Сбрасываем список

                data.forEach(subcategory => {
                    const option = document.createElement('option');
                    option.value = subcategory.id;
                    option.textContent = subcategory.name;
                    subcategorySelect.appendChild(option); // Добавляем подкатегорию в список
                });
            });
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
            const categorySelect = document.getElementById('category');
            if (!categorySelect) {
                console.error('Element with id "id_category" not found');
                return; // Прерываем выполнение, если элемент не найден
            }

            // Очищаем текущие опции и добавляем новые
            categorySelect.innerHTML = '<option value="">Category</option>';
            data.forEach(category => {
                const option = document.createElement('option');
                option.value = category.id;
                option.textContent = category.name;
                categorySelect.appendChild(option);
            });

            // Очищаем подкатегории
            const subcategorySelect = document.getElementById('subcategory');
            if (subcategorySelect) {
                subcategorySelect.innerHTML = '<option value=""></option>';
            }
        })
        .catch(error => console.error('Error fetching categories:', error));
}

// Обработчик изменения для категории
document.getElementById('category').addEventListener('change', function () {
    const selectedCategory = this.value;

    if (selectedCategory) {
        // Получаем подкатегории по выбранной категории
        fetch(`/transaction/get_subcategories/${selectedCategory}/`)
            .then(response => response.json())
            .then(data => {
                const subcategorySelect = document.getElementById('subcategory');
                subcategorySelect.innerHTML = '<option value=""></option>';
                data.forEach(subcategory => {
                    const option = document.createElement('option');
                    option.value = subcategory.id;
                    option.textContent = subcategory.name;
                    subcategorySelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching subcategories:', error));
    } else {
        // Если категория не выбрана, очищаем подкатегории
        const subcategorySelect = document.getElementById('subcategory');
        if (subcategorySelect) {
            subcategorySelect.innerHTML = '<option value=""></option>';
        }
    }
});