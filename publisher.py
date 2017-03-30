#!/usr/bin/python3
# coding: utf-8

"""
Autors: CEREMA/DTerSO/DALETT/ESAD-ZELT/ TAHINJANAHARY Jean Noël
Projet: Capteur Bluetooth open Source et open Hardware
"""

import paho.mqtt.client as paho
import sys, json, time, datetime

		
def on_connect(client, userdata, flags, rc):
	print("Connected  with result code" + str(rc))
	
			
def on_publish (message):
	"""Sending horodate MAC """
	#If message is not empty publish
	
	legth = len(message)
	if legth > 1:
		print("Message received...     {} ".format(message))
		
		now = datetime.datetime.today()
		print(now.year, now.month, now.day, now.hour, now.minute, now.second)
		for i in range(1, legth):
			value = [message[0],message[i]]
			json_value = {}
			json_value['Message'] = str(value)
			mqtts.publish("/id_arc_OSM/value", json.dumps(json_value))
			print("		Message published...     {} ".format(value))
			
def on_disconnect():
	print("Disconnect Publisher")
	mqtts.disconnect()
	print("Done ...\n\n")
		
#Conneted the mqtt client with broker
mqtts = paho.Client()
mqtts.on_connect = on_connect
mqtts.connect("iot.eclipse.org", 1883, 60)



#NB  this code block the sensor
#mqtts.loop_forever()





	
