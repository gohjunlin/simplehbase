import requests
import json
import base64

class AzHbaseRestAPI:
    
    def __init__(self):
        self.url = None
        self.username = None
        self.password = None
        self.headers = headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
    
    def connectionParameters(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password
    
    def create_table(self, table_name, columnFamilies):
        if self.url == None or self.username == None or self.password == None:
            print("Missing Parameters. Use connectionParamaters to set up URL, username and password")
            return
        
        else:
            query_url = self.url+str(table_name)+'/schema'
            ColumnSchema = []
            for cf in columnFamilies:
                ColumnSchema.append({"name":cf})
            data = {"@name": table_name, "ColumnSchema":ColumnSchema}


            response = requests.put(query_url, headers=self.headers, data=json.dumps(data), auth=(self.username, self.password))
            return response.status_code
    
    def delete_table(self, table_name):
        if self.url == None or self.username == None or self.password == None:
            print("Missing Parameters. Use connectionParamaters to set up URL, username and password")
            return
        
        else:
            query_url = self.url+str(table_name)+'/schema'
            response = requests.delete(query_url, headers=self.headers, auth=(self.username, self.password))
            return response.status_code
    
    def get_table_schema(self, table_name):
        if self.url == None or self.username == None or self.password == None:
            print("Missing Parameters. Use connectionParamaters to set up URL, username and password")
            return
        
        else:
            query_url = self.url+str(table_name)+'/schema'
            response = requests.get(query_url, headers=self.headers, auth=(self.username, self.password))
            return response.text
    
    def insert_data(self, table_name, data):
        if self.url == None or self.username == None or self.password == None:
            print("Missing Parameters. Use connectionParamaters to set up URL, username and password")
            return
        
        else:
            query_url = self.url+str(table_name)+'/false-row-key"'
            response = requests.put(query_url, headers=self.headers, data=json.dumps(data), auth=(self.username, self.password))
            return response.status_code
    
    def get_value(self, table_name, row_key, column = None):
        if self.url == None or self.username == None or self.password == None:
            print("Missing Parameters. Use connectionParamaters to set up URL, username and password")
            return
        if column == None:
            query_url = self.url+str(table_name)+"/"+str(row_key)
            response = requests.get(query_url, headers=self.headers, auth=(self.username, self.password))
            return response.text
        else:
            pass
    
        