from pydantic import BaseModel, Field, model_validator
from typing import List, Optional
from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

class Category(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=50)

class Transaction(BaseModel):
    id: int
    amount: float = Field(gt=0, le=1000000)  
    description: str = Field(min_length=1, max_length=200)  
    date: datetime
    type: TransactionType  
    categories: List[Category] = Field(default_factory=list)  
    notes: Optional[str] = None  

    @model_validator(mode='after')
    def validate_transaction(self):
        if self.type == TransactionType.EXPENSE and self.amount > 50000:
            raise ValueError("Expense amount cannot exceed 50000")
        if not self.categories:
            raise ValueError("Transaction must have at least one category")
        return self