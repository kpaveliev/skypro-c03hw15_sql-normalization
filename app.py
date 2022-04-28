from flask import Flask, render_template, request, jsonify
from dao import OutcomesDAO

# Initiate Flask app, load config and DAO
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = OutcomesDAO(app.config.get('DB_PATH'))


# Search results - API
@app.route('/<id>')
def search_by_id_api(id):
    query_result = db.get_outcome_by_id(id)
    return jsonify(query_result)


# Render main page (optional)
@app.route('/')
def index():
    id = request.args.get('s')

    # Render search form if no arguments passed
    if id is None:
        return render_template('index.html')

    # Render outcome form if argument passed
    else:
        try:
            query_result = db.get_outcome_by_id(id)
        except TypeError as e:
            return render_template('error.html', message=e)
        except ValueError as e:
            return render_template('error.html', message=e)
        else:
            return render_template('outcome.html', data=query_result)


if __name__ == '__main__':
    app.run()
