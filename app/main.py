from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers import calendars

import logging


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8010"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(calendars.router)

# Create a logger object
logging.basicConfig(filename='execution_log.log', encoding='utf-8', format='%(levelname)s %(asctime)s %(message)s', datefmt='%Y.%m.%d %H:%M:%S', level=logging.DEBUG)