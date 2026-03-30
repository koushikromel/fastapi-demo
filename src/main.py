from fastapi import FastAPI
from datetime import datetime, timezone, timedelta

app = FastAPI()


@app.get("/")
async def hello():
    ist_now = datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=5, minutes=30)))
    formatted_time = ist_now.strftime("%Y-%m-%d %I:%M %p")
    return f"Hello world {formatted_time}"


@app.get("/{name}")
async def greet(name: str):
    return f"Hello {name}"
