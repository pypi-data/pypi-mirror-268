from typing import Any, Dict, Optional

import pydantic
from pydantic import BaseModel
from typing_extensions import Self


class DagsterModel(BaseModel):
    """Standardizes on Pydantic settings that are stricter than the default.
    - Frozen, to avoid complexity caused by mutation.
    - extra=forbid, to avoid bugs caused by accidentally constructing with the wrong arguments.
    - arbitrary_types_allowed, to allow non-model class params to be validated with isinstance.
    """

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

    class Config:
        extra = "forbid"
        frozen = True
        arbitrary_types_allowed = True

    def model_copy(self, *, update: Optional[Dict[str, Any]] = None) -> Self:
        if pydantic.__version__ >= "2":
            return super().model_copy(update=update)  # type: ignore
        else:
            return super().copy(update=update)
