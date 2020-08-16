# utility.py
import sys
import json
import csv


class FileUtility:
    utility_name:str = 'B-cal file management utility'

    def __init__(self, *args, **kwargs):
        if args:
            if len(args)>1:
                self.name = args[0]
                self.file = args[1]
                print(self.__dict__)
            elif len(args) == 1:
                self.name = args[0] 
                print(self.name, 'Initiliazsed...')    

    def _json_to_csv(self, file:str, obj:dict):
        keys = [*obj]
        items = [obj[key] for key in keys]
        print(keys)
        print(items)
        with open(file, 'w') as outfile:
            writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([*obj])
            writer.writerow(items)
        return f"{file} Saved."  


    def save_csv(self, file:str=None, data:dict=None):
        ''' This Utility creates and saves a .csv file in the application base directory.
            parameters are:
                file = a String of the name of the file with .csv ending,
                path = a String id of where to save the file defaults to the application base directory,
                data = a dictionary object of the data be saved in the file,
            If a filename is not provided the data payload is scanned for an id key which is used 
            as the file identifier if an id key is not present the first item key is used.
            USAGE

                util = FileUtility() or 
                util = FileUtility('CSV file Handler') # for utility logs
                util.save_csv(data=payload) # without file and path parameter
                util.save_csv(file='todo.json', data=payload) # without path parameter
                util.save_csv(file='todo.json', path='Documents/projects', data=payload) 
        '''

        if file and data:
            try:
                if len(data) > 0:
                    self._json_to_csv(file=file, obj=data)
            except Exception as e:
                return e
        try:
            # if user did'nt supply a filename use the id key of the data
            if len(data) > 0 and 'id' in data:
                file = f"{data['id']}.csv"
                self._json_to_csv(file=file, obj=data)                
        except Exception as e:
            return e
        try:
            # if user did'nt supply a filename and data does not have an id key use the first item key of data
            if len(data) > 0:
                keys = [*data]
                file = f"{keys[0]}.csv"
                self._json_to_csv(file=file, obj=data)               
        except Exception as e:
            return e
        return
    

    def save_json(self, file:str=None, path:str=None, data:dict=None):
        ''' This Utility creates and saves a .json file in the application base directory.
            parameters are:
                file = a String of the name of the file with .json ending,
                path = a String id of where to save the file defaults to the application base directory,
                data = a dictionary object of the data be saved in the file,
            If a filename is not provided the data payload is scanned for an id key which is used 
            as the file identifier if an id key is not present the first item key is used.
            USAGE

                util = FileUtility() or 
                util = FileUtility('Json file Handler') # for utility logs
                util.save_json(data=payload) # without file and path parameter
                util.save_json(file='todo.json', data=payload) # without path parameter
                util.save_json(file='todo.json', path='Documents/projects', data=payload) 
        '''

        if file and data:
            try:
                if len(data) > 0:
                    with open(file, 'w') as outfile:
                        json.dump(data, outfile)
                    return f"{file} Saved."                
            except Exception as e:
                return e
        try:
            # if user did'nt supply a filename use the id key of the data
            if len(data) > 0 and 'id' in data:
                file = f"{data['id']}.json"
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
                return f"{file} Saved."                
        except Exception as e:
            return e
        try:
            # if user did'nt supply a filename and data does not have an id key use the first item key of data
            if len(data) > 0:
                keys = [*data]
                file = f"{keys[0]}.json"
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
                return f"{file} Saved."                
        except Exception as e:
            return e

        
        return
