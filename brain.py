from flask import Flask, render_template, request
import datetime
import numpy as np
import sqlite3 as sql
from subprocess import Popen, PIPE
#from zufallswerte import zufallswerte

app=Flask(__name__)

@app.route("/")
def hello():
    now=datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData={
        'title': 'Hello!',
        'time': timeString
        }
    return render_template('main.html', **templateData)

@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route("/addrec", methods=['POST','GET'])
def addrec():
    if request.method == 'POST':

        try:
            user = request.form['user']
            vorname = request.form['vorname']
            nachname = request.form['nachname']
            geb = request.form['geb']
            geschl = request.form['geschl']

            with sql.connect('./data/ibike.sqlite') as con:
                cursor=con.cursor()
                cursor.execute("INSERT INTO tblFahrer(Username,Vorname,Nachname,Geburtsdatum,Geschlecht) Values(?,?,?,?,?);", (str(user),str(vorname),str(nachname),str(geb),str(geschl)))

                con.commit()

        except:
            con.rollback()
            msg = "Datensatz konnte nicht hinzugefügt werden"

        finally:
            return
            con.close()

@app.route("/fahrer")
def fahrer():
    con=sql.connect('./data/ibike.sqlite')
    con.row_factory=sql.Row

    cursor=con.cursor()
    cursor.execute("select * from tblFahrer;")

    rows=cursor.fetchall()
    return render_template("fahrer.html", rows=rows)


@app.route('/test')
def run():

    Popen(['python', './apps/test2.py'], stdout = PIPE )
    return render_template('test.html')

@app.route('/action', methods=['POST', 'GET'])
def action():
    if request.method == 'POST':
        try:
            a=request.form['basis']
            Data={'a':a}
            process=Popen(['python', './apps/test.py'], stdin = PIPE,stdout=PIPE )
            process.stdin.write(int(a).to_bytes(1, byteorder='little'))
            process.stdin.close()
        finally:

            return render_template('action.html', **Data)

if __name__== "__main__":
    app.run(host='', port=8000, debug=True)
