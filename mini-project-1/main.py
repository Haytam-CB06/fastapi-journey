from fastapi import FastAPI, HTTPException
from models import Transaction, Category, TransactionType
from typing import List
import asyncio

app = FastAPI(title="Budget Tracker API")

transactions: List[Transaction] = []
categories: List[Category] = []

# Transactions endpoints
@app.get("/transactions/", response_model=List[Transaction])
async def get_transactions():
    return transactions

@app.get("/transactions/{transaction_id}", response_model=Transaction)
async def get_transaction(transaction_id: int):
    for t in transactions:
        if t.id == transaction_id:
            return t
    raise HTTPException(status_code=404, detail="Transaction not found")

@app.post("/transactions/", response_model=Transaction)
async def create_transaction(transaction: Transaction):
    # Check if id already exists
    if any(t.id == transaction.id for t in transactions):
        raise HTTPException(status_code=400, detail="Transaction ID already exists")
    transactions.append(transaction)
    return transaction

@app.put("/transactions/{transaction_id}", response_model=Transaction)
async def update_transaction(transaction_id: int, transaction: Transaction):
    for i, t in enumerate(transactions):
        if t.id == transaction_id:
            transactions[i] = transaction
            return transaction
    raise HTTPException(status_code=404, detail="Transaction not found")

@app.delete("/transactions/{transaction_id}")
async def delete_transaction(transaction_id: int):
    for i, t in enumerate(transactions):
        if t.id == transaction_id:
            del transactions[i]
            return {"message": "Transaction deleted"}
    raise HTTPException(status_code=404, detail="Transaction not found")

# Categories endpoints
@app.get("/categories/", response_model=List[Category])
async def get_categories():
    return categories

@app.get("/categories/{category_id}", response_model=Category)
async def get_category(category_id: int):
    for c in categories:
        if c.id == category_id:
            return c
    raise HTTPException(status_code=404, detail="Category not found")

@app.post("/categories/", response_model=Category)
async def create_category(category: Category):
    if any(c.id == category.id for c in categories):
        raise HTTPException(status_code=400, detail="Category ID already exists")
    categories.append(category)
    return category

@app.put("/categories/{category_id}", response_model=Category)
async def update_category(category_id: int, category: Category):
    for i, c in enumerate(categories):
        if c.id == category_id:
            categories[i] = category
            return category
    raise HTTPException(status_code=404, detail="Category not found")

@app.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    for i, c in enumerate(categories):
        if c.id == category_id:
            del categories[i]
            return {"message": "Category deleted"}
    raise HTTPException(status_code=404, detail="Category not found")