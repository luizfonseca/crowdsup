#! /usr/bin/python
#! coding: utf-8

from flask import Flask, request, render_template, url_for, redirect, abort, flash, session
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='128739hhahsdgasgq736$$(1928::1283183126{}',
))


def connect():
    return MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="marina_whatsapp", port=8889)


@app.route("/")
def start():
    return render_template('index.html', phones=all_phones())



@app.route("/phone/create", methods=['POST'])
def save_phone():
    if (request.form['phone_number'] == ''):
        flash('Telefone não pode ficar em branco.')
        return redirect(url_for('start'))

    db = connect()
    c = db.cursor()
    c.execute("""
            INSERT INTO cellphones (phone) 
            VALUES (%s)
            """, request.form['phone_number'])

    db.commit()

    flash('Telefone salvo com sucesso')
    return redirect(url_for('start'))




def all_phones():
    db = connect()
    db.cursor()

    db.query("""SELECT * FROM cellphones""")
    result = db.store_result()
    phones = result.fetch_row()
    db.close()
    return phones


if __name__ == "__main__":
    app.run()
