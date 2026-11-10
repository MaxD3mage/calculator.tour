# ТурМир — онлайн-калькулятор стоимости тура

Учебный проект на Python и Django: пользователь выбирает направление, город вылета, даты, состав группы и услуги, после чего получает прозрачную предварительную стоимость тура.

## Быстрый запуск

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Откройте http://127.0.0.1:8000/.

## Тесты

```bash
python manage.py test
```

## Docker

```bash
docker compose up --build
```

Основные каталоги:

- `pricing.py` — правила расчёта;
- `calculator/` — Django-форма и обработчик;
- `templates/` и `static/` — интерфейс;
- `Dockerfile` и `docker-compose.yml` — контейнеризация;
- `.github/workflows/ci.yml` — автоматические проверки GitHub Actions.
