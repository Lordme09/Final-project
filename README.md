# CommunityGive 

> A web app that allows people to donate items they no longer need and allows people to look up items listed for donation, so they can contact the owner through contact information and receive the item

>This app is particaly intersting and usful because it shows how imortant it's to reuse item and help one another

# Application Tutorial 

## Home Page
![Homepage Screenshot](image/home_page.png)

>The home page introduces CommunityGive and its misson. The navigation bar guides to the other pages of the application

## Donate An Item Page
![Donate Page Screenshot](image/donate_page.png)

Files: donate_page.html, app.py

>The Donate An Item page allows users to submit items they would like to donate through a form

Users provide:
- Item name
- Category
- Description
- Location
- Contact Information

The form sends data using a POST request

>@app.route('/donations', methods=['POST'])
def add_donation():

This route recieves the information from the donation and saves it into the SQLite database

### Database Storage
Files: create_database.py, app.pyy

>CommunityGive uses a SQLite database(donations.db) to store information from the donation

The database stores:
- Item name
- Category
- Description
- Location
- Contact Information

>donations_df = pd.DataFrame(donations_data)
>donations_df.to_sql('donations',con='sqlite:///donations.db' if_exists='replace',index=False)
>print("Database created successfully!")

This code creates and stores the submitted item so it can be shown on the Available Items Page

## Available Items Page
![Available Items Page Screenshot](image/available_items_page.png)

The Available Items page shows donated items submitted by users

Users can:
- Filter items by category
- View item detials
- Browse avaible otems
- Contact onwer to arrange pickup

FIles: avaiable_tems_page.html, app.py

>@app.route("/available_items_page")
>def available_items_page():
    >df = pd.read_sql('SELECT * FROM donations', con='sqlite:///>donations.db')
    >donations = df.to_dict('records')
    >return render_template('available_items_page.html', >donations=donations)

The page gets the infromatino from the donatinon form from the SQLite database and shows the items for the users to view

# Installation and Local Setup
- Install dependencies using pip install -r requirements.txt
- Run python app.py
- Open http://127.0.0.1:5000 in browser

# Known Limitation

- Only runs locally (not public)
- No messaging system between the donors and people wanting to get the item
- Can't create accounts/log in
- People can't fix or delete donations












