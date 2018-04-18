# Python script to read the json file and store in the database
import datetime
import json
from app import db
from app.models import Project

data = json.load(open('projects_data.json'))

for i in range(len(data["projects"])):
	rate = data['projects'][i]['rate']
	distance = data['projects'][i]['distance']
	project_size = data['projects'][i]['project_size']
	completion_date = data['projects'][i]['completion_date']
	completion_date = datetime.datetime.strptime(completion_date,"%Y-%m-%d").date()
	p = Project(distance = distance, rate = rate, project_size = project_size, completion_date = completion_date)
	db.session.add(p)
	db.session.commit()

