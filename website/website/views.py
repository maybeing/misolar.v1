from flask import Blueprint, render_template, request
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", estadoTela1 = "inline",estadoTela2 ="none",estadoTela3 ="none",estadoTela4 ="none")

@views.route('sobre.html')
def sobre():
   return render_template('sobre.html')
