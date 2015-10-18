
from flask import flash,render_template,redirect,url_for,request,session,escape
from app import app,models,db
from .models import User

@app.route('/',methods = ['GET', 'POST'])  
@app.route('/index',methods = ['GET', 'POST'])
def index():
    if "user" in session:
        username=escape((session['user']))
    else:
        username=None
    if request.method =="POST":
        users=models.User.query.all()
        for u in users:
            if u.username==request.form["Username1"]:
                if u.password==request.form["Password1"]:
                    session["user"]= u.username
        if "user" in session:
            flash("Login succeeded","info")
            
        else:
            flash("Login failed","info")
        return redirect(url_for('index'))
    return render_template("index.html",username=username)
    
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out")
    return redirect(url_for('index'))

    

