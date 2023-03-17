from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import ninja
from flask_app.models import dojo

@app.route("/dojos")
def home():
    all_dojos = dojo.Dojo.get_all_dojos()
    for one_dojo in all_dojos:
        print(one_dojo.name)
    return render_template("dojos.html", dojos=all_dojos)

@app.route("/dojos/<int:id>")
def show_dojo(id):
    ninjas = ninja.Ninja.get_one_dojo_with_ninjas(id)
    one_dojo = dojo.Dojo.get_dojo_by_id(id)
    print(one_dojo)
    return render_template("dojo_show.html", ninjas=ninjas, dojo=one_dojo)

@app.route("/dojos/create", methods=['POST'])
def create_dojo():
    new_dojo = dojo.Dojo.create_dojo(request.form) # this does an insert, which returns the id
    return redirect(f"/dojos/{new_dojo}") #so I can just pass the id here