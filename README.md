# Костяк проекта на FastAPI + SQLModel ORM + Alembic

## Как запускать:
0) Установить пакеты из reqs.txt
1) Поднять Postgres
2) Применить миграции с помощью `alembic upgrade head`
3) Запустить с проект командой `uvicorn main:app --reload`

## Какое API?
Идем на `localhost:8000/docs`, там поднят автоматом сваггер. Можно хоть там поиграться
