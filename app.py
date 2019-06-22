from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auto')
def auto():
    return render_template('auto.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/quick')
def quick():
    return render_template('quick.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')
    