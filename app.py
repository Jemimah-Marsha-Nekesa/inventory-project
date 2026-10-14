from tasks import Task 
import json 

tasks=[]

while True:

    #get user input
    user_id = input("Enter Task ID: ")
    user_activity = input("Enter Activity: ")
    user_worker = input("Enter Task worker: ")
    user_scope = input("Enter Task scope: ")
    user_rate = input("Enter Task Rate: ")

    #instances
    S1 = Task(user_id, user_activity,user_worker, user_scope, user_rate)

    #creating dictionary to be saved in the json file 
    new_task = {
        "task_id":S1.task_id,
        "activity":S1.activity_name,
        "worker":S1.worker,
        "scope":S1.scope,
        "rate":S1.rate,
        "work_done":S1.update_work_done(10),
        "amount":S1.compute_amount(),
        "rate":S1.get_status(),
    }

    #opening the json file 
    with open("tasks.json", "r") as doc:
        tasks = json.load(doc)

    #saving the tasks
    with open ("tasks.json", "w") as doc:
        tasks.append(new_task)

        json.dump(tasks, doc, indent=4)

    more_tasks = input ("do you have more tasks? (y/n); ")
    if more_tasks == "y":
        continue
    else:
        break

