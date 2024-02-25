from flask import Flask, request, redirect, url_for, render_template
from api import get_cve
from api import process_cve_data

# WSGI APPLICATION (Communication between server and application)
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

@app.route('/search')
def search():
    cpe_name = request.args.get('cpe_name')  # Retrieve the CPE name from the query parameter
    cve_data = get_cve(cpe_name)  # Assume this calls the NVD API and gets the JSON response
    processed_data = process_cve_data(cve_data)  # Process the JSON to get relevant info
    return render_template('search_results.html', vulnerabilities=processed_data)



if __name__ == '__main__':
    app.run(debug=True)