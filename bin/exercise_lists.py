#!/usr/bin/env python3.6

users = [{ 'admin': True, 'active': True, 'name': 'Kevin' },
        { 'admin': False, 'active': True, 'name': 'Billy' },
        { 'admin': False, 'active': True, 'name': 'Cassie' },
        { 'admin': False, 'active': False, 'name': 'Joe' },
        { 'admin': False, 'active': True, 'name': 'Nick' },
        { 'admin': True, 'active': True, 'name': 'William'},
        { 'admin': True, 'active': False, 'name': 'Marques'}        ]

for user in users:
    if user['admin'] and user['active']:
        print(f"ACTIVE - (ADMIN) {user['name']}")
    elif user['admin']:
        print(f"(ADMIN) {user['name']}")
    elif user['active']:
        print(f"ACTIVE - {user['name']}")
    else:
        print(user['name'])


