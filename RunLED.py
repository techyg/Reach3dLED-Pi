# 
#
# Reach3D NeoPixel 
# 
# Cycles and animates your NeoPixel LED's based on temperature
#
# Author: Greg Huber

import os
import requests
import logging, sys
import json
import neopixel

execfile('./NeoPixelFunctions.py')
from pprint import pprint  #used for debugging json response

#Define your printer variables. Change your API key based on OctoPrint settings.
OctoPiURL = "http://127.0.0.1/api/printer"
APIKey = '13D5342F1B5C4C00AC6FF1A3B08B638F'

#Define the delay between checking printer status (in seconds). Recommend between 3 and 10
WaitTime = 3

#Define your LED Settings. Don't change if you are using a 24 pin NeoPixel Ring
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


#functions

def SetPrinting():
	rainbowCycle(strip)


def SetTemp(strip, temp):

	if temp < 30:
		colorWipe(strip, Color(0, 0, 64))  # Blue wipe
	elif temp > 30 and temp < 100:
		colorWipe(strip, Color(0, 32, 0))  # Green
	elif temp > 100 and temp < 150:
		colorWipe(strip, Color(64, 64, 0)) # Dark Green
	elif temp > 150 and temp < 200:
		colorWipe(strip, Color(64, 0, 0)) # Yellow
	elif temp > 200:
		colorWipe(strip, Color(255, 255, 255)) # Bright White

#MAIN program loop

if __name__ == '__main__':

#initialize the NeoPixel
       # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        # Intialize the library (must be called once before other functions).
        strip.begin()
	Printing  = "False"
	
	print ('Press Ctrl-C to quit.')
	while True:	
		response = requests.get(OctoPiURL,
        	                 headers={'X-Api-Key': APIKey})
		data = response.json()		
		
		SetTemp(strip, int(data["temperature"]["tool0"]["actual"]))

		if not Printing == data["state"]["flags"]["printing"]:
			SetPrinting()
			Printing = data["state"]["flags"]["printing"]
		
		time.sleep(WaitTime)
#debug
		pprint(data)
		print data["temperature"]["tool0"]["actual"]
#end debug
		
	
	
