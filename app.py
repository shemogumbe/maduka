from flask import Flask
from flask_graphql import GraphQLView

from config import config
from helpers.database import db_session
from flask_cors import CORS
from schema import schema

app = Flask(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    cors = CORS(app)
    config[config_name].init_app(app)

    app.add_url_rule(
        '/maduka',
        view_func=GraphQLView.as_view(
            'maduka',
            schema=schema,
            graphiql=True
        )
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    
    return app
