from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ValidationError, validator

from base.models.store import Store

class Request(BaseModel):
    """ Pydantic model to validate the HTTP request send to POST /store"""

    name: str
    delay: Optional[int] = 15
    working_since: Optional[datetime] = None
    employees: List[str] = []

    @validator('name')
    def name_must_be_unique(cls, v):
        # Sometimes a robust validation logic will require us to
        # read from DB !!!
        if Store.scan(Store.name == v):
            raise ValidationError("store name already in use")
        return v
