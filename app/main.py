from fastapi import FastAPI
from app.core.db import Base, engine
from app.api import teams  # импорт роутов

app = FastAPI()

# Создание таблиц (если ещё не созданы)
Base.metadata.create_all(bind=engine)

# Подключение роутов
app.include_router(teams.router, prefix="/teams")


from fastapi.staticfiles import StaticFiles

app.mount("/webapp", StaticFiles(directory="frontend", html=True), name="webapp")
