import os, json, csv
from src.settings import RESOURCES_DIRECTORY
from random import choice


def get_resource_file(file_name):
    path = os.path.join(RESOURCES_DIRECTORY, file_name)
    with open(path) as file:
        data = json.load(file)
    return data

def random_userAgent(software=None):
    userAgents = get_resource_file('UserAgents.json')
    if software:
        userAgents_list = userAgents[software]
    else:
        userAgents_list = list()
        for userAgent in userAgents.values():
            userAgents_list += userAgent
    return choice(userAgents_list)

"""

def to_csv_file(item, file_name='default.csv'):
    path = os.path.join(OUTPUT_DIRECTORY, file_name)
    item = dict(item)
    with open(path, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=item.keys())
        if os.stat(path).st_size == 0:
            writer.writeheader()
        writer.writerow(item)

def remove_file(file_name='default.csv'):
    filePath = os.path.join(OUTPUT_DIRECTORY, file_name)
    if os.path.exists(filePath):
        os.remove(filePath)
        
"""