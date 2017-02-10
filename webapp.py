from flask import Flask
from model import *


app = Flask(__name__)


engine = create_angine('sqlite:///webdata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()




@app.route('/')
def hello_world():
	return 