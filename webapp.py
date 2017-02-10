from flask import Flask
from model import *
from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context

app = Flask(__name__)


engine = create_engine('sqlite:///webdata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()




@app.route('/')
def hello_world():
	return 'main page route'


if __name__=='__main__':
	app.run()