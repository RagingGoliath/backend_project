from flask import Flask, render_template #Imports Flask
from views import Views #Imports the views file

app = Flask(__name__) #Defines what website is

#404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

app.register_blueprint(Views, url_prefix = "/") #Specifies page location

#For testing purposes, turns debug on and sets port to 8000
if __name__ == "__main__":
    app.run(debug=True, port = 8000)