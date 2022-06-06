from flask import Flask

def create_app():
    #create flask app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dasjkdhsajdksa"

    
    #where to look for the blueprints
    from .views import views
    from .auth import auth

    #register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
