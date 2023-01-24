import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_data(data_id):
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM data WHERE id = ?',
                        (data_id,)).fetchone()
    conn.close()
    if data is None:
        abort(404)
    return data


application = Flask(__name__)
application.config['SECRET_KEY'] = 'secretsecretsecretkey'


@application.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM data').fetchall()
    conn.close()
    return render_template('index.html', data=data)


@application.route('/<int:post_id>')
def data(data_id):
    data = get_data(data_id)
    return render_template('post.html', data=data)


# Important Create Post Function --------------------------------
@application.route('/create', methods=('GET', 'DATA'))
def create():
    if request.method == 'DATA':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


# Edit Post Function -------

@application.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


# The Delete Function -----------------------------------
@application.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


if __name__ == "__main__":
    application.run()
