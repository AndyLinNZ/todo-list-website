from app import app, db
from app.models import Task

# db.drop_all clears our database/tables
db.drop_all()
# creates the database for our models
db.create_all()

tasks = [
    'Flutter crash course video',
    'Graphics and Interaction tutorial preparation',
    'Graphics and Interaction lecture week 1 review',
    'Graphics and Interaction lecture week 2 preview'
]

for task in tasks:
    # For each task, create a new task and add it to the database
    new_task = Task(name=task, description='')
    db.session.add(new_task)
db.session.commit()