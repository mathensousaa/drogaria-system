from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = 'drogaria.db'

@app.route('/')
def index():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    if request.method == 'GET':
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items WHERE id = ?', (id,))
        item = cursor.fetchone()
        conn.close()
        return render_template('edit.html', item=item)

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute('UPDATE items SET name=?, description=? WHERE id=?', (name, description, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_item(id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
