# Password Manager
## Установка
Для установки данного проекта достаточно клонировать его из данного репозитория. Это можно сделать командой:
```bash
git clone https://github.com/dobrodelete/password
```

После клонирования репозитория переходим в папку с проектом:
```bash
cd password
```

Создаём виртуальное окружение (Bash, PowerShell, CMD):
```bash
python3 -m venv venv # if python^3.11 calling by `python3` command else use `python`
```

После чего активируем виртуальное окружение:
Bash:
```bash
source venv/bin/activate
```
PowerShell:
```powershell
.\venv\Scripts\activate.ps1
```
CMD:
```cmd
.\venv\Scripts\activate
```

После активации виртуального окружения, надо импортировать нужные модули из requirements.txt (Bash, PowerShell, CMD):
```bash
pip install -r requirements.txt
```

После установки потребуется создание базы данных. Для этого используется Flask-Migrate:
```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

## Запуск приложения
Приложение запускается следующей командой (Bash, PowerShell, CMD):
```bash
python3 main.py # if python^3.11 calling by `python3` command else use `python`
```

По умолчанию программа запускается на 5000 порту и ссылка на сайт выглядит так: http://127.0.0.1:5000

## Запуск тестов
Для проведения тестов достаточно в корневой папке запустить команду (Bash, PowerShell, CMD):
```bash
pytest
```

## Authors
Проект создан dobrodelete для итоговой аттестации курса "Этичный хакинг на Python: надень «белую шляпу»"
Данный проект доступен всем и можете делать с ним что хотите