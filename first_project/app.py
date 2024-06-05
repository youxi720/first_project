from flask import Flask
from flask import render_template, request, redirect, url_for, render_template, g
import sqlite3

app = Flask(__name__)
app.config["DATABASE"] = "compliments.db"

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

@app.route('/')
def index():
    db = get_db()
    random_compliment = db.execute('SELECT * FROM compliments ORDER BY RANDOM() LIMIT 1').fetchone()
    return render_template('index.html', compliment=random_compliment)

@app.route('/delete/<int:compliment_id>')
def delete(compliment_id):
    db = get_db()
    db.execute('DELETE FROM compliments WHERE id = ?', [compliment_id])
    db.commit()
    return redirect(url_for('index'))

@app.route("/create.html", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        db = get_db()
        message = request.form['message']
        db.execute('INSERT INTO compliments (message) VALUES (?)', [message])
        db.commit()
        return redirect(url_for('index'))
    else:
        return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True)