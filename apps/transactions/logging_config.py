import logging
import re
import textwrap


class SQLFormatter(logging.Handler):
    def emit(self, record):
        # Форматирование сообщения
        message = self.format(record)

        # Регулярное выражение для поиска SQL-запросов
        sql_pattern = re.compile(
            r'(\(\d+\.\d+\))\s*(SELECT|INSERT|UPDATE|DELETE|WITH|FROM)\s*(.*?);',
            re.DOTALL
        )
        formatted_message = sql_pattern.sub(self.format_sql, message)

        # Выводим отформатированное сообщение
        print(formatted_message)  # Используем print для вывода в консоль

    def format_sql(self, match):
        # Форматирование SQL-запроса для лучшей читаемости
        query = match.group(0)
        formatted_query = textwrap.indent(query, '    ')  # Добавляем отступ
        return formatted_query