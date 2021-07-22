import time
import datetime as dt
from datetime import datetime
from flask import Flask, request, send_from_directory, jsonify

import serial
import RPi.GPIO as GPIO
import time

import requests, json

import threading

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

app = Flask(__name__)

class Alarm:
    
    def __init__(self):
        self.al_state = True
        self.alarm_set = False
        self.alarm_time = None
    
    def alarm_on(self, alarm_time):
        self.alarm_time = alarm_time
        self.al_state = True
        self.alarm_set = True
        while(self.al_state):
            now_time= datetime.now()
            print(now_time, alarm_time)
            print(alarm_time - now_time)
            if (alarm_time - now_time)<dt.timedelta(seconds=30):
                print("setting alarm")
                ser.flushInput()        
                ser.write("al_on".encode('UTF-8'))
                break
            
            time.sleep(5)
        
                
        
    def alarm_off(self):
        self.al_state = False
        ser.flushInput()        
        ser.write("al_off".encode('UTF-8'))
        self.alarm_set = False
        
alarm = Alarm()
            

@app.route('/')
def initpage():
    
    return send_from_directory('./templates/','index.html')
    

@app.route('/set_alarm', methods = ['GET', 'POST'])
def set_alarm():
    alarm_time = None
    
    if request.method=="POST":
        print("requesting alarm set")
        alarm_hour = request.form["hour"]
        alarm_minute = request.form["minute"]
        print(alarm_hour, alarm_minute)
        now_time = datetime.now()
        
        alarm_time = datetime(now_time.year, now_time.month, 
                                        now_time.day, int(alarm_hour), int(alarm_minute))
                                        
        if now_time>alarm_time:
            alarm_time = datetime(now_time.year, now_time.month, 
                                        now_time.day+1, int(alarm_hour), int(alarm_minute))
        
        al_command = threading.Thread(target=alarm.alarm_on, args=(alarm_time,), daemon=True)
        
        al_command.start()
        
    return "OK"
        
@app.route('/stop_alarm', methods = ['GET', 'POST'])
def stop_alarm():
    alarm.alarm_off()
    
    return "OK"

@app.route('/get_status', methods = ['GET', 'POST'])
def get_status():
    if request.method=="POST":
        if alarm.alarm_set:
            alarm_time_hour = alarm.alarm_time.hour
            alarm_time_min = alarm.alarm_time.minute
            status_text = "Alarm Set at "+str(alarm_time_hour)+":"+\
                            str(alarm_time_min)+" Eastern Standard Time"
            return jsonify({'alarm_status':status_text})
        else:
            return jsonify({'alarm_status':"No Alarm Set"})


if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0')

