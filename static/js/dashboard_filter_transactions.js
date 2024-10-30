document.addEventListener('DOMContentLoaded', function () {
    const expenseBtn = document.getElementById('expense-transactions-btn')
    const incomeBtn = document.getElementById('income-transactions-btn')
    const transactionsList = document.getElementById('transactions-list')
    const dateRangeInput = document.getElementById('date-range');

    const buttons = {
        day: document.getElementById('filter-day'),
        week: document.getElementById('filter-week'),
        month: document.getElementById('filter-month'),
        year: document.getElementById('filter-year'),
        period: document.getElementById('date-range')
    };

    expenseBtn.style.backgroundColor = 'red'
    incomeBtn.style.backgroundColor = 'black'

    buttons.period.addEventListener('click', () => {
        dateRangeInput.style.display = 'inline';
    });

    window.onload = function () {
        expenseBtn.click()
    }


    function changeClass(activeBtn) {

        activeBtn.classList.remove('black-btn')

        for (const btn in buttons) {
            if (buttons.hasOwnProperty(btn) && buttons[btn] !== activeBtn) {

                    buttons[btn].classList.add('black-btn');

            }
        }
    }


    expenseBtn.addEventListener('click', function () {
        loadExpensesDefault('day_expense')

        changeClass(buttons.day)

        expenseBtn.style.backgroundColor = 'red'
        incomeBtn.style.backgroundColor = 'black'

        buttons.day.addEventListener('click', function () {
            changeClass(buttons.day)
            loadExpenses('day_expense')
        });
        buttons.week.addEventListener('click', function () {
            changeClass(buttons.week)
            loadExpenses('week_expense')
        });
        buttons.month.addEventListener('click', function () {
            changeClass(buttons.month)
            loadExpenses('month_expense')
        });
        buttons.year.addEventListener('click', function () {
            changeClass(buttons.year)
            loadExpenses('year_expense')
        });

        buttons.period.addEventListener('click', () => {
            changeClass(buttons.period)
            const dateRange = dateRangeInput.value;
            if (dateRange) {
                loadExpenses('period_expense', dateRange);
            }
        });
    })

    incomeBtn.addEventListener('click', function () {
        loadIncomes('day_income')

        expenseBtn.style.backgroundColor = 'black'
        incomeBtn.style.backgroundColor = 'green'

        buttons.day.addEventListener('click', function () {
            changeClass(buttons.day)
            loadIncomes('day_income')
        });
        buttons.week.addEventListener('click', function () {
            changeClass(buttons.week)
            loadIncomes('week_income')
        });
        buttons.month.addEventListener('click', function () {
            changeClass(buttons.month)
            loadIncomes('month_income')
        });
        buttons.year.addEventListener('click', function () {
            changeClass(buttons.year)
            loadIncomes('year_income')
        });

        buttons.period.addEventListener('click', () => {
            changeClass(buttons.period)
            const startDate = dateRangeInput.value;
            if (startDate) {
                loadIncomes('period_income', startDate);
            }
        });
    })


    function loadExpensesDefault() {
        axios.get(`expenses-filter-transactions/day_expense/`)
            .then(response => {
                transactionsList.innerHTML = response.data.html
            })
            .catch(error => console.error('Ошибка:', error));
    }

    // {# EXPENSES #}
    $(function () {
        const dateRangePicker = $('input[name="daterange"]');

        dateRangePicker.daterangepicker({
            opens: 'left',
            maxDate: today,
        }, function (start, end) {
            // Вызываем функцию с выбранным диапазоном дат
            loadExpenses('period_expense', start.format('YYYY-MM-DD'), end.format('YYYY-MM-DD'));
        });
    });

    function loadExpenses(filterType, startDate = null, endDate = null) {
        const params = startDate && endDate ? {
            date_range: `${startDate},${endDate}`
        } : {};

        axios.get(`expenses-filter-transactions/${filterType}/`, {params})
            .then(response => {
                transactionsList.innerHTML = response.data.html;
            })
            .catch(error => console.error('Ошибка:', error));
    }

    // {# INCOMES #}

    $(function () {
        const dateRangePicker = $('input[name="daterange"]');

        dateRangePicker.daterangepicker({
            "showDropdowns": true,
            opens: 'left',
            maxDate: today
        }, function (start, end) {
            // Вызываем функцию с выбранным диапазоном дат
            loadIncomes('period_income', start.format('YYYY-MM-DD'), end.format('YYYY-MM-DD'));
        });
    });

    function loadIncomes(filterType, startDate = null, endDate = null) {
        const params = startDate && endDate ? {
            date_range: `${startDate},${endDate}`
        } : {};

        axios.get(`incomes-filter-transactions/${filterType}/`, {params})
            .then(response => {
                transactionsList.innerHTML = response.data.html;
            })
            .catch(error => console.error('Ошибка:', error));
    }


    // Установка даты и ограничений по дате
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;
    dateRangeInput.max = formattedDate;
})