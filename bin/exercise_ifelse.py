#!/usr/bin/env python3.6

user = { 'admin': True, 'active': True, 'name': 'Kevin' }
user = { 'admin': False, 'active': True, 'name': 'Billy' }

if user['admin'] and user['active']:
    print(f"ACTIVE - (ADMIN) {user['name']}")
elif user['admin']:
    print(f"(ADMIN) {user['name']}")
elif user['active']:
    print(f"ACTIVE {user['name']}")
else:
    print(user['name'])


