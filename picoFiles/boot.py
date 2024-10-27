from usb_midi import disable as mididisable
from usb_cdc import disable as consoledisable
from digitalio import DigitalInOut, Direction, Pull
from storage import disable_usb_drive, remount
from board import GP27, LED
from time import sleep
from mode import configMode
mididisable()
accessButton = DigitalInOut(GP27)
accessButton.direction = Direction.INPUT
accessButton.pull = Pull.UP

# regular mode
# no usb drive if button pressed at boot
# note that the value of the button is inverted (true when not pressed)
if accessButton.value: # button NOT pressed
    if configMode:
        remount("/", readonly=False)
        with open("mode.py", "w") as f:
            f.write("configMode=False")
        remount("/", readonly=True)
        import supervisor
        supervisor.reload()
    disable_usb_drive()
    consoledisable()

# config mode when button pressed
# allows USB drive
else:
    if not configMode:
        remount("/", readonly=False)
        with open("mode.py", "w") as f:
            f.write("configMode=True")
        remount("/", readonly=True)
        import microcontroller
        microcontroller.reset()