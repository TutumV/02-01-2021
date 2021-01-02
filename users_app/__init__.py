from flask import Flask, Blueprint
from logging import getLogger
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from users_app.config import Config

logger = getLogger(__name__)

db = SQLAlchemy()


def setup_routes(application: Flask) -> None:
    from users_app.views import sign_in, sign_up, profile
    user_bp = Blueprint('user', __name__, url_prefix='/api/users')
    user_bp.add_url_rule('/sign-in/', view_func=sign_in, methods=['POST'])
    user_bp.add_url_rule('/sign-up/', view_func=sign_up, methods=['POST'])
    user_bp.add_url_rule('/profile/', view_func=profile, methods=['GET'])
    application.register_blueprint(user_bp)


def create_app():
    application = Flask("users_app")
    application.config.from_object(Config)
    db.init_app(application)
    migrate = Migrate()
    migrate.init_app(application, db)
    setup_routes(application)
    JWTManager(application)
    return application


app = create_app()

if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
