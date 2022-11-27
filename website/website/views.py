from flask import Blueprint, render_template, request
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


@views.route('sobre.html')
def sobre():
   return render_template('sobre.html')


#@views.route('qdr.html', methods=['post'])
#def qdr():
#   quadro = request.form.get('quadro')
#   return render_template('qdr.html', quadro=quadro)




