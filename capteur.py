#! /usr/bin/env python3
# coding: utf-8

from threading import Thread, Condition, Event
import paho.mqtt.client as paho
from random import *
import sys, json, time 


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
			self.condition.wait(self.delais)
			self.function("Horodate, MAC")
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
		"""Sending MAC horodate"""
		json_value = {}
		json_value['value'] = str(value)
		mqtts.publish("/publish/value", json.dumps(json_value))
		print("envoyer")

	detection = Detection(2,on_value)
	detection.start()
	
	mqtts = paho.Client()
	mqtts.on_connect = on_connect
	mqtts.connect("iot.eclipse.org", 1883, 60)
	mqtts.loop_forever()





	
