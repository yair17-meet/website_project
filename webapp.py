from flask import Flask
from flask import render_template
from model import *
from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
from flask import session as login_session
from flask import Flask, url_for, flash, redirect, request

ID = None

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


engine = create_engine('sqlite:///webdata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS






@app.route('/',methods = ['GET','POST'])
def main_page_html():
    if request.method == 'POST':
    	flash("Youssss")
        name1 = request.form['name']
        
        password1 = request.form['password']
        if name1 == "" or password1 == "":
            flash("Your form is missing arguments")
            return redirect(url_for('sign_up'))
        users = session.query(User).all()
        for item in users:
        	if (item.name == name1) and (item.password_hash == password1):
        		flash("loged in")
        		ID = item.id
        		return redirect(url_for('read_more_html'))
        	else:
        		return redirect(url_for('main_page_html'))

        
    else:
        return render_template('main_page.html')

@app.route('/user_view')
def user_view_html():
	user_items = session.query(User).all()
	articul_id = session.query(Articul).filter(Articul.id==2)#.all()
	return str(articul_id)#render_template('user_view.html', user_items=user_items, articul_id=articul_id)


@app.route('/sign_up', methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
    	flash("Youssss")
        name = request.form['name']
        flash(name)
        email = request.form['email']
        password = request.form['password']
        if name == "" or email == "" or password == "":
            flash("Your form is missing arguments")
            return redirect(url_for('sign_up'))
        if session.query(User).filter_by(email = email).first() is not None:
            flash("A user with this email address already exists")
            return redirect(url_for('sign_up'))
        user = User(name = name, email=email)#, password_hash=password)
        user.hash_password(password)
        session.add(user)
        session.commit()
        flash(str(user))
        return redirect(url_for('sign_up'))
    else:
        return render_template('sign_up.html')




@app.route('/read_more')
def read_more_html():

	user_items = session.query(User).all()
	articul_items = session.query(Articul).all()
	return render_template("read_more.html", user_items=user_items, articul_items=articul_items)
	
	return "please log in you dick(or sign up if you dont ave an account)"



#@app.route('/read_more/')
@app.route('/read_more/<Id>')
def view_articuls_name_html(Id):
	articul = session.query(Articul).all()#filter_by(id = id)

	for a in articul:
		if a.id == int (Id):
			break
	articul_id = a.id
	articul_name = a.name
	articul_content = a.content

	return render_template("articul.html", articul_name=articul_name,articul_content=articul_content,articul_id=articul_id)
	

@app.route('/new_articul' ,methods = ['GET','POST'])
def new_articul_html():
	if request.method == 'POST':
    	#flash("Youssss")
        name = request.form['name']
        flash(name)
        content = request.form['content']
        if name == "" or content == "":
            flash("Your form is missing arguments")
            return redirect(url_for('read_more'))
       	articul = Articul(id = ID, name = name, content = content)
        session.add(articul)
        session.commit()
        flash(str(user))
        return redirect(url_for('sign_up'))
    else:
        return render_template('sign_up.html')
	


@app.route('/aaa')
def aaa():
	i = 1
	artart = session.query(Articul).all()
	user1 = session.query(User).all()
	htmlString = ""
	for item in artart:
		htmlString +=  "<p>"+ item.name +"</p><p>" +item.content +"</p><p>" +str (item.user_id) +"</p><br><br>"
	return htmlString


#@app.route('/aaa')
#@app.route('/aaa/<name>')
#def index(name=None):
#	return render_template('main_page.html',name=name)


if __name__=='__main__':
	app.run(debug=True)
