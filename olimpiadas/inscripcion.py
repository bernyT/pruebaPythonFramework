from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from olimpiadas.auth import login_required
from olimpiadas.db import get_db

bp = Blueprint('inscripcion', __name__)

@bp.route('/')
def index():
    db = get_db()
    alumnos =  db.execute(
        'SELECT a.id, a.nombre, a.apellido, a.dni'
        ' FROM alumno a JOIN facultad f ON a.facultad_id = f.id'
        ' JOIN deporte d ON a.deporte_id = d.id'
        ' ORDER BY a.id'
    ).fetchall()
    return render_template('inscripcion/index.html', alumnos=alumnos)