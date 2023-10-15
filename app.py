from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notebook/')
def notebook():
    return render_template('notebook_page.html')
