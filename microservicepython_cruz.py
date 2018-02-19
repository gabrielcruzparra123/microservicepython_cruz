#!/usr/bin/python
#pip install mysqlclient
#pythonmicroservice.c7v0hpe7htge.us-east-2.rds.amazonaws.com
import pika
import MySQLdb
import json
import requests
import sys
import asyncio
import aiohttp
from flask import Flask, request 

class Microservice:

    app = Flask(__name__)

    @app.route('/microservicio/busqueda_parametrizada', methods=['GET'])
    def microserviceLogic ():

        try:
            

            if request.method =="GET":
                if request.get_json()!= None:
                    req_data =request.get_json()
                    searchType = req_data['searchType']
                    criteria = req_data['criteria']
                    url =    req_data['url'] 

                else:

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


        except ConnectionError as e:
            print ("Error en conexión a url ".url)


    @staticmethod
    def queuePublishMessage ():
        try:

            credentials = pika.PlainCredentials('test', 'test')
            parameters = pika.ConnectionParameters('192.168.56.7',5672,'/',credentials)
            connection = pika.BlockingConnection(parameters)

            channel = connection.channel()
            channel.queue_declare(queue='micro_sv')
            channel.basic_publish(exchange='',routing_key='micro_sv',body='Hello World!')
            print(" [x] Sent 'Hello World!'")
            connection.close()


        except IOError as e:
            print ("Error Queue: ".format(e.errno, e.strerror))




    if __name__ == '__main__':
        app.run(host="0.0.0.0", debug=True, port=5000)

#Microservice.microserviceLogic(sys.argv[1], sys.argv[2], sys.argv[3])
#Microservice.get_http(sys.argv[3])
#Microservice.queuePublishMessage()

   

