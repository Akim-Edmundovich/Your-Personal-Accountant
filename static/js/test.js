// Принимает тег, который нужно создать.
// param - объект, который будем передавать
function newElement(tag, param) {
    // Создание элемента с переданным тегом
    const el = document.createElement(tag)

    // Object.entries - словарь.
    for (const [key, value] of Object.entries(param)) {
        // Если передан список классов
        if (key === 'classList') {
            for (const newClass of value) {
                // Добавление элементу класса
                el.classList.add(newClass)
            }
        }
    }
    return el
}


// ------------------- Данные по умолчанию -------------------


const userSelectedType = document.getElementById('user-transaction-type')
const userSelectedCategory = ' '


// ------------------- Действия -------------------

document.querySelectorAll('#transaction-btn')
    .forEach(button => {
        button.addEventListener('click', function () {
            loadCategories(button.name)
        })
    })

document.getElementById('categories').onchange = function (event) {
    const selectedValue = event.target.value
    loadSubcategories(selectedValue)

}


// ------------------- Загрузка данных -------------------

function loadCategories(type) {
    axios.get(`/transaction/get_categories/${type}`)
        .then(function (response) {
            const data = response.data
            const categorySelect = document.getElementById('categories')
            categorySelect.innerHTML = ''

            for (const category of data) {
                let option = newElement('option', '')
                option.value = category.id
                option.textContent = category.name
                categorySelect.appendChild(option)
            }

            const selectedCategoryId = categorySelect.value
            loadSubcategories(selectedCategoryId)

        })
}


function loadSubcategories(category) {
    if (!category) {
        const subcategorySelect = document.getElementById('subcategory')
        subcategorySelect.innerHTML = ''
        const defaultOption = newElement('option', '')
        defaultOption.value = ''
        defaultOption.text = 'Subcategory'
        defaultOption.setAttribute('selected', 'Subcategory')
        subcategorySelect.appendChild(defaultOption)
    }

    axios.get(`http://127.0.0.1:8000/transaction/get_subcategories/${category}`)
        .then(function (response) {
            const data = response.data
            const subcategorySelect = document.getElementById('subcategories')
            subcategorySelect.innerHTML = ''
            const defaultOption = newElement('option', '')
            defaultOption.value = ''
            subcategorySelect.appendChild(defaultOption)

            for (const subcategory of data) {
                let option = newElement('option', '')
                option.value = subcategory.id
                option.textContent = subcategory.name
                subcategorySelect.appendChild(option)
            }
        })
}


// ------------------- Настройка select2 -------------------
$(document).ready(function () {
    $('.select2').select2({
        width: '100%',
        placeholder: 'Select',
        allowClear: true
    });
});


// ------------------- Date -------------------

// Установка даты и ограничений по дате
const today = new Date();
const year = today.getFullYear();
const month = String(today.getMonth() + 1).padStart(2, '0');
const day = String(today.getDate()).padStart(2, '0');
const formattedDate = `${year}-${month}-${day}`;
document.getElementById('created-at-input').max = formattedDate;


// ------------------- Обработка отправки формы -------------------
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