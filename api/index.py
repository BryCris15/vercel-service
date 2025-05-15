from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¿Sabías que aprender en red distribuye el conocimiento? ¡Tú también puedes hacerlo!"

# Vercel espera una función WSGI-style
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
