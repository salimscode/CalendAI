from pymongo import MongoClient
from datetime import datetime
import random

client = MongoClient("mongodb://localhost:27017/")
database = client['calendar_db']

task_collection = database['tasks']
category_collection = database['categories']
schedule_collection = database['schedules']

name = input() # source ai to generate name from description user gives
category_ids = [0]

#Adding a category to the user
def add_category(category_name: str):
    color = random.choices(range(256), k=3) # randomly generates color as a list [r, g, b]
    category = {(category_id := category_ids[-1] + 1): [category_name, color]}
    category_collection.insert_one(category)
    if category_id == 1:
        category_ids[0] = category_id
    else:
        category_ids.append(category_id)
    print(f'category {category_name} was added successfully.')

#Finds the category ID by the name
def findCategoryID(category_name):
    for category in category_collection:
        for id in category:
            if category[id][0] == category_name:
                return id
            
# checks if date and times given are valid
def valid_date_time(lst):
    while lst[0] < 0:
        print('year out of range.')
        lst[0] = int(input("re-enter year: "))
    while lst[1] < 0 or lst[1] > 12:
        print('month was out of range.')
        lst[1] = int(input("re-enter month: "))
    while lst[2] < 0 or lst[2] > 31:
        print('day was out of range.')
        lst[2] = int(input("re-enter day: "))
    while lst[3] < 0 or lst[3] > 24:
        print('hour was out of range.')
        lst[3] = int(input("re-enter hour: "))
    while lst[4] < 0 or lst[4] > 60:
        print('minute was out of range.')
        lst[4] = int(input("re-enter minute: "))
    return datetime(*lst)
    
#Adding a task to the calendar
def add_task(task_name: str, description: str, category_name: str, start_date_time: list, end_date_time: list):
    find_category = category_collection.find_one({'name':category_name})
    if not find_category:
        print(f'category {category_name} not found. it was created successfully.')
        add_category(category_name)
        find_category = category_collection.find_one({'name':category_name})
    task = {
        'name' : task_name,
        'description' : description,
        'category_name' : category_name,
        'category_id' : findCategoryID(category_name),
        'start' : valid_date_time(start_date_time), # 11-09-24 23:00
        'end' : valid_date_time(end_date_time)
    }
    task_collection.insert_one(task)
    print(f'task {task_name} was added successfully.')

add_task('gym', 'hit legs', 'fitness', [2024, 11, 9, 20, 30] , [2024, 11, 9, 22, 30])
tsk = task_collection.find_one({'name':'gym'})
print(tsk)

#Finds events by category
def getEventsByCategory(category_name):
    tasks = task_collection.find({'category': category_name})
    for task in tasks:
        print(f"Title: {task['title']}, Start: {task['start_datetime']}, End: {task['end_datetime']}")

#Lists every category
def listAllCategories():
    categories = category_collection.find()
    for category in categories:
        print(f"ID: {category['_id']}, Name: {category['name']}, Color: {category['color']}")

#Lists every task created
def listAllTasks():
    tasks = task_collection.find()
    for task in tasks:
        print(f"Name: {task['name']}, Description: {task['description']}, Start: {task['start']}, End: {task['end']}")

