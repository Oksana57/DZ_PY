"""Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV."""

import json
import csv

def json_to_csv(name, res_file):
    with open(name, 'r', encoding='utf-8') as f_json:
        db = json.load(f_json)
    with open(res_file, 'w', encoding='utf-8') as f_res:
        #data = []
        for k, v in db.items():
            #data = []
            for k2, v2 in v.items():
                data=[]
                data.append([k,k2,v2])
                #print(f'{k}, {k2}, {v2}', file=f_res)   
                write_csv = csv.writer(f_res, dialect='excel-tab', delimiter='|')
                write_csv.writerows(data)

if __name__ == '__main__':
    json_to_csv(name='db.json', res_file='db.csv')