document.getElementById('add-subcategory-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Останавливаем стандартную отправку формы

    const subcategoryName = document.getElementById('subcategory-name').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = event.target.getAttribute('data-url');  // Получаем URL из атрибута формы

    // Отправляем данные через Axios
    axios.post(url, {
    subcategory_name: subcategoryName
}, {
    headers: {
        'X-CSRFToken': csrfToken
    }
})
.then(function (response) {
    const newSubcategory = response.data;  // Убедитесь, что это объект с id и name
    const subcategoryList = document.getElementById('subcategory-list');
    const newLi = document.createElement('li');
    newLi.id = `subcategory-${newSubcategory.id}`;
    newLi.innerHTML = `
        <form class="subcategory-edit-form" data-subcategory-id="${newSubcategory.id}">
            <input type="text" name="name" value="${newSubcategory.name}">  // Используйте newSubcategory.name
            <button type="submit" class="submit">Save</button>
        </form>
        <button class="delete-button" data-subcategory-id="${newSubcategory.id}">Delete</button>
    `;
    subcategoryList.appendChild(newLi);

    // Очищаем поле ввода
    document.getElementById('subcategory-name').value = '';
})

document.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-button')) {
            const subcategoryId = event.target.getAttribute('data-subcategory-id');
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            // Подтверждение удаления
            if (!confirm('Are you sure you want to delete this subcategory?')) {
                return;
            }

            axios.delete(`/settings/subcategory/${subcategoryId}/delete/`, {
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(function(response) {
                // Удаляем подкатегорию из списка
                document.getElementById(`subcategory-${subcategoryId}`).remove();
            })
            .catch(function(error) {
                console.error('Error:', error);
            });
        }
    });}