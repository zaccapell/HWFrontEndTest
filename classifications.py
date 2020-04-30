# Zac Capell
# HeavyWater Solutions Front End Engineer Test
# 4/24/2020

import csv
import json
from tempfile import NamedTemporaryFile as Ntf
import shutil

customer_map = json.load(open('./customers-file-map.json'))


# function to return all requested client document types from a single client
# parameters are the client name and a list of any number of document types to find
# returns a list of client documents
def find_values(client, documents):
    result = [client]
    path = customer_map[client]
    reader = csv.DictReader(open(path))
    for row in reader:
        if row['Document Type'] in documents:
            result.append(row['Customer Document Type'])
    return result


def read_all(clients, documents):
    result = []
    for client in clients:
        result.append(find_values(client, documents))
    return result


# function to update value in a specific row for a specific column
# parameters are the client and document type to be updated, as well as the new value to use
# does not return anything, but edits the csv
def update(client, doc_type, new_value):
    path = customer_map[client]
    temp = Ntf('w', delete=False)
    field_names = ['Document Type', 'Customer Document Type']
    with open(path, 'r') as csvFile, temp:
        reader = csv.DictReader(csvFile)
        writer = csv.DictWriter(temp, field_names)
        writer.writeheader()
        for row in reader:

            if row['Document Type'] == doc_type:
                row['Customer Document Type'] = new_value
            row = {'Document Type': row['Document Type'], 'Customer Document Type': row['Customer Document Type']}
            writer.writerow(row)
    shutil.move(temp.name, path)
    temp.close()
    csvFile.close()


# exports the list of values for given clients and documents type
# parameters are the the list of clients for the columns and the list of documents for the rows
# does not return, but writes a new csv
def exports(clients, documents):
    field_names = ['Document Type']
    for c in clients:
        field_names.append(c)
    with open('./exports/classifications export.csv', 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(field_names)
        for d in documents:
            row = [d]
            for c in clients:
                row.append(find_values(c, d)[0])
            writer.writerow(row)
        file.close()


# helper to ensure all given client csvs have all fields, even if they're not used
# parameter is the client data to be cleaned
# does not return anything, but edits the csv
def cleaner(client):
    all_fields = json.load(open('./documents-file-map.json'))
    fields = list(all_fields)
    given_fields = []
    path = customer_map[client]
    temp = Ntf('w', delete=False)
    field_names = ['Document Type', 'Customer Document Type']
    with open(path, 'r') as csvFile, temp:
        reader = csv.DictReader(csvFile)
        writer = csv.DictWriter(temp, field_names)
        writer.writeheader()
        for row in reader:
            given_fields.append(row['Document Type'])
            writer.writerow(row)
        for i in fields:
            if i not in given_fields:
                row = {'Document Type': i, 'Customer Document Type': ''}
                writer.writerow(row)
    shutil.move(temp.name, path)
    temp.close()
    csvFile.close()
    all_fields.close()
