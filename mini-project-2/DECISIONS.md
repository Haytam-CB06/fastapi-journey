# DECISIONS.md

## 1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?

An ODM (Object Document Mapper) is a tool that lets us work with the database using Python classes instead of writing raw MongoDB queries. Instead of manually writing queries like insert or find, we define models (like Event and User), and Beanie handles the communication with MongoDB.

I used Beanie because it makes the code cleaner and easier to understand. For example, calling `document.insert()` is simpler than writing a full MongoDB query. It also integrates well with FastAPI and Pydantic, so validation and structure are already handled. Without Beanie, I would have to write more complex and repetitive database code.

---

## 2. What is the role of the Database class — why wrap Beanie methods inside it instead of calling them directly in routes?

The Database class acts as a middle layer between the routes and the database. Instead of calling Beanie methods directly inside the route functions, all database operations go through this class.

This makes the code more organized and easier to maintain. If I need to change how data is stored or retrieved, I only need to update the Database class instead of every route. It also keeps the routes focused on handling requests and responses, not database logic.

---

## 3. What happens if initialize_database() is not called on startup? What would break and why?

If `initialize_database()` is not called, Beanie will not be connected to MongoDB. That means the document models (Event and User) will not be registered, and any database operation will fail.

For example, trying to insert or retrieve data would cause errors because the connection to MongoDB was never initialized. Basically, the app would run, but any endpoint that uses the database would not work.

---

## 4. What is the difference between the Event document and the EventUpdate model, and why are they two separate classes?

The Event document represents the full data stored in the database. All required fields must be provided when creating a new event.

The EventUpdate model is used for updating an existing event. All its fields are optional, so I can update only specific fields without sending the entire object.

They are separate because creation and update operations have different requirements. If I used the same model for both, I would be forced to provide all fields even when I only want to update one, which is not practical.