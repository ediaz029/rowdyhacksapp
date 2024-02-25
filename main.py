from flask import Flask, redirect, url_for,render_template

#WSGI APPLICATION(Communication between server and application)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)