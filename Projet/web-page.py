from flask import Flask, render_template, request, url_for, flash, redirect
from script import QRCode_generator, QRCode_generator_logo, printAllStudents, printAverage, printPrcFreq, printTopEnteprise

app = Flask(__name__)
app.config['SECRET_KEY'] = 'D}hC~9a,KK2Jx_#5V=)L-4VGq8.rgpcz5/h8B?4J36T36ut'

db_file = "./database.txt"

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

@app.route('/add_db', methods=('GET', 'POST'))
def add_db():
    if request.method == "POST":
        excel_file = request.form['excel_file']
        file = open(db_file, "w")
        file.write(excel_file)
        file.close()
        flash('Base de donnée ajoutée !', 'success')
    return render_template('add_db.html')

@app.route('/dashboard', methods=('GET', 'POST'))
def dashboard():
    db = open(db_file, "r")
    excel_file = db.read()
    if excel_file == "":
        flash('Veuillez ajouter une base de données pour visualiser le dashboard.', 'warning')
    if request.method == "POST":
        dashboard_to_display = request.form['dashboard']
        if dashboard_to_display=="prc_freq":
            img = printPrcFreq(db_file)
            return render_template('prc_freq.html', img=img)
        elif dashboard_to_display=="average":
            img = printAverage(db_file)
            return render_template('average.html', img=img)
    return render_template('dashboard.html')

@app.route('/prc_freq')
def prc_freq():
    return render_template('prc_freq.html')

@app.route('/average')
def average():
    return render_template('average.html')