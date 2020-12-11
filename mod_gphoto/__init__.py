from flask import Blueprint , render_template

galery_photo = Blueprint('galery_photo',__name__,url_prefix='/galery_photo')

@galery_photo.route('/')
def index():
    return render_template('links/galery_photo.html')

