from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', message='Hello, world!')

if __name__=='__main__':
    app.run('0.0.0.0', 8000)
