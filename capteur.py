#!/usr/bin/python3
# coding: utf-8

"""
Autors: CEREMA/DTerSO/DALETT/ESAD-ZELT/ TAHINJANAHARY Jean Noël
Projet: Capteur Bluetooth open Source et open Hardware
"""

from threading import Thread, Condition, Event
import paho.mqtt.client as paho
import sys, json, time 
import bluetooth


class Detection(Thread):
	
	def __init__(self, delais,fonction):
		Thread.__init__(self)
		print(delais)
		self.delais = delais
		self.function = fonction

		self.condition = Condition()
		self.executer = Event()
		self.executer.set()
		
	def run(self):
		self.condition.acquire()
		true = 0		
		while true==0:
			#self.condition.wait(self.delais)
			nearby_devices = bluetooth.discover_devices(duration=self.delais, lookup_names=True, flush_cache= True, lookup_class=False)
			print(nearby_devices)
			self.function(nearby_devices)
		self.condition.release()
		
	def get(self):
		self.condition.acquire()
		self.condition.notify()
		self.condition.release()
		
		
	def stop(self):
		self.executer.clear()
		
		


if __name__ == '__main__' :
	
	def on_connect(client, userdata, flags, rc):
		print("Connected  with result code" + str(rc))
		
	def on_value (value):
		"""Sending horodate MAC """
		json_value = {}
		json_value['value'] = str(value)
		mqtts.publish("/publish/value", json.dumps(json_value))
		
	detection = Detection(1,on_value)
	detection.start()
	
	mqtts = paho.Client()
	mqtts.on_connect = on_connect
	mqtts.connect("iot.eclipse.org", 1883, 60)
	mqtts.loop_forever()





	
