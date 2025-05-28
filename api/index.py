from flask import Flask
from vercel_wsgi import handle_request

app = Flask(__name__)

@app.route('/')
def home():
    return "¿Sabías que aprender en red distribuye el conocimiento? ¡Tú también puedes hacerlo!"

# Esta es la función que Vercel usará para ejecutar tu app
def handler(environ, start_response):
    return handle_request(app, environ, start_response)
