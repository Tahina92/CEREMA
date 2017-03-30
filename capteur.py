#!/usr/bin/python3
# coding: utf-8

"""
Autors: CEREMA/DTerSO/DALETT/ESAD-ZELT/ TAHINJANAHARY Jean Noël
Projet: Capteur Bluetooth open Source et open Hardware
"""

from threading import Thread, Condition, Event
import paho.mqtt.client as paho
import sys, json, time 
import bluetooth, signal


class Detection(Thread):
	
	def __init__(self, delais,publish):
		Thread.__init__(self)
		print(delais)
		self.__delais = delais
		self.__publish = publish

		self.__condition = Condition()
		self.__keep_running = Event()
		self.__keep_running.set()
		
	def run(self):
		self.__condition.acquire()
<<<<<<< HEAD
		self.__keep_running.isSet
		while self.__keep_running.isSet:
			nearby_devices = bluetooth.discover_devices(duration=self.__delais, lookup_names=True, flush_cache= True, lookup_class=False)
			print(nearby_devices)
			self.__publish(nearby_devices)
		self.__condition.release()
	def get(self):
		self.__condition.acquire()
		self.__condition.notify()
		self.__condition.release()		
		
	def stop(self):
		self.__keep_running.clear()
		self.get()
		print("Exit")
	
=======
		while self.__keep_running.isSet:
			nearby_devices = bluetooth.discover_devices(duration=self.delais, lookup_names=True, flush_cache= True, lookup_class=False)
			print(nearby_devices)
			self.__publish(nearby_devices)
		self.__condition.release()
		
		
	def stop(self):
		self.__keep_running.clear()
		break
		
		


if __name__ == '__main__' :
	
	def on_connect(client, userdata, flags, rc):
		print("Connected  with result code" + str(rc))
		
	def on_value (message):
		"""Sending horodate MAC """
		json_value = {}
		json_value['Message'] = str(message)
		mqtts.publish("/id_arc_OSM/value", json.dumps(json_value))
	
<<<<<<< HEAD
	def deconnection(signal, frame):
		print("Exit")
		mqtts.disconnect()
		detection.stop()
		print("Exit")
		
	detection = Detection(1,on_value)
	detection.start()
	signal.signal(signal.SIGINT, deconnection)  # Ctrl-c
=======
	def stop_handler(signal, frame):
		detection.stop()
		
	detection = Detection(1,on_value)
	detection.start()
	signal.signal(signal.SIGINT, stop_handler)  # Ctrl-c
>>>>>>> 757cb168ccaee32f2095e12ee951b512573f22d8
	
	#Mise en connexion avec le serveur
	mqtts = paho.Client()
	mqtts.on_connect = on_connect
	mqtts.connect("iot.eclipse.org", 1883, 60)
	mqtts.loop_forever()





	
