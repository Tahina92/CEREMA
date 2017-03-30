#!/usr/bin/python3
# coding: utf-8

"""
Autors: CEREMA/DTerSO/DALETT/ESAD-ZELT/ TAHINJANAHARY Jean Noël
Projet: Capteur Bluetooth open Source et open Hardware
"""

import time, datetime
import threading
import signal
import paho.mqtt.client as paho
import sys, json
import bluetooth
import publisher as pub
 
class Detection(threading.Thread):
 
	def __init__(self, delais,publish):
		threading.Thread.__init__(self)
		# The keep_running is a threading.Event object that
		# indicates whether the thread should be terminated.
		self.keep_running = threading.Event()
		print(delais)
		self.__delais = delais
		self.__publish = publish
		# ... Other thread setup code here ...
 
	def run(self):
		print("Thread # {} started\n".format(self.ident))
		print("Detection code start here")
		while not self.keep_running.is_set():
			# ... Detection code here ...
			nearby_devices = bluetooth.discover_devices(duration=self.__delais, lookup_names=True, flush_cache= True, lookup_class=False)
			if len(nearby_devices) != 0:
				#What time is it please ?
				now = datetime.datetime.today()
				#print(now.year, now.month, now.day, now.hour, now.minute, now.second)
				horodate = [now.year, now.month, now.day, now.hour, now.minute, now.second]
				nearby_devices.insert(0,horodate)
				self.__publish(nearby_devices)
				time.sleep(.5)
			else:
				print("No device detected ...")
				time.sleep(.5)
 
		# ... Clean shutdown code here ...
		print("\nThread # {} stopped\n".format(self.ident))
			
	
	
class ServiceExit(Exception):
	"""
	Custom exception which is used to trigger the clean exit
	of all running threads and the main program.
	"""
	pass
 
 
def service_shutdown(signum, frame):
	print("\nCaught signal {}".format( signum))
	raise ServiceExit

def main():
	# Register the signal handlers
	signal.signal(signal.SIGTERM, service_shutdown)
	signal.signal(signal.SIGINT, service_shutdown)
 
	print("Starting main program")
	print("*********************\n\n")
	print("To Exit Press Ctrl+C")
	print("*********************\n\n")
	# Start the detection threads

	try:
		detection = Detection(2,pub.on_publish)
		detection.start()
 
		# Keep the main thread running, otherwise signals are ignored.
		while True:
			time.sleep(0.5)
 
	except ServiceExit:
		# Terminate the running threads.
		# Set the shutdown flag on each thread to trigger a clean shutdown of each thread.
		detection.keep_running.set()
		# Wait for the threads to close...
		detection.join()
	pub.on_disconnect()
	print('Exiting main program')
 
 
if __name__ == '__main__':
	main()
