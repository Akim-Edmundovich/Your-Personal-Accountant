function enableEdit(index) {
    const form = document.getElementById(`subcategory-form-${index}`);
    const inputs = form.querySelectorAll('input, select, textarea');
    inputs.forEach(input => input.disabled = false); // Разблокировка полей

    const editButton = form.querySelector('button[type="button"]');
    const confirmButton = form.querySelector(`#confirm-btn-${index}`);
    editButton.style.display = 'none';  // Скрытие кнопки "Edit"
    confirmButton.style.display = 'inline';  // Отображение кнопки "Confirm"
}

function deleteSubcategory(subcategoryId, index) {
    const form = document.getElementById(`subcategory-form-${index}`);
    if (confirm("Are you sure you want to delete this subcategory?")) {
        fetch(`/settings/subcategory/delete/${subcategoryId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
            .then(response => {
                if (response.ok) {
                    form.remove();  // Удаление формы с HTML страницы
                } else {
                    alert("Error: Could not delete the subcategory.");
                }
            });
    }
}
