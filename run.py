from flask import Flask, render_template
from utils.load_config import load_config

app = Flask(__name__)
config = load_config()

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host=config['server']['host'],
        port=config['server']['port'],
        debug=config['server']['debug'],
    )