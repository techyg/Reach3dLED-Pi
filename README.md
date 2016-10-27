"# Reach3dLED" 

This is a project for adding a 24 LED NeoPixel for Reach3d printers.

This is currently a Work in Progress!  ALPHA code!

PLEASE CONNECT TO OCTOPRINT BEFORE RUNNING CODE, otherwise you will have an error. 
(This will be fixed in a future version)

General architectural approach:
•Raspberry Pi is running OctoPrint (code relies on OctoPrint API), and connected to RAMPS board via USB
•Raspberry Pi drives NeoPixel using PWM 
•NeoPixel is connected to 5V power supply
•Common ground between Pi, NeoPixel

Notes:
Raspberry Pi is connected from PWM pin 18 to a Logic Shifter, and then to the NeoPixel.
For wiring information, implement per this article from AdaFruit:
https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring

Code:
•Based on the temperature, the NeoPixel will light up. Cold = blue, Hot= red.
•When idle, and while printing the NeoPixel can also be set to colors. Colors can be changed in the code.


You will need to install the several packages for this code to work on your Raspberry Pi. Connect to your Raspberry Pi using SSH (Use Putty on a Windows PC) and perform the steps below.

Step 1: RPI_ws281x Library:
sudo apt-get install build-essential python-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons

Step 2: Install requests library:
sudo apt-get requests

Step 3: Clone the code:

git clone https://github.com/techyg/Reach3dLED-Pi.git

Step 4: Modify the file with your API Key from OctoPrint.

sudo nano RunLED.py

Update the APIKey line with your key. This can be found under the settings tab in OctoPrint. 
Press Control X and answer "Y" to save the file.

Step 5: Ensure that OctoPrint is running. 

Open your browser, connect to OctoPrint, and press "connect". 

Step 6: Run the RunLED.py program

sudo python RunLED.py

Everything should be running now! Check the Reach3D Google Groups if you have any questions.

