from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Cześć, tu Olga! Witaj na mojej stronie!'

if __name__ == '__main__':
    app.run()
