from flask import Flask, redirect, request, render_template
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET','POST'])

def index():
    alpha="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    un_error = ''
    pwd_error = ''
    ver_error = '' 
    em_error = ''
    
    u_name=''
    p_word=''
    v_p_word=''
    e_mail=''
    
    user=''
    pwd=''
    ver=''
    email=''
    
    
    if request.method == 'POST':
        
        user = request.form['username']
        # Include validation for username
        #If User field is blank
        if user == '':
            un_error = "User must enter a username."
        
        #If length is greater than 20 or less than 3
        elif len(user) < 3 or len(user) > 20:
            un_error = "Username must be between 3 and 20 characters."
        
        #If username contains spaces or special characters
        for char in user:
            if char not in alpha:
                un_error = "Username can't use special characters or spaces."

        # Include validation for password       
        pwd = request.form['password']
        
        if pwd == '':
            pwd_error="User must enter a password."

        # Include validation for verify presence
        ver = request.form['verify']
        if ver == '':
            ver_error="User must verify password."
        
        # Include validation for password matching
        elif pwd != ver:
            ver_error="Passwords do not match."

        # Include validation for email formatting
        email = request.form['email']
        # Include validation for email
        confirm_at = 0
        confirm_dot = 0
        if email != '':
            for char in email:            
                if char == '@':
                    confirm_at += 1
                elif char == '.':
                    confirm_dot += 1
            if confirm_at != 1 or confirm_dot != 1:
                em_error="Invalid email address."

        if (un_error + pwd_error + ver_error + em_error) != '':
            return render_template('index.html', 
            user_name_error=un_error, 
            password_error=pwd_error, 
            verify_error=ver_error, 
            email_error=em_error, u_name=user, p_word=pwd, v_p_word=ver, e_mail=email )    
        else:
            return render_template('greeting.html', uname=user)

    return render_template('index.html', u_name=user, p_word=pwd, v_p_word=ver, e_mail=email )




if __name__ == "__main__":
    app.run()