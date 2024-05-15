from flask import render_template, Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


@app.route('/', methods=['GET', 'POST'])
def register():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
