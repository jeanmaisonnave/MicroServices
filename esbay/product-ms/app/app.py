from flask import Flask
import models

app = Flask(__name__)

app.config.update(
    dict(
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@user_db/product',
    )
)

models.init_app(app)
models.create_tables(app)
@app.route('/products/welcome')
def hello():
    return 'Hello, welcome to the ESBAY Product API`\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
