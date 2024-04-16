from .model import BaseModel
from typing import Optional, TypeVar

T = TypeVar('T')

class GenericStateErrorStatus(BaseModel):
    state: Optional[T]
    class Config:
        use_enum_values: bool
