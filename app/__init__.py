from flask import Flask
from app.main.controllers import main
from app.sub01.controllers import sub01


app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(sub01, url_prefix='/sub01')
