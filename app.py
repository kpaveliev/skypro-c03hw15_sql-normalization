from flask import Flask, render_template, request, jsonify
from dao import OutcomesDAO

# Initiate Flask app, load config and DAO
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = OutcomesDAO(app.config.get('DB_PATH'))


# Search results - API
@app.route('/<int:id>')
def search_by_id_api(id):
    query_result = db.get_outcome_by_id(id)
    return jsonify(query_result)


# Render main page (optional)
@app.route('/')
def index():
    return render_template('index.html')


# Render search results (optional)
@app.route('/search/')
def search_by_id():
    id = request.args.get('s')
    query_result = db.get_outcome_by_id(id)
    return render_template('list.html', data=query_result)


if __name__ == '__main__':
    app.run()