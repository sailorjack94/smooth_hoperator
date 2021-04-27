from flask import Flask, render_template, url_for, request

from controllers.beer_controller import beer_blueprint
from controllers.brewer_controller import brewer_blueprint

app = Flask(__name__)

app.register_blueprint(beer_blueprint)
app.register_blueprint(brewer_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

# WIP - Query string test
# @app.route('/query', methods=['GET'])
# def get_query_string():
#     return request.query_string


if __name__ == '__main__':
    app.run(debug=True)
