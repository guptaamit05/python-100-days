import smtplib
import json, random

my_email = "YOURS_EMAIL_HERE"
password = "APP_PASSWORD_HERE"


# Read a random Quote from the json file...
random_quote = ""
with open('./data.json', 'r') as json_data:
    data = json.load(json_data)
    random_json = random.choice(data)
    random_quote = random_json['q']


with smtplib.SMTP("smtp.gmail.com") as new_connection:   
    try:
        # new_connection.starttls()  # make the connection secure..
        # new_connection.login(user=my_email, password=password)
        if random_quote:
            # new_connection.sendmail(
            #     from_addr=my_email, 
            #     to_addrs='abc@gg.com, 
            #     msg=f"Subject: Hi Shubham, Happy Birthday to you. \n\n  {random_quote}.",
            # )
            print(f"Mail sent success with random quote: {random_quote}...")
        else:
            print("No random quote found!")
       
    except Exception as e:
        print("Error: ", e)

#############################################################################

# --- DateTime Module
import datetime as dt
# now = dt.datetime.now()
# print(now.date(), now.year,  now.month, now.day,  now.hour, now.minute,  now.second, now.microsecond)

