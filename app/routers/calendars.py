from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class CalendarDescription(BaseModel):
    id: str
    name: str


@router.get("/calendars/",
            tags=["calendars"],
            response_model=list[CalendarDescription])
async def get_all_calendar_descriptions():
    return []
