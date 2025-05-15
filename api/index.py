from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¿Sabías que aprender en red distribuye el conocimiento? ¡Tú también puedes hacerlo!"

# Entry point for Vercel
def handler(request, context):
    return app(request.environ, start_response=context['start_response'])
