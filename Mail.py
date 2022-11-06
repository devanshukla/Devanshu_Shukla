from flask import *
from flask_mail import *
from random import *
import re
app = Flask(__name__)
mail = Mail(app)
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'username@gmail.com'
app.config['MAIL_PASSWORD'] = '*************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
otp = randint(000000, 999999)


@app.route('/')
def index():
    return render_template("homepage.html")


@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        msg = Message('OTP', sender='username@gmail.com', recipients=[email])
        msg.body = str(otp)
        mail.send(msg)
        return render_template('verify.html')
    return "<h3>!Enter Valid Email Address!</h3>"


@app.route('/verify', methods=["POST"])
def resend():
    email = request.form["email"]
    msg = Message('OTP', sender='username@gmail.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template('verify.html')


@app.route('/validate', methods=["POST"])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3> Email  verification is  successful </h3>"
    return "<h3>!OTP not valid!</h3>"


if __name__ == '__main__':
    app.run(debug=True)
