from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¿Sabías que aprender en red distribuye el conocimiento? ¡Tú también puedes hacerlo!"

# Solo expón la app, sin handler extra

