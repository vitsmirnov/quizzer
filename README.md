# Quizzer

### Стек:
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.12.0](https://img.shields.io/badge/3.12.0-blue?style=flat-square&logo=3.12.0)
![Django](https://img.shields.io/badge/Django-171515?style=flat-square&logo=Django)![4.2.14](https://img.shields.io/badge/4.2.14-blue?style=flat-square&logo=4.2.14)
![SQLite](https://img.shields.io/badge/SQLite-171515?style=flat-square&logo=SQLite)![3.46.0](https://img.shields.io/badge/3.46.0-blue?style=flat-square&logo=3.46.0)
![Pytest](https://img.shields.io/badge/Pytest-171515?style=flat-square&logo=Pytest)

### Описание
**_Quizzer_** - сервис для прохождения увлекателных тестов/опросов, позволяющий проходить тесты, получать за это баллы, на которые можно покупать невероятные цвета для своей рамки, и многое другое (ничего).

### Запуск проекта (локально)
**В продакшене проект пока не тестировался*
**Команды проверялись на Windows (PowerShell 7.4.2), но большая часть должна работать и на Unix*

На машине должен быть установлен Python версии 3.12 или совместимый с ним. Скачать и установить можно отсода: https://www.python.org/downloads/. Проверить, установлен ли Python, можно командой `python --version`
```bash
python --version
Python 3.12.0
```

Чтобы клонировать репозиторий, должен быть установлен git, но это не обязательно, исходный код можно скачать с GitHub архивом (кнопка для скачивания находится в верхнем правом углу страницы репозитория: <>Code -> Download ZIP). Скачать и установить git можно отсюда: https://git-scm.com/downloads. Проверить, установлен ли git, можно командой `git version`:
```bash
git version
git version 2.43.0.windows.1
```

В командной строке переходим в каталог (команда `cd`), где будет хранится проект, клонируем репозиторий и переходим в него:
```bash
cd <ИМЯ КАТАЛОГА>
git clone https://github.com/vitsmirnov/quizzer
cd quizzer
```
**Создать каталог можно командой* `mkdir <ИМЯ КАТАЛОГА>`

Создаём и активируем виртуальное окружение командой `python -m venv <ИМЯ КАТАЛОГА>` (имя каталога, где будет располагаться окружение, в данном случае .venv):
```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
```
**Если виртуальное окружение успешно установлено и активировано, в командной строке должна появится соответствующая надпись* **(.venv)** *(справедливо для PowerShell)*
**Деактивировать виртуальное окружение можно командой* `deactivate`
**Если команда python не работает, можно попробовать команду* `python3`

Обновляем pip до последней версии:
```bash
python -m pip install --upgrade pip
```

Устанавливаем зависимости (виртуальное окружение должно быть активировано):
```bash
python -m pip install -r requirements.txt
```

На момент написания проект зависит только от Django (помимо Python), а зависимости, необходимые для работы Django, он установит самостоятельно. Поэтому в requirements.txt содержит только Django, но после установки должны появится следующие приложения, что можно проверить командой `pip list`
```bash
pip list
asgiref  3.8.1
Django   4.2.14
pip      24.1.2
sqlparse 0.5.1
tzdata   2024.1
```
**Если команда* `pip list` *не работает, можно попробовать команду* `python -m pip list`

Вместе с проектом в репозитории уже находится тестовая база данных SQLite (файл с именем db.sqlite3), к ней применены миграции и в ней находятся тестовые данные. Подробнее о ней далее.
Если вам не нужна база данных, то нужно удалить или переместить файл db.sqlite3, после чего нужно создать и применить миграции, а затем создать суперюзера для входа в портал администрации Django для редактирования базы данных.
Создать миграции можно командой `python manage.py makemigrations`, а применить миграции командой `python manage.py migrate`:
```bash
python manage.py makemigrations
...
python manage.py migrate
...
```
**Для того, чтобы эти инструкции работали, нужно находиться в каталоге репозитория, где расположен файл manage.py. Это файл, который Django создаёт автоматически при создании проекта, что упрощает разработку. Подробнее узнать можно здесь:* https://docs.djangoproject.com/en/4.2/ref/django-admin/.

Создать суперюзера можно командой `python manage.py createsuperuser`, где необходимо будет ввести имя, пароль и адрес почты.
```bash
python manage.py createsuperuser
...
```

После того, как суперюзер создан, можно запустить локальный сервер командой `python manage.py runserver`:
```bash
python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 1, 2000 - 23:59:59
Django version 4.2.14, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
**Остановить работу локального сервера можно сочетанием клавишь Ctrl+C (для Windows)*

После успешного запуска сервера можно перейти в браузере по адресу http://127.0.0.1:8000/admin, авторизоваться под созданным именем и паролем, где можно будет редактировать базу данных.

По адресу http://127.0.0.1:8000/ будет доступно само приложение Quizzer.

Чтобы войти в ту..

Чтобы упростить процесс запуска приложения, в корневом каталоге репозитория находятся скрипты для PowerShell (*.ps1), которые содержат в себе все перечисленные выше команды:
`start.ps1`
`cloneandstart.ps1`
**Скрипты написаны для Windows, но, возможно, будут работать и в Unix.*

Эти скрипты не включают в себя команды создания и применения миграций, и создания суперюзера для новой базы данных. Для этого нужно применить команды, описанные выше. Также нужно самостоятельно установить Python и git (см. выше). Если команды не работают, можно попробовать заменить в скриптах команду `python` на `python3`.
Если вы уже клонировали репозиторий с GitHub, то просто запустите скрипт *start.ps1*. Или скачайте/скопируйте скрипт cloneandstart.ps1 в каталог, где будет располагаться проект и запустите его.

Приятного использования!

*Виталий Смирнов, 2024*
*https://github.com/vitsmirnov*
*mrmaybelately@gmail.com*