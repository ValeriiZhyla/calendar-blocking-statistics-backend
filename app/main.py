from fastapi import FastAPI
from .routers import calendars

app = FastAPI()
app.include_router(calendars.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
