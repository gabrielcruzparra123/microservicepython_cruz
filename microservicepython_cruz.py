#!/usr/bin/python
import MySQLdb
import json
import requests
from flask import Flask, request 

app = Flask(__name__)

@app.route('/microservicio/busqueda_parametrizada', methods=['GET'])
def microserviceLogic ():

    try:
        
        if request.method =="GET":
 
            searchType = request.args.get('searchType')
            criteria = request.args.get('criteria')
            url =    request.args.get('url')

            if searchType == "PRESE":
                param = {'criteria': criteria}
                r = requests.get(url, param)
            elif searchType == "COLOR":
                param = {'criteria': criteria}
                r = requests.get(url, param)
            elif searchType == "MATER":
                param = {'criteria': criteria}
                r = requests.get(url, param)
            elif searchType == "PROVE":
                param = {'criteria': criteria}
                r = requests.get(url, param)
            elif searchType == "ESPAC":
                param = {'criteria': criteria}
                r = requests.get(url, param)
            elif searchType == "CATEG":
                param = {'criteria': criteria}
                r = requests.get(url, param)
            elif searchType == "SERVI":
                param = {'criteria': criteria}
                r = requests.get(url, param)
            else:
                param = {'criteria': criteria}
                r = requests.get(url, param)       

            
            response = {} 
            if(r.json()!= None):
                response = r.json()

            return  json.dumps(response)


    except IOError as e:
        print ("Error en conexion a url ".url)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5003)


   

