from flask import Blueprint , render_template

school_dates = Blueprint('school_dates',__name__,url_prefix='/school_dates')

@school_dates.route('/')
def index():
    return render_template('links/school_dates.html')