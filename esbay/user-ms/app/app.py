from flask import Flask
import models

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="This is an INSECURE secret!! DO NOT use this in production!!",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@user_db/user',
))

models.init_app(app)
models.create_tables(app)

@app.route('/api/users', method=['GET'])
def get_users():
    data = []

    for row in models.User.query.all():
        data.append(row.to_json())

    response = jsonify(data)

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
