from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

class Articul(Base):
    __tablename__ = 'articul'
    #__table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)
    user_id = Column(Integer)
 #   user = relationship("User",back_populates="articul")
    #comment = relationship("Comment", back_populates="articul") 
    def __str__(self):
        return "name: " + self.name + " content: " + self.content + " user_id: " + str(self.user_id)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password_hash = Column(String(255))  
#    articul_id = Column(Integer, ForeignKey("articul.id"))
 #   articul = relationship("Articul", back_populates="user")
    #comment = relationship("Comment", back_populates="user")
    def __str__(self):
        return "name: " + self.name + " email: " + self.email + " pass: " + self.password_hash


    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class Comment(Base):
	__tablename__ = 'comment'
	id = Column(Integer, primary_key=True)
#	user = relationship("User", back_populates="comment")
	user_id = Column(Integer, ForeignKey('user.id'))
	content = Column(String)
#	articul = relationship("Articul", back_populates="comment")
#	articul_id = Column(Integer, ForeignKey('articul.id'))




















engine = create_engine('sqlite:///webdata.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()