from pydantic import BaseModel, Field
from typing import Literal, Annotated, Optional
from datetime import datetime


class Transaction(BaseModel):
    """Domain model for the transaction data"""

    title: str = Field(min_length=5, max_length=70)
    description: str = Field(max_length=255)
    date: datetime
    tags: Optional[list[str]]
    amount: Annotated[float, Field(gt=0)]
    type_transaction: Literal["income", "expense"]

    @property
    def year(self) -> int:
        """Extract year component"""
        return self.date.year

    @property
    def month(self) -> int:
        """Extract month component"""
        return self.date.month

    @property
    def day(self) -> int:
        """Extract day component"""
        return self.date.day

    @property
    def year_month_key(self) -> str:
        """Generate a sortable year-month key for grouping."""
        return self.date.strftime("%Y-%m")
