#!/usr/bin/python3
""" API Task 0 - Gather Data From API """
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
            emp_name = user['name']

    num_tasks = 0
    num_completed = 0
    completed_tasks = []
    for to_do in json_todos:
        if to_do['userId'] == int(sys.argv[1]):
            num_tasks += 1
            if to_do['completed'] is True:
                num_completed += 1
                completed_tasks.append(to_do['title'])

    print(f"Employee {emp_name} is done with "
          f"tasks({num_completed}/{num_tasks}):")
    for title in completed_tasks:
        print(f"\t {title}")
