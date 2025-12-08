from pydantic import BaseModel, Field
from typing import Literal, Annotated, Optional
from datetime import datetime


class Transaction(BaseModel):
    title: str = Field(min_length=5, max_length=70)
    description: str = Field(max_length=255)
    date: datetime
    tags: Optional[list[str]]
    amount: Annotated[float, Field(gt=0)]
    type_transaction: Literal["income", "expense"]
