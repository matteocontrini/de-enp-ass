#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version 0.1.1

# Copyright © 2016 Andreas Thilander <andreasthilander@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.

import re, sys, os, csv


def get_item_part(item, part):
    """Returns a specific part of the item, like 'password'"""
    try:
        return re.findall('{} : (.*?)\n'.format(part), '{}\n'.format(item),
                          re.IGNORECASE)[0]
    except IndexError:
        return ''


def get_item_notes(notes):
    """Returns everything in the item that does not have a 'label'
        (like 'password' or 'username')
    """
    #notes = '{}\n'.format('\n'.join(notes.strip().split('\n')[1:]))
    for l in ['title', 'password', 'username', 'nome utente', 'email', 'url']:
       notes = re.sub('{} : (.*?)(?:\n|$)'.format(l), '', notes, flags=re.I)
    
    return notes.strip()


def to_password_item(item):
    """Returns a dict version of an item"""
    out = {
        'title': get_item_part(item, 'title'),
        'password': get_item_part(item, 'password'),
        'username': get_item_part(item, 'username') or get_item_part(item, 'nome utente'),
        'email': get_item_part(item, 'email'),
        'url': get_item_part(item, 'url'),
        'notes': get_item_notes(item)
    }
    
    if out['username'] == '' and out['email'] != '':
        out['username'] = out['email']
        out['email'] = ''
    
    return out


def write_csv_file(path, passwords, fieldnames):
    with open(path, 'w') as file:
        file.truncate()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerows(passwords)
        file.close()


def main(file_path):
    """Do all the things"""
    with open(file_path, 'r') as enpass_file:
        file = enpass_file.read().strip()
        items = file.split('\n\n\n')
        passwords = [to_password_item(item) for item in items]

        print('Found {} items:'.format(len(passwords)))

        file_name = os.path.splitext(file_path)[0]

        logins_path = '{}-logins.csv'.format(file_name)
        
        write_csv_file(logins_path, passwords, ['title', 'url', 'username', 'password',
                                             'notes', 'email'])
        print('conversion complete')
        enpass_file.close()


if __name__ == '__main__':
    main(sys.argv[1])
