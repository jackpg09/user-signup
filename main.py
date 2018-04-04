from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home_page.html',username = '',password = '',
            verify = '', email = '')

@app.route("/", methods=['POST'])
def enter_info():
    user = request.form['username']
    p_word = request.form['password']
    vp_word = request.form['verify']
    e_mail = request.form['email']

    user_error = ''
    password_error = ''
    verify_error = ''
    e_mail_error = ''


    if user == "" or len(user) < 3 or len(user) > 20 or (" " in user):
        user_error = "Please type in a valid username."
    
    if p_word == "" or len(p_word) < 3 or len(p_word) > 20 or " " in p_word:
        password_error = "Please type in a valid password."

    if vp_word == "" or vp_word != p_word:
        verify_error = "Password does not match."
    
    if e_mail != "":
        if ("@" or ".") not in e_mail:
            e_mail_error ="Please enter valid e-mail address."
        if (" " in e_mail) or (len(e_mail) < 3 or len(e_mail) > 20):
            e_mail_error ="Please enter valid e-mail address."

    if not user_error and not password_error and not verify_error and not e_mail_error:
        return redirect('/success?user={0}'.format(user))   

    return render_template('home_page.html', error1=user_error,
            error2=password_error,error3=verify_error,error4=e_mail_error,username=user,email=e_mail)

@app.route("/success")
def success():
    user = request.args.get('user')
    return render_template('success.html', username=user)
app.run()