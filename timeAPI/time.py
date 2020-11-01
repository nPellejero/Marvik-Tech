import functools
from datetime import datetime


from flask import (
    Blueprint, request, session, url_for
)

bp = Blueprint('time', __name__, url_prefix='/time')

@bp.route('/now', methods=['POST'])
def now():
        timeFormat = request.form['timeFormat']
        now = datetime.now()
        if timeFormat == None:
            return 'format is required.'
        elif timeFormat == 'True':
            return now.strftime("%Y-%m-%d %H:%M:%S")
        elif timeFormat == 'False':
            return now.strftime("%Y-%m-%d")
        else:
            return 'format not recognized.'
