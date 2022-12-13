# Laser Harp
This is a project for building a frameless laser harp using a PocketBeagle built for ENGI 301 at Rice University

## Table of Contents
1. [Introduction](#introduction)
2. [Project Outline](#project-outline)
3. [Hardware Required](#hardware-required)
4. [Schematic](#schematic)
5. [Running the Python Script](#running-the-python-script)

## Introduction
This project is a frameless laser harp built using a PocketBeagle. The laser harp works by shining a laser beam and using a stepper motor with a mirror to divide it into 5 beams. When one or more of the beams are cut, the light sensor detects it and sends signals to the PocketBeagle, which produces the corresponding notes through a computer or speaker.

## Project Outline
Assemble the hardware according to the schematic provided.
Install the Adafruit_BBIO library on the PocketBeagle.
Connect the PocketBeagle to a computer or keyboard.
Run the Python script on the PocketBeagle to control the laser harp, or configure the script to run automatically by running the following steps.
1. Open the file /etc/rc.local.
2. Add the following line before the exit 0 line: `python /home/debian/laser_harp/scripts/laser_harp.py &`
3. Save the file and reboot the PocketBeagle
Enjoy making music with the laser harp!

## Hardware Required
1. PocketBeagle
2. Laser pointer
3. Stepper motor (we used the PM356-048 model)
4. DC supply (12 V)
5. ULN2003a motor driver
6. Light Detecting Resistor (LDR)
7. Small mirror
8. Breadboard
9. Transistor (we used the 2N3904 model)
10. 1kΩ and 20kΩ resistors
11. Fimo for attaching the mirror to the motor
12. Wires

## Schematic
![Schematic](https://github.com/spoken-angus/ENGI301/blob/main/project1/public/project1_bb.jpg?raw=true)

## Running the Python Script
To control the laser harp, you will need to run the included Python script on the PocketBeagle. To do this, you will need to have the Adafruit_BBIO library installed. To do this, run `sudo pip install Adafruit_BBIO` on the PocketBeagle. Then, connect the hardware as described in the script and run the script using the following command:

`python scripts/laser_harp.py`

The script includes functions for controlling the stepper motor and for detecting when a beam is cut. It also includes a main loop that constantly checks the light sensor and produces notes when a beam is cut.