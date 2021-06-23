from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


# Admin service event payloads
class UserRegistered(BaseModel):
    userid: UUID


class UserPasswordUpdated(BaseModel):
    userid: UUID
    date: datetime


"""
class UserRegistered(BaseModel):
    userid: UUID
    title: str
    description: str
    creation_date: Optional[date]
    rating: Optional[float]
    type: str
    length_minutes: Optional[int]
    created: datetime
    modified: datetime
    actors: List[Dict[str, str]]
    directors: List[Dict[str, str]]
    writers: List[Dict[str, str]]
    genres: List[Dict[str, str]]

"""