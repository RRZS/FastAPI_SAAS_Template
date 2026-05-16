# python imports
from datetime import datetime
from enum import Enum
from typing import List, Optional

# 3rd party imports
from pydantic import EmailStr

# application imports
from src.app.utils.schemas_utils import AbstractModel, ResponseModel


# Lead lifecycle status
class LeadStatus(Enum):
    new = "new"
    contacted = "contacted"
    won = "won"
    lost = "lost"


# Public lead capture DTO (submitted by a website form, no auth)
class LeadCapture(AbstractModel):
    name: str
    email: Optional[EmailStr]
    phone: Optional[str]
    message: Optional[str]
    source: Optional[str]


# Lead status / detail update DTO
class LeadUpdate(AbstractModel):
    name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    message: Optional[str]
    status: Optional[LeadStatus]


# Lead response DTO
class LeadResponse(AbstractModel):
    id: int
    org_id: int
    name: str
    email: Optional[str]
    phone: Optional[str]
    message: Optional[str]
    source: str
    status: str
    contacted_at: Optional[datetime]
    date_created: Optional[datetime]


# Single lead response DTO
class MessageLeadResp(ResponseModel):
    data: LeadResponse


# List of leads response DTO
class MessageListLeadResp(ResponseModel):
    data: List[LeadResponse]
