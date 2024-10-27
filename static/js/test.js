const typeBtn = document.getElementById('select-transaction')
const saveCategoryBtn = document.getElementById('save-subcategory-btn')
const categoryInput = document.getElementById('subcategory-input');
const categoryList = document.getElementById('subcategory-list');
const currentType = 'expense'

// Load categories by type button
typeBtn.addEventListener('change', function () {
    loadCategories(typeBtn.value)
})
loadCategories(currentType)


function loadCategories(type) {
    axios.get(`/transaction/get_categories/${type}/`)
        .then(response => {
            const data = response.data;
            const categorySelect = document.getElementById('category-select');
            categorySelect.innerHTML = ''; // Очищаем список категорий


            data.forEach(category => {
                const option = document.createElement('option');
                option.value = category.id;
                option.textContent = category.name;
                categorySelect.appendChild(option);
            });

            // const subcategorySelect = document.getElementById('subcategory-select');
            // subcategorySelect.innerHTML = ''; // Очищаем список подкатегорий
            // const defaultSubOption = document.createElement('option');
            // defaultSubOption.value = '';
            // defaultSubOption.textContent = 'Subcategory';
            // subcategorySelect.appendChild(defaultSubOption);
            // $('#subcategory').val('');
        })
        .catch(error => {
            console.error('Ошибка загрузки категорий:', error);
            alert('Ошибка загрузки категорий. Попробуйте еще раз.');
        });
}

function loadSubcategories(categoryId) {
    // if (!categoryId) {
    //     const subcategorySelect = document.getElementById('subcategory-select');
    //     subcategorySelect.innerHTML = ''; // Очищаем подкатегории
    //     const defaultOption = document.createElement('option');
    //     defaultOption.value = '';
    //     defaultOption.textContent = 'Subcategory';
    //     subcategorySelect.appendChild(defaultOption);
    //     $('#subcategory').val('');
    //     return;
    // }

    const subcategorySelect = document.getElementById('subcategory-select')

    axios.get(`/transaction/get_subcategories/${categoryId}/`)
        .then(response => {
            const data = response.data;
            const subcategorySelect = document.getElementById('subcategory-select');
            // subcategorySelect.innerHTML = ''; // Очищаем подкатегории
            // const defaultOption = document.createElement('option');
            // defaultOption.value = '';
            // defaultOption.textContent = 'Subcategory';
            // subcategorySelect.appendChild(defaultOption);




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
