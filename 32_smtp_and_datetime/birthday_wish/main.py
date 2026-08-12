##################### Extra Hard Starting Project ######################
import random, pandas, smtplib, datetime as dt

my_email = "YOURS_EMAIL_HERE"
password = "APP_PASSWORD_HERE"

today = dt.datetime.now()
current_month = today.month
current_day = today.day
random_template_number = random.randint(1,3)

try:
    df = pandas.read_csv("./birthdays.csv")
    content = ""
    matching_rows = df[(df["month"] == current_month) & (df["day"] == current_day)]
    matching_rows = matching_rows.to_dict(orient="records")
    
    if not matching_rows:
        print("No one as birthday today.")
    else:
        with open(f"./letter_templates/letter_{random_template_number}.txt", 'r') as template_n:
            content = template_n.read()
        
        birtday_person = matching_rows[0]['name']
        birthda_person_email = matching_rows[0]['email']
        template = content.replace("[NAME]", birtday_person)
        

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            to_addrs=birthda_person_email,
            from_addr=my_email, 
            msg=f"Subject: Happy Birtday {birtday_person}\n\n {template}"
        )
    print("Birthday mail sent to: ", birthda_person_email)
except Exception as e:
    print("Error to send mail: ",e)



