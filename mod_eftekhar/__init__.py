from flask import Blueprint , render_template

eftekhar_afarinan = Blueprint('eftekhar_afarinan',__name__,url_prefix='/eftekhar_afarinan')

@eftekhar_afarinan.route('/')
def index():
    return render_template('links/eftekhar_afarinan.html')