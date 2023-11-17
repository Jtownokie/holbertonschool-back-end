#!/usr/bin/python3
""" API Task 2 - Export to JSON """
import json
import requests
import sys

if __name__ == '__main__':
    r_users = requests.get('https://jsonplaceholder.typicode.com/users')
    r_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/'
                           f'{sys.argv[1]}/todos')

    json_users = r_users.json()
    json_todos = r_todos.json()

    for user in json_users:
        if user['id'] == int(sys.argv[1]):
            user_name = user['username']

    json_dict = {}
    json_dict[f'{sys.argv[1]}'] = []

    for to_do in json_todos:
        json_dict[f'{sys.argv[1]}'].append({"task": to_do['title'],
                                            "completed": to_do['completed'],
                                            "username": user_name})

    with open(f'{sys.argv[1]}.json', 'w') as f:
        json.dump(json_dict, f)
