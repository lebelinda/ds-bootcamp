from flask import Flask, jsonify
import os
import yaml

dir_path = os.path.dirname(os.path.realpath(__file__))
MAX_VALUE = 10000
MIN_VALUE = 0


def create_app():
    app = Flask(__name__)
    with open(os.path.join(dir_path, 'yaml', 'belinda_model.yaml')) as f:
        belinda_model = yaml.load(f, Loader=yaml.SafeLoader)

    @app.route("/belinda")
    def hello_world():
        return "Hello World", 200

    @app.route("/belinda_model/<submodel>/<x_1>")
    def belinda_yaml_model(submodel, x_1):
        if int(x_1) > MAX_VALUE:
            return f"Value {x_1} > {MAX_VALUE}", 400
        elif int(x_1) < MIN_VALUE:
            return f"Value {x_1} < {MIN_VALUE}", 400
        try:
            model = belinda_model[submodel]
        except KeyError:
            return 'Model not found', 404
        dict_ = {'score': model['b_0'] +
                 model['b_1'] * int(x_1)}
        return jsonify(dict_)

    @app.route("/belinda_bye")
    def bye_world():
        return "Bye World", 200

    return app
