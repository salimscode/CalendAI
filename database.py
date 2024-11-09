from pymongo import MongoClient
import datetime
import random

client = MongoClient("mongodb://localhost:27017/")
database = client['calendar_db']

task_collection = database['tasks']
category_collection = database['categories']
schedule_collection = database['schedules']

name = input() # source ai to generate name from description user gives
category_ids = [0]

#Adding a category to the user
def add_category(category_name):
    color = random.choices(range(256), k=3) # randomly generates color as a list [r, g, b]
    category = {(category_id := category_ids[-1] + 1): [category_name, color]}
    category_collection.insert_one(category)
    if category_id == 1:
        category_ids[0] = category_id
    else:
        category_ids.append(category_id)
    print(f'Category {name} was added successfully.')

#Finds the category ID by the name
def findCategoryID(category_name):
    find_category = category_collection.find_one({'name':category_name}) #Returns True or False
    for id in category_ids:
        if category[id][0] == category_name:
            return id

#Adding a task to the calendar
def add_task(name, description, category_name, start_date_time, end_date_time):
    find_category = category_collection.find_one({'name':category_name})
    if find_category == False: #If the category is not found when creating task
        print(f'Category {category_name} not found. It was created successfully.')
        add_category(category_name)
        find_category = category_collection.find_one({'name':category_name})
    task = {
        'name' : name,
        'description' : description,
        'category_name' : category_name,
        'category_id' : findCategoryID(category_name),
        'start' : start_date_time,
        'end' : end_date_time
    }
    task_collection.insert_one(task)
    print(f'Task {name} was added successfully.')
    
#Adding a schedule to the user
def add_schedule(start_time, end_time, start_day, end_day, tasks):
    schedule={}
    start_day=""
    end_day
    total_minutes=(end_time-start_time)
    today=
    