from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import ninja
from flask_app.models import dojo

@app.route("/ninjas")
def create_ninja_form():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos=dojos)

@app.route("/ninjas/create/", methods=['POST'])
def create_ninja():
    data = {
        **request.form
    }
    dojo_id = ninja.Ninja.create_ninja(data)
    return redirect(f"/dojos/{dojo_id}")