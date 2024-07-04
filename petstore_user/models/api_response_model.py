from pydantic import BaseModel, StrictStr, ConfigDict
from typing import Optional


class ApiResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: Optional[int] = None
    type: Optional[StrictStr]
    message: Optional[StrictStr]
