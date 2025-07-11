from typing import TypeVar, Generic, Optional
import strawberry

T = TypeVar("T")

@strawberry.type
class Response(Generic[T]):
    status: str 
    message: str
    data: Optional[T] = None
