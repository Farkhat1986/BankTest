Установка и запуск проекта

Склонировать репозиторий
git clone https://github.com/Farkhat1986/BankTest

Перейти в директорию проекта

Создать вируальное окружение
python -m venv venv

Активировать окружение
venv\Scripts\activate

Установка зависимостей
pip install -r requirements.txt

Запуск тестов
pytest --alluredir=allure-results

Запуск отчета allure по тестам
allure serve allure-results
