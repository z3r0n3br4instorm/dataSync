import os
import time
import threading
def run_adb_background():
	print("DEBUG")
	while True:
		os.system("""adb shell "su -c 'content query --uri content://call_log/calls --where \"type=1\"'" > data.zttf""")

def get_input_data():
	while True:
		try:
			caller_data = open("data.zttf","r").read()
			print(caller_data.split()[18].replace("number=","").replace(",",""))
		except:
			print("An error occured !")

if __name__ ==  "__main__":
	print("Zerone Laboratories dataSyncv1.0")
	adb_thread = threading.Thread(target=run_adb_background)
	adb_thread.start()
	get_input_data()
