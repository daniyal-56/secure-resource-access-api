My Approach & Thought Process
1. Building a Solid Foundation (Database & Persistence)
I chose SQLite for persistence because it’s reliable and requires zero setup for the evaluator. I designed the schema to be fully relational, ensuring that every access request is tied to a real user and a specific resource.

Persistence: Even if you restart the server, your data stays safe.

Optimization: I added a Composite Index on the AccessRequest table. Why? Because checking if a user already has "active" access needs to be fast, even if the database grows to thousands of rows.

2. Security First (Auth & Tokens)
Security isn't just about passwords; it's about how you store them.

Hashing: I used bcrypt directly to ensure passwords are never stored in plain text.

JWT Tokens: I implemented JSON Web Tokens for session management, allowing for stateless and secure communication between the client and server.

3. Solving the Hard Problems (Race Conditions)
One of the most interesting challenges was handling Race Conditions. What if two admins click "Approve" at the exact same millisecond?

The Solution: I used Row-Level Locking (with_for_update) in SQLAlchemy. This ensures the database "locks" the request during the approval process, preventing double-approvals or data corruption.

4. Smart Expiration Logic
I implemented Automatic Access Expiration. Instead of running a heavy background task every second, I used a "Lazy Validation" approach: the system checks the timestamp every time access is requested and expires it on-the-fly if the window has passed.

🛠️ How to Run This Project
Activate your environment:

Bash
venv\Scripts\activate
Install the dependencies:

Bash
pip install -r requirements.txt
Launch the API:

Bash
uvicorn app.main:app --reload
Explore the API: Head over to http://127.0.0.1:8000/docs to use the interactive Swagger UI.

 Project Structure
app/models/: The blueprint of the data.

app/services/: The "brain" where the complex logic and locking happen.

app/routes/: The entry points for the API.

app/utils/: Security helpers for hashing and tokens.