from flask import render_template , request,redirect , url_for , flask
from . import worker
import database


app = Flask(__name__)

db = database.Database()
db.load_db()


@app.route("/" , methods = ["GET" , "POST"])
def index():

    if request.method == 'GET':
        return render_template("index.html" , code = "" , href = "")

    if request.method == 'POST':
            code = database.Code()
            code.data = request.form["data"]
            db.save_code(code)
            return '{}'.format(name)



@app.route("/<id>" , methods = ["GET" , "POST"])
def code(id):
    result = worker.loadCode(id)
    
    if result:
        return render_template("index.html" , code = result , href = id )
    else:
        return render_template("index.html" , code = "" , href = '')    

    
app.run()





