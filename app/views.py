from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Project, Order
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/view', methods = ['GET','POST'])
def view():
	projects = []
	ordered_by = " "
	if request.method == "POST":
		ordered_by = request.form['orderby']
		o = Order.query.filter_by(col_name = ordered_by).first() # If the table is empty, prompt the user to create the priority order
		if o is None:
			flash ("No priority order has been defined, please define an order before filtering")
			return redirect(url_for('add'))
		projects = Project.query.filter_by().order_by(o.col_name,o.priority_2,o.priority_3,o.priority_4).all() # Sort by the required order
	return render_template("view.html", projects = projects, title = ordered_by)

@app.route('/add', methods = ['GET','POST'])
def add():
	distance = []
	project_size = []
	completion_date = []
	rate =[]
	try:
		if request.method == "POST":
			db.session.query(Order).delete() # Remove the previously existing order from the db
			db.session.commit()
			o = Order(col_name = "distance", priority_2 = request.form['distancep2'],priority_3 = request.form['distancep3'],priority_4 = request.form['distancep4'])
			db.session.add(o)
			db.session.commit()
			o = Order(col_name = "rate", priority_2 = request.form['ratep2'],priority_3 = request.form['ratep3'],priority_4 = request.form['ratep4'])
			db.session.add(o)
			db.session.commit()
			o = Order(col_name = "completion_date", priority_2 = request.form['completion_datep2'],priority_3 = request.form['completion_datep3'],priority_4 = request.form['completion_datep4'])
			db.session.add(o)
			db.session.commit()
			o = Order(col_name = "project_size", priority_2 = request.form['project_sizep2'],priority_3 = request.form['project_sizep3'],priority_4 = request.form['project_sizep4'])
			db.session.add(o)
			db.session.commit() # Store the priority order in the db
			flash("Updated Successfully")
			return redirect(url_for('index'))
		else:
			o = Order.query.filter_by().all()
			distance.append(o[0].priority_2)
			distance.append(o[0].priority_3)
			distance.append(o[0].priority_4)

			rate.append(o[1].priority_2)
			rate.append(o[1].priority_3)
			rate.append(o[1].priority_4)

			completion_date.append(o[2].priority_2)
			completion_date.append(o[2].priority_3)
			completion_date.append(o[2].priority_4)

			project_size.append(o[3].priority_2)
			project_size.append(o[3].priority_3)
			project_size.append(o[3].priority_4)

	except:
		pass
	return render_template("add.html", distance = distance, project_size= project_size, rate = rate, completion_date =completion_date)
# datetime.datetime.strptime("2017-09-28","%Y-%m-%y").date()
# data = json.load(open('projects.json'))
# data["projects"][0]['rate']
