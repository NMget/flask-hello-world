from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message


app = Flask(__name__)

mail = Mail(app)


Bootstrap(app)

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = False
MAIL_USERNAME = 'megnet.noah@gmail.com'
MAIL_PASSWORD = 'Net4G@h03m'


@app.route('/')
def index():
    Titre = "Accueil"
    Content = "index.html"
    return render_template("bone.html", Titre=Titre, Content="accueil.html")

@app.route('/profil')
def profil():
    Titre = "Profil"
    Content = "profil.html"
    return render_template("bone.html", Titre = Titre, Content=Content)

@app.route('/sio')
def sio():
    Titre='BTS SIO'
    Content = 'SIO.html'
    return render_template('bone.html', Titre=Titre, Content=Content)

@app.route('/DGFiP')
def DGFiP():
    Titre='DGFiP'
    Content = 'DGFiP.html'
    return render_template('bone.html', Titre=Titre, Content=Content)

@app.route('/projets')
def projets():
    Titre='Projets'
    Content = 'projets.html'
    return render_template('bone.html', Titre=Titre, Content=Content)

@app.route('/veille')
def veille():
    Titre="Veille"
    Content="veille.html"
    return render_template('bone.html', Titre=Titre, Content=Content)

@app.route('/contact')
def contact():



    Titre="contact"
    Content="contact.html"
    return render_template('bone.html', Titre=Titre, Content=Content)

if __name__ == '__main__':
    app.run(debug=True)