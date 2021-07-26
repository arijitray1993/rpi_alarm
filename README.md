# WiFi-based Alarm Clock using Raspberry Pi

Code for making a wifi-controlled alarm clock using Raspberry Pi.

## Instructions:


### Schematic

![schematic](https://github.com/arijitray1993/rpi_alarm/blob/main/images/schematic.001.png)

### RaspberryPi Setup

- If you don't have the RaspberryPi OS already installed in your RaspberryPi, follow instructions [here](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html)  

- Make sure the RaspberryPi is connected to WiFi or LAN. 
- Use [VNC](https://www.realvnc.com/en/connect/download/viewer/) (recommended) to `ssh` into `pi@raspberrypi.local` on the local intranet. The default password is usually `raspberry`. 
- Open the terminal and clone this repository `git clone https://github.com/arijitray1993/rpi_alarm.git`.  


### Arduino Set-up
- Use VNC to log into RaspberryPi. The ip is usually `raspberrypi.local` with username as `pi` and password as `raspberry`.
- Download the [Arduino IDE](https://www.arduino.cc/en/software) for 32-bit Linux. 
- Using the Arduino IDE, open `smart_alarm/smart_alarm.ino`. 
- We are using an Arduino Mega 2560. Hence, go to `Tools` and select the correct board (Arduino Mega 2560) and Processor (ATMega 2560). 
- Select the `Port` as `/dev/ttyACM0`. This is important. If you see some other number like `ttyACM1` or something else, go to line 14 in `smart_alarm_rpi.py` and change the serial port name. 
- Click on `Serial Monitor` on the upper right side (magnifying glass symbol) and make sure the baud rate is 9600.  

### Load Arduino Program
- Click on upload on the upper left side in Arduino IDE software. 

### Run the Python Program on the RaspberryPi Terminal
- Run `python3 smart_alarm_rpi.py` on the RaspberryPi terminal. You may have to pip install some dependencies. 

The alarm control server should now be running on the localhost:5000 of the RaspberryPi. 

From any computer or mobile device connected to your WiFi or LAN, open http://raspberrypi.local:5000. You should be able to set and delete alarms. 

