from flask import Flask, render_template, request, url_for, flash, redirect
from script import QRCode_generator, QRCode_generator_logo

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'D}hC~9a,KK2Jx_#5V=)L-4VGq8.rgpcz5/h8B?4J36T36ut'

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        name = request.form['name']
        logo = request.form['logo']
        if logo == "":
            qrcode = QRCode_generator(name)
            return render_template('qrcode.html', name=qrcode)
        else:
            qrcode = QRCode_generator_logo(name, logo)
            return render_template('qrcode.html', name=qrcode)
    return render_template('index.html')

@app.route('/qrcode')
def qrcode():
    return render_template('qrcode.html')

@app.route('/reponse', methods=('GET', 'POST'))
def reponse():
    if request.method == "POST":
        add_db = request.form['add_db']
        dashboard = request.form['dashboard']
        if add_db:
            return render_template('add_db.html')
        elif dashboard:
            return render_template('dashboard.html')
    return render_template('reponse.html')

@app.route('/add_db', methods=('GET', 'POST'))
def add_db():
    return render_template('add_db.html')

@app.route('/dashboard', methods=('GET', 'POST'))
def dashboard():
    return render_template('dashboard.html')