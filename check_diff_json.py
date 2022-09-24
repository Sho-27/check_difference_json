import sys
import json
import difflib
import pprint as pp
import select_json

#Convert json to list.
def convJsonToList(src_json):
    with open(src_json, "r") as f:
        src_dict = json.load(f)
    #Maintain order with [sort_dicts = False]
    src_str = pp.pformat(src_dict, sort_dicts = False)
    src_list = src_str.split("\n")
    return src_list

#Check the difference
def display_diference(src_json1, src_json2):
    #Check differences one line at a time.
    diff_result = difflib.ndiff(convJsonToList(src_json1), convJsonToList(src_json2))
    #Extract and display the difference.
    for line in diff_result:
        print(line)

if __name__ == "__main__":
    presentJson = select_json.presentJson()
    src_json1 = presentJson.select_json()
    src_json2 = presentJson.select_json()
    display_diference(src_json1, src_json2)
