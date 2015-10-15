
from flask import flash,render_template,redirect,url_for,request,session,escape
#from flask.ext.login import login_user, logout_user, current_user, login_required
#from app import app,models,lm,db
from app import app,models,db
from .models import User

#@lm.user_loader
#def load_user(user_id):
 #   return User.query.get(int(user_id))
    #return User.query.get(user_id)
    
#@app.before_request
#def before_request():
 #   g.user = current_user



#@app.route('/',methods = ['GET', 'POST'])  
#@app.route('/index',methods = ['GET', 'POST'])
#def index():
 #   if request.method =="POST":
        #session["remember_me"]=request.form["remember_me"]
        #flash(g.user,"info")
  #      users=models.User.query.all()
   #     for u in users:
    #        if u.username==request.form["Username1"]:
     #           if u.password==request.form["Password1"]:
      #              user = User(username=u.username, password=u.password)
                    #flash(u.username+u.password)
       #             login_user(user)
        #            flash("haha","info")
        #if g.user is None or g.user.is_anonymous:
        #if current_user.is_anonymous:
         #   flash("Login failed","info")
            
        #else:
         #   flash("Login succeeded","info")
        #return redirect("/index")
    #return render_template("index.html")
    

@app.route('/',methods = ['GET', 'POST'])  
@app.route('/index',methods = ['GET', 'POST'])
def index():
    if "user" in session:
        username=escape((session['user']))
    else:
        username=None
    if request.method =="POST":
        #session["remember_me"]=request.form["remember_me"]
        #flash(g.user,"info")
        users=models.User.query.all()
        for u in users:
            if u.username==request.form["Username1"]:
                if u.password==request.form["Password1"]:
                    session["user"]= u.username
                    #flash(u.username+u.password)
                    #flash("haha","info")
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

    

