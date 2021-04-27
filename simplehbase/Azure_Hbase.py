import requests
import json
import pandas as pd

from .utils import base64_to_string

class AzHbaseRestAPI:
    
    def __init__(self):
        self.url = None
        self.username = None
        self.password = None
        self.headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }

    def _checkParametersPresent(self):
        if self.url == None or self.username == None or self.password == None:
            print("Missing Parameters. Use connectionParamaters to set up URL, username and password")
            return False
        else:
            return True


    def connectionParameters(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password
    
    def create_table(self, table_name, columnFamilies):
        if not self._checkParametersPresent():
            return

        query_url = self.url+str(table_name)+'/schema'
        ColumnSchema = []
        for cf in columnFamilies:
            ColumnSchema.append({"name":cf})
        data = {"@name": table_name, "ColumnSchema":ColumnSchema}

        response = requests.put(query_url, headers=self.headers, data=json.dumps(data), auth=(self.username, self.password))
        return response.status_code
    
    def delete_table(self, table_name):
        if not self._checkParametersPresent():
            return

        query_url = self.url+str(table_name)+'/schema'
        response = requests.delete(query_url, headers=self.headers, auth=(self.username, self.password))
        return response.status_code
    
    def get_table_schema(self, table_name):
        if not self._checkParametersPresent():
            return

        query_url = self.url+str(table_name)+'/schema'
        response = requests.get(query_url, headers=self.headers, auth=(self.username, self.password))
        return response.text
    
    def insert_data(self, table_name, data):
        if not self._checkParametersPresent():
            return

        query_url = self.url+str(table_name)+'/false-row-key"'
        response = requests.put(query_url, headers=self.headers, data=json.dumps(data), auth=(self.username, self.password))
        return response.status_code, response.reason
    
    def get_value(self, table_name, row_key, column = None):
        if not self._checkParametersPresent():
            return

        query_url = self.url + str(table_name) + "/" + str(row_key)
        response = requests.get(query_url, headers=self.headers, auth=(self.username, self.password))
        try:
            key = base64_to_string(json.loads(response.text)['Row'][0]['key'])
        except:
            print ('{} does not exist'.format(row_key))
            return
        n = len(json.loads(response.text)['Row'][0]['Cell'])
        df = pd.DataFrame(json.loads(response.text)['Row'][0]['Cell']).drop(columns='timestamp').applymap(base64_to_string).assign(ID = [key]*n).pivot(index='ID', columns='column', values='$')

        if column == None:
            return df
        else:
            try:
                return df[column].values[0]
            except:
                print ("Column {} does not exist for {}.".format(column, row_key))
                return

    def delete_row(self, table_name, row_key):
        if not self._checkParametersPresent():
            return

        query_url = self.url + str(table_name) + "/" + str(row_key)
        response = requests.delete(query_url, headers=self.headers, auth=(self.username, self.password))
        return response.status_code

    def create_scanner(self, table_name):
        if not self._checkParametersPresent():
            return

        query_url = self.url + str(table_name) + "/scanner"

        data = {
            '<Scanner batch="1"/>'
        }
        print(query_url, data)
        response = requests.post(query_url, headers=self.headers, data=json.dumps(data), auth=(self.username, self.password))

        return response.text

    
        
