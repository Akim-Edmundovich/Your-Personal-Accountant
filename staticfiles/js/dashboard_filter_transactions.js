document.addEventListener('DOMContentLoaded', function () {
    const expenseBtn = document.getElementById('expense-transactions-btn')
    const incomeBtn = document.getElementById('income-transactions-btn')
    const transactionsList = document.getElementById('transactions-list')
    const expenseDateRangeInput = document.querySelector('input[name="expenseDaterange"]');
    const incomeDateRangeInput = document.querySelector('input[name="incomeDaterange"]');

    const expenseFilterButtons = {
        day: document.getElementById('expense-filter-day'),
        week: document.getElementById('expense-filter-week'),
        month: document.getElementById('expense-filter-month'),
        year: document.getElementById('expense-filter-year'),
        period: document.getElementById('expense-date-range')
    };

    const incomeFilterButtons = {
        day: document.getElementById('income-filter-day'),
        week: document.getElementById('income-filter-week'),
        month: document.getElementById('income-filter-month'),
        year: document.getElementById('income-filter-year'),
        period: document.getElementById('income-date-range')
    };


    expenseBtn.style.backgroundColor = 'red'
    incomeBtn.style.backgroundColor = 'black'

    expenseFilterButtons.period.addEventListener('click', () => {
        expenseDateRangeInput.style.display = 'inline';
    });

    incomeFilterButtons.period.addEventListener('click', () => {
        incomeDateRangeInput.style.display = 'inline';
    });

    window.onload = function () {
        expenseBtn.click()
    }


    function changeClassExpenseFilter(activeBtn) {
        activeBtn.classList.remove('black-btn')
        for (const btn in expenseFilterButtons) {
            if (expenseFilterButtons.hasOwnProperty(btn) && expenseFilterButtons[btn] !== activeBtn) {

                expenseFilterButtons[btn].classList.add('black-btn');
            }
        }
    }

    function changeClassIncomeFilter(activeBtn) {
        activeBtn.classList.remove('black-btn')
        for (const btn in incomeFilterButtons) {
            if (incomeFilterButtons.hasOwnProperty(btn) && incomeFilterButtons[btn] !== activeBtn) {

                incomeFilterButtons[btn].classList.add('black-btn');
            }
        }
    }


    const expenseBntContainer = document.getElementById('expense-filter-btns')
    const incomeBntContainer = document.getElementById('income-filter-btns')

    expenseBtn.addEventListener('click', function () {
        loadExpensesDefault('day_expense')

        expenseBntContainer.style.display = ''
        incomeBntContainer.style.display = 'none'

        changeClassExpenseFilter(expenseFilterButtons.day)

        expenseBtn.style.backgroundColor = 'red'
        incomeBtn.style.backgroundColor = 'black'

        expenseFilterButtons.day.addEventListener('click', function () {
            changeClassExpenseFilter(expenseFilterButtons.day)
            loadExpenses('day_expense')
        });
        expenseFilterButtons.week.addEventListener('click', function () {
            changeClassExpenseFilter(expenseFilterButtons.week)
            loadExpenses('week_expense')
        });
        expenseFilterButtons.month.addEventListener('click', function () {
            changeClassExpenseFilter(expenseFilterButtons.month)
            loadExpenses('month_expense')
        });
        expenseFilterButtons.year.addEventListener('click', function () {
            changeClassExpenseFilter(expenseFilterButtons.year)
            loadExpenses('year_expense')
        });

        expenseFilterButtons.period.addEventListener('click', () => {
            changeClassExpenseFilter(expenseFilterButtons.period)
            const dateRange = expenseDateRangeInput.value;
            if (dateRange) {
                loadExpenses('period_expense', dateRange);
            }
        });
    })

    incomeBtn.addEventListener('click', function () {
        loadIncomes('day_income')

        incomeBntContainer.style.display = ''
        expenseBntContainer.style.display = 'none'

        expenseBtn.style.backgroundColor = 'black'
        incomeBtn.style.backgroundColor = 'green'

        changeClassIncomeFilter(incomeFilterButtons.day)

        incomeFilterButtons.day.addEventListener('click', function () {
            changeClassIncomeFilter(incomeFilterButtons.day)
            loadIncomes('day_income')
        });
        incomeFilterButtons.week.addEventListener('click', function () {
            changeClassIncomeFilter(incomeFilterButtons.week)
            loadIncomes('week_income')
        });
        incomeFilterButtons.month.addEventListener('click', function () {
            changeClassIncomeFilter(incomeFilterButtons.month)
            loadIncomes('month_income')
        });
        incomeFilterButtons.year.addEventListener('click', function () {
            changeClassIncomeFilter(incomeFilterButtons.year)
            loadIncomes('year_income')
        });

        incomeFilterButtons.period.addEventListener('click', () => {
            changeClassIncomeFilter(incomeFilterButtons.period)
            const startDate = incomeDateRangeInput.value;
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
        const dateRangePicker = $('input[name="expenseDaterange"]');

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
        const dateRangePicker = $('input[name="incomeDaterange"]');

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
    expenseDateRangeInput.max = formattedDate;
    incomeDateRangeInput.max = formattedDate;
})