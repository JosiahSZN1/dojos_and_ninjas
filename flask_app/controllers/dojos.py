from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import dojo, ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def render_dojo_page():
    return render_template('dojo.html', all_dojos = dojo.Dojo.get_all_dojos())

@app.route('/ninja')
def render_ninja_page():
    return render_template('ninja.html', all_dojos = dojo.Dojo.get_all_dojos())

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    data = {'name': request.form['dojo_name']}
    dojo.Dojo.add_dojo(data)
    return redirect('dojos')

@app.route('/show_dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    return render_template('dojo_show.html', dojo_info = dojo.Dojo.get_one_dojo({'id': dojo_id}), all_ninjas_in_dojo = ninja.Ninja.get_all_ninjas({'id': dojo_id}))

@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    data = {
        'dojo_id': request.form['dojo'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
    }
    ninja.Ninja.add_ninja(data)
    return redirect('/show_dojo/' + request.form['dojo'])