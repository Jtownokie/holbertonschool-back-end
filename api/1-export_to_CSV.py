#!/usr/bin/python3
""" API Task 0 - Gather Data From API """
import csv
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

    with open(f'{sys.argv[1]}.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for to_do in json_todos:
            csv_row = []
            if to_do['userId'] == int(sys.argv[1]):
                csv_row.append(to_do['userId'])
                csv_row.append(user_name)
                csv_row.append(to_do['completed'])
                csv_row.append(to_do['title'])
                writer.writerow(csv_row)
