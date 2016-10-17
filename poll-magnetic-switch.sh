#!/bin/bash 

#set up the LED GPIO pin
sudo echo 17 > /sys/class/gpio/export
sudo echo out > /sys/class/gpio/gpio17/direction

#set up the port expander
sudo i2cset -y 1 0x20 0x00 0xFF

# loop forever
while true
do 
	SWITCH=$(sudo i2cget -y 1 0x20 0x12) 

	if [ $SWITCH == "0x01" ]
	then
		#echo "The door is closed"
		sudo echo 0 > /sys/class/gpio/gpio17/value
	else 
		#echo "The door is open"
		sudo echo 1 > /sys/class/gpio/gpio17/value
	fi
	sleep 0.5
done
