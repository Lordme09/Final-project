from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd

app = Flask(__name__)
DATABASE='sqlite:///donations.db'
app.secret_key = 'your-secret-key-here'  # Required for flash messages

#Page Routes: show different pages of the website
@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/donate_page")
def donate_page():
    return render_template("donate_page.html")

@app.route("/available_items_page")
def available_items_page():
    #Read from SQLite database
    df = pd.read_sql('SELECT * FROM donations', con='sqlite:///donations.db')
    #Convert to list of dictonaries for template
    donations = df.to_dict('records')
    return render_template('available_items_page.html', donations=donations)

#Donation Form Submission (recieves the data from the form, approves it and saves to database)
@app.route('/donations', methods=['POST'])
def add_donation():
    #get info from form
    name = request.form.get('name', '')
    category = request.form.get('category', '')
    description = request.form.get('description', '')
    location = request.form.get('location', '')
    contact_info = request.form.get('contact_info', '')

    # Validation
    errors = []

    if not name:
        errors.append('Name is required. Try Again!')

    if not category:
        errors.append('Category is required. Try Again!')

    if not description:
        errors.append('Description is required. Try Again!')

    if not location:
        errors.append('Location is required. Try Again!')

    if not contact_info:
        errors.append('Contact Information is required. Try Again!')

    if errors:
        # Flash error messages
        for error in errors:
            flash(error, 'error')
        return redirect(url_for('available_items_page'))
    
    # Create DataFrame with new donations
    new_donations = pd.DataFrame([{
        'name': name,
        'category': category,
        'description': description,
        'location': location,
        'contact_info': contact_info
    }])
    #Append new donations to database
    new_donations.to_sql('donations', con=DATABASE,if_exists='append',index=False)

    #Shows a successful donation
    flash('Thank you for your donation! The item has been added to the Available Items page', 'success')
    return redirect(url_for('available_items_page'))

if __name__ == '__main__':
    app.run(debug=True)