"""Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться."""

import json
import os

def cicle_json(name= 'db.json'):
    db = {}
    if os.path.exists(name) and os.path.isfile:
        with open(name, 'r', encoding='utf-8') as f:
            db = json.load(f)
   
    with open(name, 'w', encoding='utf-8') as f:
            
        while True:
            while True:
                try:
                    user_level = int(input('введите уровень от 1 до 7 или букву для выхода: '))
                except:
                    json.dump(db, f)
                    exit()
                else:
                    break
            if not 1<=user_level<=7:
                continue
            if user_level not in db:
                db[user_level] = {}
            while True:
                try:   
                    user_id = int(input("введите идентификатор"))   
                except:
                    print('некорректный ввод')     
                else:
                    flag = False
                    for level in db:
                        for us_id in db[level]:
                            if us_id == user_id:
                                print('идентификатор должен быть уникальныи')
                                flag = True
                                break
                    
                    if flag:
                        continue
                    else:
                        break
            user_name = input("введите имя")  
            db[user_level][user_id] = user_name 


if __name__ == '__main__':
    cicle_json()