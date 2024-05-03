import os
from flask_admin import Admin
from models import db, User, Personas,Planetas, Naves, FavoritosNaves, FavoritosPersonas,FavoritosPlanetas  ## , MODELO QUE TOQUE
from flask_admin.contrib.sqla import ModelView


 ##apartir 16, modelos aqui, cambiar user por 


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    #user models without adding this won't show on the admin section we had// but for this we need html??
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Personas, db.session))
    admin.add_view(ModelView(Planetas, db.session))
    admin.add_view(ModelView(Naves, db.session))
    admin.add_view(ModelView(FavoritosNaves, db.session))
    admin.add_view(ModelView(FavoritosPersonas, db.session))
    admin.add_view(ModelView(FavoritosPlanetas, db.session))


    
    ##admin.add_view(ModelView(Planeta, db.session))  estoy tiene que star IMPORTADO

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))

    #endpoint @ GET ALL "user"
   