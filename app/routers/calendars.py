import http
import requests
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from pydantic import BaseModel
import logging
router = APIRouter()

GOOGLE_CALENDARS_URL = "https://www.googleapis.com/calendar/v3/users/me/calendarList"
GOOGLE_EVENTS_URL = ""


class CalendarDescription(BaseModel):
    id: str
    name: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def build_header_with_bearer_token(access_token: str = Depends(oauth2_scheme)) -> dict:
    return {"Authorization": f"Bearer {access_token}"}


@router.get("/calendars/",
            tags=["calendars"],
            response_model=list[CalendarDescription],
            name="Get all calendar descriptions",
            description="Get metadata of all calendars"
            )
async def get_all_calendar_descriptions(access_token: str = Depends(oauth2_scheme)):
    headers = build_header_with_bearer_token(access_token)
    response = requests.get(GOOGLE_CALENDARS_URL, headers=headers)
    if response.status_code == http.HTTPStatus.OK:
        events = response.json()["items"]
        descriptions: list[CalendarDescription] = list(map(lambda event: CalendarDescription(id=event['id'], name=event['summary']), events))
        logging.info(f"Successfully fetched {len(descriptions)} calendar descriptions")
        return descriptions
    else:
        logging.error(f"Error while fetching calendars: {response.status_code}: {response.reason}")
        return []


class EventDescription(BaseModel):
    id: str
    name: str
    duration_minutes: int


@router.get("/calendars/{calendar_id}/events/",
            tags=["calendars"],
            response_model=list[EventDescription],
            name="Get all events of calendar",
            description="Get metadata of all events from calendar by id of this calendar"
            )
async def get_all_calendar_descriptions(calendar_id: int):
    return []
