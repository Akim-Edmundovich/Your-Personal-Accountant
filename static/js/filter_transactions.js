document.addEventListener('DOMContentLoaded', function () {
    const buttons = {
        day: document.getElementById('filter-day'),
        week: document.getElementById('filter-week'),
        month: document.getElementById('filter-month'),
        year: document.getElementById('filter-year'),
        period: document.getElementById('filter-period')
    };
    const startDateInput = document.getElementById('start-date');
    const endDateInput = document.getElementById('end-date');

    buttons.period.addEventListener('click', () => {
        startDateInput.style.display = 'inline';
        endDateInput.style.display = 'inline';
    });

    function filterTransactions(filterType, startDate = null, endDate = null) {
        const params = startDate && endDate ? { start_date: startDate, end_date: endDate } : {};
        axios.get(`filter-transactions/${filterType}/`, { params })
            .then(response => {
                document.getElementById('transactions-list').innerHTML = response.data.html;
                console.log(response.data.html)
            })
            .catch(error => console.error('Ошибка:', error));
    }

    buttons.day.addEventListener('click', () => filterTransactions('day'));
    buttons.week.addEventListener('click', () => filterTransactions('week'));
    buttons.month.addEventListener('click', () => filterTransactions('month'));
    buttons.year.addEventListener('click', () => filterTransactions('year'));

    buttons.period.addEventListener('click', () => {
        const startDate = startDateInput.value;
        const endDate = endDateInput.value;
        if (startDate && endDate) {
            filterTransactions('period', startDate, endDate);
        }
    });
});
