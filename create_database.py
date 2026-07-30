import pandas as pd

#create dataframe w/items
donations_data = {
    'name': ["Couch", "Dress"],
    'category': ["Household Goods and Home Items", "Clothing, Footwear, and Accessories"],
    'description': ["A soft brown leather couch", "A dark blue sparkly dress"],
    'location': ["123 Street Way","098 Cir Way"],
    'contact_info': ["123-456-7890", "098-765-4321"]
}

#donation data into dataframe
donations_df = pd.DataFrame(donations_data)

#save to SQLite database
donations_df.to_sql('donations',con='sqlite:///donations.db',if_exists='replace',index=False)

print("Database created successfully!")

