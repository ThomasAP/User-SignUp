from flask import Flask, redirect, request, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user = request.form['username']
        # Include validation for username

        return render_template('greeting.html', name=user)

    return render_template('index.html')



if __name__ == "__main__":
    app.run()