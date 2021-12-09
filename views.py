from flask import Flask, render_template, url_for, redirect, Blueprint
render_template

#Creates page blueprint
Views = Blueprint(__name__, "views")

#create home page
@Views.route("/")

def homepage():
    #Name of home page function
    return render_template("index.html")

#To redirect to home page
@Views.route("/home")

#Adds the actual redirection
def home_redirect():
    return redirect(url_for("views.homepage"))

#To redirect to home page
@Views.route("/javascript")

#Adds the actual redirection
def javascript_redirect():
    return redirect(url_for("views.homepage"))

#To redirect to home page
@Views.route("/js")

#Adds the actual redirection
def js_redirect():
    return redirect(url_for("views.homepage"))

@Views.route("/admin")

def admin_page():
    return render_template("admin.html")

@Views.route("/about")

def about_page():
    return render_template("About.html")

@Views.route("/tutorials")

def tutorials_page():
    return render_template("tutorials.html")

@Views.route("/page4")

def page_four():
    return render_template("page_four.html")

@Views.route("/page5")

def page_five():
    return render_template("page_five.html")