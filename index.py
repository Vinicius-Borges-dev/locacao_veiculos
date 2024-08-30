from flask import Flask, render_template
from src.routes.RenderRoutes import RenderRoutes

class Index:
    def __init__(self):
        self.app = Flask(__name__)
        RenderRoutes.routes(self)
    
if __name__ == '__main__':
    index = Index()
    index.app.run(debug=True)