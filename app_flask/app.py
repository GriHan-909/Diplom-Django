from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template('base.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)