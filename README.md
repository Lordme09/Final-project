What the app does
- People can donate items they no longer need
- View items that othe rpeople have donated (filter)
- Can add item information that is saved and shown on the Available Items Page

How to install dependencies and run it locally
- Install dependencies thorugh pip install requirement.txt
- Create the database: python create_database.py
- Run python app.py
- Open http://127.0.0.1:5000 in browser

Which point(s) your team completed and where to find them in the code (e.g. "POST endpoint at /submit in app.py")
- Persistent Data Store: Saved donation information using a SQLite database (donations.db) It can be found in app.py and create_database.py
- Meaningful POST Usage: Used /donation POST to recive donation form infromation, approve it, and saves the new donatins to the database. It can be found in app.py 

Any known limitations
- Only runs locally(not public)
- No messaign system between donors and people wanting to get the item
- Can't create accounts/log in
- People can't fix or delete donations
