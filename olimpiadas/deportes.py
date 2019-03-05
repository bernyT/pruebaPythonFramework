from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from olimpiadas.auth import login_required
from olimpiadas.db import get_db

bp = Blueprint('deportes', __name__)

@bp.route('/deportes')
def index():
    db = get_db()
    deportes =  db.execute(
        'SELECT d.id, d.nombre'
        ' FROM deporte d '
        ' ORDER BY d.id'
    ).fetchall()
    return render_template('deportes/index.html', deportes=deportes)

@bp.route('/deportes/crear', methods=('GET','POST'))
@login_required
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        error = None

        if not nombre:
            error = 'El nombre es requerido.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO deporte (nombre)'
                ' VALUES (?)',
                (nombre,)
            )
            db.commit()
            return redirect(url_for('deportes.index'))


    return render_template('deportes/crear.html')


@bp.route('/deportes/<int:id>/', methods=('GET', 'POST'))
@login_required
def update(id):
    if request.method == 'POST':
        pass

    return render_template('deportes/update.html', deporte=deporte)

