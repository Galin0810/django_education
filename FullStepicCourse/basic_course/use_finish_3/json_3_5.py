"""
Вам дано описание наследования классов в формате JSON. Описание представляет из себя массив
JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое
содержит имя класса, и поле parents, которое содержит список имен прямых предков.
"""

import json


def read_input():
    data_json = input()
    data = json.loads(data_json)
    return data


def get_parents(clazz_name, input_data):
    for row in input_data:
        if row["name"] == clazz_name:
            return row["parents"]
    return []


def walk(from_clazz, to_clazz, input_data):
    for parent in get_parents(from_clazz, input_data):
        if parent == to_clazz:
            return True
        else:
            part = walk(parent, to_clazz, input_data)
            if part:
                return part
    return False


def main():
    data = read_input()
    result_dict = {}
    for i in data:
        for j in data:
            a = i["name"]
            b = j["name"]
            if b not in result_dict:
                result_dict[b] = 1
            if a != b and walk(a, b, data):
                result_dict[b] += 1
    result_lst = []
    for key in result_dict:
        result_lst.append({"key": key, "value": result_dict[key]})
    result_lst_sort = sorted(result_lst, key=lambda k: k['key'])
    for i in result_lst_sort:
        print(i["key"], ":", i["value"])


main()
