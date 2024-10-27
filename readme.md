# Simple text typer

This is a very simple way to type text using a raspberry pi pico microcontroller and circuitpython

## Setup

1. flash an rp2040 pico with a circuitpython 9 uf2 file
    - latest can be found in this repo in the [firmware folder](https://github.com/mynah22/passwordWriter/tree/main/firmware)
    - hold down the BOOTSEL button on the pico when plugging into PC
    - a USB storage device named `RPI-RP2` will appear, copy the uf2 file to that
    - after it finishes copying, the pico will reboot and a `CIRCUITPY` usb storage device will appear
2. copy files to circuitpython drive
    - the entire contents of the [picoFiles](https://github.com/mynah22/passwordWriter/tree/main/picoFiles) folder must be copied to the pico
3. connect a button from GP27 to ground on the pico
    - this will be the control interface for the device
    - another pin can be used, be sure to edit `boot.py` and `main.py` if you use a different one

## Usage instructions

### Configuration mode

- To enter configuration mode, hold the button connected to gp27 down when plugging it in to PC
- While in configuration mode, the on-board LED will 'breathe', and the `CIRCUITPY` drive will be visible
- Edit the `string.txt` file so that it has the text you want to type (trailing spaces and new lines will be typed)

### Normal mode

- Plug into PC without pressing the GP27 button for normal operation
- LED will not 'breathe'
- `CIRCUITPY` drive will not appear
- press the button to type out the contents of the `string.txt` file
  - LED will blink rapidly when button press is detected
