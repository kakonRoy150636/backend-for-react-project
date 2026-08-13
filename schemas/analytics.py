from pydantic import BaseModel
from typing import Optional

class TrackEvent(BaseModel):
    event_type: str
    template_id: Optional[int] = None