
#CREATE DICTIONARY WITH STUDENT DETAILS
students = {
    "s1": {
        "name": "Neha",
        "age": 20,
        "grade": "A"
    },
    "s2": {
        "name": "Priya",
        "age": 18,
        "grade": "B"
    },
    "s3": {
        "name": "Alia",
        "age": 19,
        "grade": "C"
    },
    "s4": {
        "name": "Madhu",
        "age": 20,
        "grade": "A"
    },
    "s5": {
        "name": "Michael",
        "age": 18,
        "grade": "B"
    },
    "s6": {
        "name": "Surekha",
        "age": 19,
        "grade": "C"
    },
    "s7": {
        "name": "Dhanu",
        "age": 20,
        "grade": "A"
    },
    "s8": {
        "name": "lata",
        "age": 18,
        "grade": "B"
    },
    "s9": {
        "name": "Javed",
        "age": 19,
        "grade": "C"
    },
    "s10": {
        "name": "Isha",
        "age": 20,
        "grade": "A"
    }
}

import json

#CREATE METHOD TO CONVERT DICTIONARY INTO JSON FORMAT AND SET IDENT LEVEL 4
def convert_to_json(dict_obj):
    json_data = json.dumps(dict_obj, sort_keys=True, indent=4)
    print(json_data)
    return json_data
convert_to_json(students)




