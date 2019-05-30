from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello World", 200

    @app.route("/bye")
    def bye_world():
        raise Exception("BLAH")
        return "Bye World", 200

    return app
