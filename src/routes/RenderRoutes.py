from flask import Flask, render_template

class RenderRoutes:
    def __init__(self):
        self.app = Flask(__name__)

    def routes(self):
        @self.app.route('/')
        def index():
            return render_template('login.html')