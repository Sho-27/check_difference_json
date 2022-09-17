import os
import sys
import glob

class presentJson:
    def __init__(self):
        pass

    def collectJson(self):
        jsonList = glob.glob("*.json")
        if len(jsonList) < 1:
            print("Json file not found...¥n" + 
                    "Finish processing...")
            sys.exit()
        return jsonList

    def serviceJson(self, jsonList):
        json_service = {}
        for No in range(len(jsonList)):
            json_service_single = {No : jsonList[No]}
            json_service.update(json_service_single)
        return json_service

    def select_json(self):
        jsonList = self.collectJson()
        json_service = self.serviceJson(jsonList)
        
        while True:
            for No, json in json_service.items():
                print(f"No.{No} : {json}")            
            selectNo = input("Please enter number... : ")
            type_check_res = self.type_check(selectNo)
            if type_check_res == True:
                selectNo = int(selectNo)
                if selectNo >= len(json_service):
                    print("Not a normal value.Please select again...")
                else:
                    print(f"Accept with this {selectNo}")
                    break

        return json_service[selectNo]
    
    def type_check(self, type_info):
        try:
            int(type_info)
        except ValueError as e:
            print(f"{e} / Please enter again...")
            return False
        except TypeError as e:
            print(f"{e} / Please enter again...")
            return False
        return True
