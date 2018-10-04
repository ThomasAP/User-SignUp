from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('sign-up.html')

@app.route('/greeting', methods=['POST'])
def greeting():
    return render_template('greeting.html')








if __name__ == "__main__":
    app.run()