from flask import Flask, render_template, url_for, request
from flask_mail import Mail, Message
import datetime
app = Flask(__name__)
port = 2000



@app.route("/<name>")
def error(name):
    return "<html> <h1>Page {} does not exist</h1> </html>".format(name)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/aboutus")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact-processor")
def contactProcessor():
    return render_template("contact-processor.php")

@app.route("/formSent")
def formSent():
    return render_template("formSent.html");

@app.route("/eachofus")
def eachofus():
    name = request.args.get('name')
    name = name.lower()
    if(name=='gunvir'):
        favSport=''
        career =''
        age = int(datetime.datetime.now().strftime("%Y")) - 2005
        message = "Hey! I'm a leader, entrepeneur, and a developer"
        instagram='https://www.instagram.com/coding.noobie/'
        linkedin='https://www.linkedin.com/in/gunvir-dhesi-51218a211/'

    elif(name=='rajan'):
        favSport=''
        career =''
        age = int(datetime.datetime.now().strftime("%Y")) - 2005
        message = 'Hi! I’m a developer, designer, author, entrepreneur and economic writer'
        instagram='https://www.instagram.com/itsrajan05'
        linkedin='https://www.linkedin.com/in/itsrajan05'

    elif(name=='vivek'):
        favSport=''
        career =''
        age = int(datetime.datetime.now().strftime("%Y")) - 2004
        message = 'I love coding'.format(age=age, name=name)
        instagram='https://www.instagram.com/_vivek.04/'
        linkedin=''
    elif(name=='manvir'):
        favSport=''
        career =''
        age = int(datetime.datetime.now().strftime("%Y")) - 2008
        message = 'Hello, I am Manvir and I love astronomy. With my passoin for programing and astronomy, in near future I want to help in the exploration of space via programming'.format(name=name)
        instagram=''
        linkedin=''
    elif(name=='cameron'):
        favSport=''
        career ='Undecided'
        age = int(datetime.datetime.now().strftime("%Y")) - 2006
        message = 'Hey, I am {{name}}, and I am love designing Websites!'.format(name=name)
        instagram=''
        linkedin=''
    else:
        return 'error'



    return render_template("eachofus/eoubase.html",age=age, linkedin=linkedin, name=(name).capitalize(), message=message, favSport=favSport, career =career , instagram=instagram)





if __name__ == "__main__":
    app.run(debug=True,port=port);
