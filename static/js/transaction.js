document.addEventListener('DOMContentLoaded', function () {
    let currentType = 'expense';
    loadCategories(currentType);

    document.querySelectorAll('.transaction-btn').forEach(button => {
        button.addEventListener('click', function () {
            const type = this.getAttribute('data-type');
            document.getElementById('transaction_type').value = type; // Исправлено на правильный селектор
            loadCategories(type);
        });
    });

    $('#category-select').on('change', function () {
        const categoryId = $(this).val();
        $('#category_id').val(categoryId); // Исправлено на правильный селектор
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
                    option.textContent = category.name ;
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

    document.getElementById('transaction-form').addEventListener('submit', function (event) {
        const categoryId = document.getElementById('category_id').value;
        if (!categoryId) {
            event.preventDefault();
            alert('Пожалуйста, выберите категорию.');
        }
    });
});
