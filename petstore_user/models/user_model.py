from pydantic import BaseModel, StrictStr, Field, ConfigDict
from typing import Optional


class UserModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: Optional[int] = None
    username: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(None, alias='firstName')
    last_name: Optional[StrictStr] = Field(None, alias='lastName')
    email: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    user_status: Optional[int] = Field(None, alias='userStatus', description='User Status')
