from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c3209OIOPP901QOU8c2u'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
# login = LoginManager(app)
# photos = UploadSet('photos', IMAGES)
# pdf = UploadSet('pdf', ['pdf','jpg','png','jpeg','wav'],'wav')
# configure_uploads(app, photos)
# configure_uploads(app, pdf)
# login.login_view = 'login'
from .models import ( Project, Order
)

# admin = Admin(app, name = 'Highlight', template_mode= 'bootstrap3')
# admin.add_views(
# 	ModelView(User, db.session),
# 	ModelView(Note, db.session)
# )

from app import views,models
