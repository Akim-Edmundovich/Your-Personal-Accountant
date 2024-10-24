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

// ------------------- Local Storage -------------------


// ------------------- Данные по умолчанию -------------------

const userSelectedType = document.getElementById('user-transaction-type')
const userSelectedCategory = document.getElementById('user-transaction-category')
const userSelectedSubcategory = document.getElementById('user-transaction-subcategory')
const userSelectedAmount = document.getElementById('user-transaction-amount')
const userSelectedQuantity = document.getElementById("user-transaction-quantity")
const userSelectedQuantityType = document.getElementById("user-transaction-quantity-type")
const userSelectedDescription = document.getElementById('user-transaction-description')
const userSelectedDate = document.getElementById('user-transaction-created_at')


// ------------------- Действия -------------------

console.log('Value ' + userSelectedQuantityType.value)
console.log('Value ' + userSelectedQuantity.value)


function loadQuantityType() {
    const quantityField = document.querySelector('input[name="quantity"]')
    const quantityTypeField = document.querySelector('select[name="quantity_type"]')

    console.log(quantityTypeField.value + ' type')

    if (!quantityField.value || quantityTypeField.value === 0) {
        quantityTypeField.disabled = true
        quantityTypeField.value = ''
    } else {
        quantityTypeField.value = userSelectedQuantityType.value
    }
    // Добавляем слушатель изменений для поля количества
    quantityField.addEventListener('input', function () {
        quantityTypeField.disabled = !quantityField.value;
    })
}

loadQuantityType()

document.querySelectorAll('#transaction-btn')
    .forEach(button => {
        button.addEventListener('click', function () {
            loadCategories(button.name)
        })
    })

document.getElementById('category-select').onchange = function (event) {
    const selectedValue = event.target.value
    loadSubcategories(selectedValue)
}


const expenseBtn = document.querySelector('button[name="expense"]')
const incomeBtn = document.querySelector('button[name="income"]')


if (userSelectedType.value === 'expense') {
    expenseBtn.classList.add('expense-btn')
    incomeBtn.classList.remove('income-btn')
} else {
    incomeBtn.classList.add('income-btn')
    expenseBtn.classList.remove('expense-btn')
}


const alertField = document.getElementById('alert-field')


document.querySelectorAll('.transaction-btn').forEach(button => {
    button.addEventListener('click', function () {
        const type = this.getAttribute('name');
        document.getElementById('user-transaction-type').value = type;
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

loadCategories(userSelectedType.value)

// ------------------- Загрузка данных -------------------

function loadCategories(type) {
    axios.get(`/transaction/get_categories/${type}`)
        .then(function (response) {
            const data = response.data
            const categorySelect = document.getElementById('category-select')
            categorySelect.innerHTML = ''

            for (const category of data) {
                let option = newElement('option', '')
                option.value = category.id
                option.textContent = category.name

                if (category.name === userSelectedCategory.value) {
                    option.setAttribute('selected', 'selected')
                }
                categorySelect.appendChild(option)
            }

            const selectedCategoryId = categorySelect.value
            loadSubcategories(selectedCategoryId)
        })
}


function loadSubcategories(category) {
    if (!category) {
        const subcategorySelect = document.getElementById('subcategory-select')
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
            const subcategorySelect = document.getElementById('subcategory-select')
            subcategorySelect.innerHTML = ''
            const defaultOption = newElement('option', '')
            defaultOption.value = ''
            subcategorySelect.appendChild(defaultOption)

            for (const subcategory of data) {
                let option = newElement('option', '')
                option.value = subcategory.id
                option.textContent = subcategory.name

                if (subcategory.name === userSelectedSubcategory.value) {
                    option.setAttribute('selected', 'selected')
                }
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

    const quantity = document.querySelector('input[name="quantity"]')

    if (!quantity.value || quantity.value === 0) {
        quantity.value = 0
    }

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