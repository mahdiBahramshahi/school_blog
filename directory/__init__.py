from flask import Flask , render_template , request ,abort, flash

app = Flask(__name__,template_folder='../templates')
app.config['SECRET_KEY'] = 'T}{1$-1$-$0-$3CR3T'


#======================================= routes ==============================================

@app.route('/')
def index():
    return render_template('index.html')





from mod_record import record_class
app.register_blueprint(record_class)

from mod_gphoto import galery_photo
app.register_blueprint(galery_photo)

from mod_eftekhar import eftekhar_afarinan
app.register_blueprint(eftekhar_afarinan)

from mod_schooldates import school_dates
app.register_blueprint(school_dates)
