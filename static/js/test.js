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


document.querySelectorAll('#transaction-btn')
    .forEach(button => {
        button.addEventListener('click', function () {
            loadCategories(button.name)
        })
    })


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

            // loadSubcategories(data.name)
        })
}

function loadSubcategories(category) {
    axios.get(`transaction/get_subcategories/${category}`)
        .then(function (response) {
            const data = response.data
            const subcategorySelect = document.getElementById('subcategories')
            subcategorySelect.innerHTML = ''

            for (const subcategory of data) {
                let option = newElement('option', '')
                option.value = subcategory.id
                option.textContent = subcategory.name
                subcategorySelect.appendChild(option)

                const subDiv = newElement('div', '')
                subDiv.innerText = subcategory.name
                document.body.appendChild(subDiv)
            }

        })
}

