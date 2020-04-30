#  Zac Capell
# HeavyWater Solutions Front End Engineer Test
# 4/25/2020

import csv
from tempfile import NamedTemporaryFile as Ntf
import shutil
import json


def find_values(document):
    elements_map = csv.DictReader(open('./extractions/data-elements.csv'))
    result = []
    for row in elements_map:
        if str(row['Document Type']) == str(document):
            result.append(row)
    return result


def group_sort(elements):
    result = {}
    temp = {}
    for e in elements:
        text = [int(e['Datapoint Order']), e['Data Elements']]
        if int(e['Group Number']) in list(result):
            result[int(e['Group Number'])].append(text)
        else:
            result[int(e['Group Number'])] = [text]
    for i in result:
        result[i] = sorted(result[i])
    for i in sorted(result):
        temp[i] = result[i]
    return temp


def read(document):
    return group_sort(find_values(document))


def exchange(data_element, new_group=-1, new_order=-1):
    if new_group == -1:
        new_group = data_element['Group Number']
    if new_order == -1:
        new_order = data_element['Datapoint Order']
    temp = Ntf('w', delete=False)
    with open('./extractions/data-elements.csv', 'r') as csvFile, temp:
        reader = csv.DictReader(csvFile)
        writer = csv.DictWriter(temp, reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if row['Document Type'] == data_element['Document Type'] and row['Data Elements'] == data_element['Data Elements']:
                row['Group Number'] = new_group
                row['Datapoint Order'] = new_order
            row = {'Document Type': row['Document Type'], 'Data Elements': row['Data Elements'],
                   'Group Number': row['Group Number'], 'Datapoint Order': row['Datapoint Order']}
            writer.writerow(row)
    shutil.move(temp.name, './extractions/data-elements.csv')
    temp.close()
    csvFile.close()


def exports():
    # field_names = []
    document_map = json.load(open('./documents-file-map.json'))
    with open('./exports/extraction export.csv', 'w') as file:
        writer = csv.writer(file, delimiter=',')
        for k in document_map:
            row = [k]
            x = read(k)
            for group in x:
                for e in x[group]:
                    row.append(e[1])
            writer.writerow(row)
        file.close()


def export_list(document):
    result = read(document)
    with open('./exports/extraction fields export.txt', 'w') as file:
        file.write(document)
        file.write('\n')
        for group in result:
            for i in result[group]:
                file.writelines(i[1])
                file.write('\n')
    file.close()
