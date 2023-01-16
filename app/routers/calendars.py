from fastapi import APIRouter
from pydantic import BaseModel
import asyncio
import httpx

router = APIRouter()

GOOGLE_CALENDARS_URL = "https://www.googleapis.com/calendar/v3/users/me/calendarList"
GOOGLE_EVENTS_URL = ""


class CalendarDescription(BaseModel):
    id: str
    name: str


@router.get("/calendars/",
            tags=["calendars"],
            response_model=list[CalendarDescription],
            name="Get all calendar descriptions",
            description="Get metadata of all calendars"
            )
async def get_all_calendar_descriptions():
    return [CalendarDescription(id="15", name="xxx")]


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
