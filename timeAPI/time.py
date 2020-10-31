import functools
from datetime import datetime


from flask import (
    Blueprint, request, session, url_for
)

bp = Blueprint('time', __name__, url_prefix='/time')

@bp.route('/now', methods=['POST'])
def now():
        timeFormat = request.form['timeFormat']
        error = None
        now = datetime.now()
        if timeFormat == None:
            error = 'format is required.'
        if timeFormat == 'True':
            return now.strftime("%Y-%m-%d %H:%M:%S")
        if timeFormat == 'False':
            return now.strftime("%Y-%m-%d")

        return timeFormat
