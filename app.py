from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¿Sabías que aprender en red distribuye el conocimiento? ¡Tú también puedes hacerlo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)