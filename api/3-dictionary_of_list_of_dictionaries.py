#!/usr/bin/python3
""" API Task 3 - Export to JSON """
import json
import requests

if __name__ == '__main__':
    r_users = requests.get('https://jsonplaceholder.typicode.com/users')
    r_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos')

    json_users = r_users.json()
    json_todos = r_todos.json()

    json_dict = {}
    for user in json_users:
        json_dict[f"{user['id']}"] = []
        for to_do in json_todos:
            if user['id'] == to_do['userId']:
                json_dict[f"{user['id']}"].append({"username":
                                                   user['username'],
                                                   "task":
                                                   to_do['title'],
                                                   "completed":
                                                   to_do['completed']})

    with open('todo_all_employees.json', 'w') as f:
        json.dump(json_dict, f)
