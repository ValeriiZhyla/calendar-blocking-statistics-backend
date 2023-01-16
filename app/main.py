from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers import calendars

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



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

SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
