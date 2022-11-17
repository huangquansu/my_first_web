from flask import Flask, render_template, redirect, request, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired
from flask_mail import Mail, Message
import os

User = 'huangtestpy@gmail.com'
Password = os.environ.get('PASSWORD')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=User,
    MAIL_PASSWORD=Password
)

mail = Mail(app)
Bootstrap(app)

# wtform
class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        c_name = request.form['name']
        c_email = request.form['email']
        c_text = request.form['text']
        if c_name == "":
            flash("Please enter your name.")
            return redirect(url_for('home'))
        elif c_email == "":
            flash('Please enter your email.')
            return redirect(url_for('home'))
        elif c_text == "":
            flash("Don't empty please.")
            return redirect(url_for('home'))
        else:
            msg = mail.send_message(
                'Send Mail tutorial!',
                sender='huangtestpy@gmail.com',
                recipients=['huangice0519@gmail.com'],
                body=f"Name:{c_name}\n email:{c_email}\n {c_text}"
            )
            # msg = Message('First web',
            #               sender='huangtestpy@gmail.com',
            #               recipients=['huangice0519@gmail.com'])
            # msg.body = f"Name:{c_name}/n email:{c_email}/n {c_text}"
            # mail.send(msg)

        return redirect(url_for('home'))
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')