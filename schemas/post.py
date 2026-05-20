from pydantic import BaseModel
from datetime import datetime, UTC


class PostRequest(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
    published: bool = False
