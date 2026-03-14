# DECISIONS.md

## Pydantic Field Types Choices

### Transaction Model
- `id: int` - Used as a unique identifier for each transaction. Integer is efficient and standard for IDs.
- `amount: float = Field(gt=0, le=1000000)` - Float for monetary values with decimal precision. `gt=0` ensures positive amounts, `le=1000000` prevents unreasonably large values.
- `description: str = Field(min_length=1, max_length=200)` - String for transaction description. `min_length=1` ensures it's not empty, `max_length=200` prevents overly long descriptions.
- `date: datetime` - Datetime object to store the transaction date and time accurately.
- `type: TransactionType` - Enum to restrict to "income" or "expense", preventing invalid types.
- `categories: List[Category] = Field(default_factory=list)` - List of Category objects for nested relationship, allowing transactions to be associated with multiple categories.
- `notes: Optional[str] = None` - Optional string for additional notes, with None as default.

### Category Model
- `id: int` - Unique identifier for categories.
- `name: str = Field(min_length=1, max_length=50)` - String for category name, constrained to prevent empty or excessively long names.

## Validation Rules Explanations

- `amount: gt=0` - Protects against negative or zero amounts, which don't make sense for transactions.
- `amount: le=1000000` - Prevents entry of unrealistically large amounts that could be errors.
- `description: min_length=1, max_length=200` - Ensures descriptions are provided and not too verbose.
- `name: min_length=1, max_length=50` - Keeps category names concise and non-empty.
- `Custom @model_validator` - Checks that expenses don't exceed 50000 (to flag large expenses) and that each transaction has at least one category.
- `Enum for type` - Restricts transaction type to valid options, preventing typos or invalid entries.
- `Optional notes with default None` - Allows flexibility for additional info without requiring it.

## Async Endpoint Usage

The `GET /transactions/` endpoint uses `await asyncio.sleep(1)` to simulate a database query delay, demonstrating meaningful async behavior in a real-world scenario where fetching data might take time. This ensures the endpoint is non-blocking and can handle concurrent requests efficiently.