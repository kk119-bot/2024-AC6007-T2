from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__=="__mian__":
    app.run()

