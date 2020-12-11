from flask import Blueprint , render_template

record_class = Blueprint('record_class',__name__,url_prefix='/record_class/')

@record_class.route('/')
def index():
    return render_template('record_class/record_class.html')






@record_class.route('/class_7/')
def class_7():
    return render_template('record_class/class_7.html')


@record_class.route('/class_8/')
def class_8():
    return render_template('record_class/class_8.html')


@record_class.route('/class_9/')
def class_9():
    return render_template('record_class/class_9.html')



@record_class.route('/class_9/math/')
def math_record():
    return render_template('record_class/class_9/math.html')

@record_class.route('/class_9/oloom/')
def oloom_record():
    return render_template('record_class/class_9/oloom.html')

@record_class.route('/class_9/persian/')
def persian_record():
    return render_template('record_class/class_9/persian.html')

@record_class.route('/class_9/arabic/')
def arabic_record():
    return render_template('record_class/class_9/arabic.html')

@record_class.route('/class_9/motaleat/')
def motaleat_record():
    return render_template('record_class/class_9/motaleat.html')

@record_class.route('/class_9/qoran/')
def qoran_record():
    return render_template('record_class/class_9/qoran.html')

@record_class.route('/class_9/payamha/')
def payamha_record():
    return render_template('record_class/class_9/payamha.html')

@record_class.route('/class_9/negaresh/')
def negaresh_record():
    return render_template('record_class/class_9/negaresh.html')

@record_class.route('/class_9/amadegy/')
def amadegy_record():
    return render_template('record_class/class_9/amadegy.html')

