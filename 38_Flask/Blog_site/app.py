from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import datetime, requests
from dotenv import load_dotenv
import os



load_dotenv()

app = Flask(__name__)

# Add this line right after initializing your app
app.secret_key = os.environ['APP_KEY']
admin_email    = os.environ['HOST_USER_EMAIL']
admin_password = os.environ['HOST_EMAIL_PASSWORD']


@app.route('/')
@app.route("/<int:id>")
def home(id=None):
    data = requests.get("https://api.npoint.io/0b5ea27fea8b7c550a9c")
    resp = data.json()
    # print(resp)
    if id:
        return render_template('post.html', posts=resp, id=id, post_time=datetime.datetime.now())
    return render_template('index.html', posts=resp, about_me="A Collection of Amit's random musings.", post_time=datetime.datetime.now())

@app.route("/about-us")
def about_us():
    return render_template("about.html", title="About Me", about_me="This is about me")


def sendMailToAdmin(name, email, message):
    
    try:
        with smtplib.SMTP('smtp.gmail.com', os.environ['SMTP_EMAIL_PORT']) as connec:
            connec.starttls()
            connec.login(user=admin_email, password=admin_password)
            connec.sendmail(
                to_addrs='amitkc.gupta@infobeans.com',
                from_addr=admin_email,
                msg=f"Subject: New Message from {name} \nHi Admin\n\n,  \n New user send a mail, here is the details of him/her:\n Name: {name}\n Email: {email}\n\n, Message: {message}. \n once you get a chance please reply to them."
            )
        return True        
    except Exception as e:
        print("Error", e)
        return False
    

@app.route("/contact-us", methods={'GET', 'POST'})
def contact_us():
    if request.method == 'POST':
        # print(request.form.get("name"))
        # Extract form data using the HTML input "name" attributes
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_message = request.form.get('message')
        
        if not user_name or not user_email or not user_message:
            flash('All fields are required!', 'error')
            return redirect(url_for('contact_us'))
        # Send mail..
        is_mail_sent = sendMailToAdmin(user_name, user_email, user_message)
        if is_mail_sent:
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact_us'))
        else:
            flash('Something went wrong to send message!', 'error')
            return redirect(url_for('contact_us'))

    return render_template("contact.html", title="Contact Me", about_me="Have questions? I have answers")



if __name__ == "__main__":
    app.run(debug=True)