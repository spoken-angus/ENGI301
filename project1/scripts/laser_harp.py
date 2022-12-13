import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

# Motor functions
def forward():
    global state

    if state == 1:
        GPIO.output("P1_36", GPIO.HIGH)
        GPIO.output("P1_38", GPIO.LOW)
        GPIO.output("P1_40", GPIO.HIGH)
        GPIO.output("P1_33", GPIO.LOW)
        time.sleep(DELAY_MOTOR)
        state = 2
    elif state == 2:
        GPIO.output("P1_36", GPIO.LOW)
        GPIO.output("P1_38", GPIO.HIGH)
        GPIO.output("P1_40", GPIO.HIGH)
        GPIO.output("P1_33", GPIO.LOW)
        time.sleep(DELAY_MOTOR)
        state = 3
    elif state == 3:
        GPIO.output("P1_36", GPIO.LOW)
        GPIO.output("P1_38", GPIO.HIGH)
        GPIO.output("P1_40", GPIO.LOW)
        GPIO.output("P1_33", GPIO.HIGH)
        time.sleep(DELAY_MOTOR)
        state = 4
    elif state == 4:
        GPIO.output("P1_36", GPIO.HIGH)
        GPIO.output("P1_38", GPIO.LOW)
        GPIO.output("P1_40", GPIO.LOW)
        GPIO.output("P1_33", GPIO.HIGH)
        time.sleep(DELAY_MOTOR)
        state = 1

def backward():
    global state

    if state == 4:
        GPIO.output("P1_36", GPIO.HIGH)
        GPIO.output("P1_38", GPIO.LOW)
        GPIO.output("P1_40", GPIO.LOW)
        GPIO.output("P1_33", GPIO.HIGH)
        time.sleep(DELAY_MOTOR)
        state = 3
    elif state == 3:
        GPIO.output("P8_8", GPIO.LOW)
        GPIO.output("P8_10", GPIO.HIGH)
        GPIO.output("P8_12", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)
        time.sleep(DELAY_MOTOR)
        state = 2
    elif state == 2:
        GPIO.output("P1_36", GPIO.LOW)
        GPIO.output("P1_38", GPIO.HIGH)
        GPIO.output("P1_40", GPIO.HIGH)
        GPIO.output("P1_33", GPIO.LOW)
        time.sleep(DELAY_MOTOR)
        state = 1
    elif state == 1:
        GPIO.output("P1_36", GPIO.HIGH)
        GPIO.output("P1_38", GPIO.LOW)
        GPIO.output("P1_40", GPIO.HIGH)
        GPIO.output("P1_33", GPIO.LOW)
        time.sleep(DELAY_MOTOR)
        state = 4

# Constants
DELAY_LASER = 4
DELAY_MOTOR = 6
LASER_STATE = GPIO.LOW
LASER_PIN = "P8_7"
THRESHOLD = 0.5
CMD = 0x90  # MIDI command byte for note on

#Initialize the photoresistor pin
#set up ldr pins
ADC.setup()

# read the ldr values
ldr1 = ADC.read("AIN6")


# Initialize motor pins
GPIO.setup("P1_36", GPIO.OUT)
GPIO.setup("P1_38", GPIO.OUT)
GPIO.setup("P1_40", GPIO.OUT)
GPIO.setup("P1_33", GPIO.OUT)

# Variables
sensor = 0
note5 = 0x37
note4 = 0x34
note3 = 0x32
note2 = 0x30
note1 = 0x2F
state = 1
a = 0
b = 0
c = 0
d = 0
e = 0

# Initialize Laser pin and status LED
GPIO.setup(LASER_PIN, GPIO.OUT)

# Position calibration
GPIO.output(LASER_PIN, GPIO.HIGH)
# The motor goes forward until the sensor receives light
# In that moment, the mirror will be perpendicular to the beam
while sensor < THRESHOLD:
    forward()
    sensor = ldr1.read()
# Once calibrated, the motor goes backward to its initial position
for i in range(8):
    backward()

def noteOn(pitch, velocity):
    # Send MIDI note on message
    print(pitch, velocity)

def run():
    # Set initial note status
    global a, b, c, d, e, ldr1

    while True:
        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.HIGH)
        # Delay for DELAY_LASER
        time.sleep(DELAY_LASER)

        # If the sensor gets a signal
        if ldr1 > THRESHOLD:
            # If there are not any notes playing
            if b+c+d+e == 0:
                # If this note is not being played
                if a == 0:
                    # Play note 1
                    noteOn(note1, 0x7F)
                a = 1

        # If the sensor does not get a signal:
        else:
            # If this note is being played
            if a >= 1:
                # If we have not had any readings for 3 cycles
                a += 1
                if a == 3:
                    # Stop playing note 1.
                    noteOn(note1, 0x00)
                    a = 0

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.LOW)

        forward()

        # The next steps are similar to the previous one. Each one of them corresponds
        # to a different note

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.HIGH)
        # Delay for DELAY_LASER
        time.sleep(DELAY_LASER)

        # If the sensor gets a signal
        if ldr1 > THRESHOLD:
            # If there are not any notes playing
            if a+c+d+e == 0:
                # If this note is not being played
                if b == 0:
                    # Play note 1
                    noteOn(note2, 0x7F)
                b = 1

        # If the sensor does not get a signal:
        else:
            # If this note is being played
            if b >= 1:
                # If we have not had any readings for 3 cycles
                b += 1
                if b == 3:
                    # Stop playing note 1.
                    noteOn(note2, 0x00)
                    b = 0

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.LOW)

        forward()

                # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.HIGH)
        # Delay for DELAY_LASER
        time.sleep(DELAY_LASER)

        # If the sensor gets a signal
        if ldr1 > THRESHOLD:
            # If there are not any notes playing
            if a+b+d+e == 0:
                # If this note is not being played
                if c == 0:
                    # Play note 1
                    noteOn(note3, 0x7F)
                c = 1

        # If the sensor does not get a signal:
        else:
            # If this note is being played
            if c >= 1:
                # If we have not had any readings for 3 cycles
                c += 1
                if c == 3:
                    # Stop playing note 1.
                    noteOn(note3, 0x00)
                    c = 0

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.LOW)

        forward()

                # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.HIGH)
        # Delay for DELAY_LASER
        time.sleep(DELAY_LASER)

        # If the sensor gets a signal
        if ldr1 > THRESHOLD:
            # If there are not any notes playing
            if a+b+c+e == 0:
                # If this note is not being played
                if d == 0:
                    # Play note 1
                    noteOn(note4, 0x7F)
                d = 1

        # If the sensor does not get a signal:
        else:
            # If this note is being played
            if d >= 1:
                # If we have not had any readings for 3 cycles
                d += 1
                if d == 3:
                    # Stop playing note 1.
                    noteOn(note4, 0x00)
                    d = 0

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.LOW)

        forward()

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.HIGH)
        # Delay for DELAY_LASER
        time.sleep(DELAY_LASER)

        # If the sensor gets a signal
        if ldr1 > THRESHOLD:
            # If there are not any notes playing
            if a+b+c+d == 0:
                # If this note is not being played
                if e == 0:
                    # Play note 1
                    noteOn(note5, 0x7F)
                e = 1

        # If the sensor does not get a signal:
        else:
            # If this note is being played
            if e >= 1:
                # If we have not had any readings for 3 cycles
                e += 1
                if e == 3:
                    # Stop playing note 1.
                    noteOn(note5, 0x00)
                    e = 0

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.LOW)

        backward()

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.HIGH)
        # Delay for DELAY_LASER
        time.sleep(DELAY_LASER)

        # If the sensor gets a signal
        if ldr1 > THRESHOLD:
            # If there are not any notes playing
            if a+b+c+e == 0:
                # If this note is not being played
                if d == 0:
                    # Play note 1
                    noteOn(note4, 0x7F)
                d = 1

        # If the sensor does not get a signal:
        else:
            # If this note is being played
            if d >= 1:
                # If we have not had any readings for 3 cycles
                d += 1
                if d == 3:
                    # Stop playing note 1.
                    noteOn(note4, 0x00)
                    d = 0

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.LOW)

        backward()

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.HIGH)
        # Delay for DELAY_LASER
        time.sleep(DELAY_LASER)

        # If the sensor gets a signal
        if ldr1 > THRESHOLD:
            # If there are not any notes playing
            if a+b+d+e == 0:
                # If this note is not being played
                if c == 0:
                    # Play note 1
                    noteOn(note3, 0x7F)
                c = 1

        # If the sensor does not get a signal:
        else:
            # If this note is being played
            if c >= 1:
                # If we have not had any readings for 3 cycles
                c += 1
                if c == 3:
                    # Stop playing note 1.
                    noteOn(note3, 0x00)
                    c = 0

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.LOW)

        backward()

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.HIGH)
        # Delay for DELAY_LASER
        time.sleep(DELAY_LASER)

        # If the sensor gets a signal
        if ldr1 > THRESHOLD:
            # If there are not any notes playing
            if a+c+d+e == 0:
                # If this note is not being played
                if b == 0:
                    # Play note 1
                    noteOn(note2, 0x7F)
                b = 1

        # If the sensor does not get a signal:
        else:
            # If this note is being played
            if b >= 1:
                # If we have not had any readings for 3 cycles
                b += 1
                if b == 3:
                    # Stop playing note 1.
                    noteOn(note2, 0x00)
                    b = 0

        # Set LaserPin to HIGH
        GPIO.output(LASER_PIN, GPIO.LOW)

        backward()

