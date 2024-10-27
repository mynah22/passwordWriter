from mode import configMode
if configMode:
    # if usb drive enabled ("config mode"), breathe LED as status indicator
    # and loop forever to prevent main code from running
    import pwmio
    from board import LED
    from time import sleep
    led = pwmio.PWMOut(LED, duty_cycle=0)
    while True:
       # Fade in
       for duty_cycle in range(0, 65536, 256):
           led.duty_cycle = duty_cycle
           sleep(0.01)
       
       # Fade out
       for duty_cycle in range(65535, -1, -256):
           led.duty_cycle = duty_cycle
           sleep(0.01)
else:
    import asyncio
    import usb_hid
    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
    from digitalio import DigitalInOut, Direction, Pull
    from board import GP27, LED
    from time import sleep

    # set up action button and status LED

    actionButton = DigitalInOut(GP27)
    actionButton.direction = Direction.INPUT
    actionButton.pull = Pull.UP

    statusLED=DigitalInOut(LED)
    statusLED.direction=Direction.OUTPUT

    # read contents of file

    textFileName = "string.txt"

    with open(textFileName, mode="r") as f:
        fileContents = f.read()
        
    # init keyboard object

    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    # function definitions
    # using asynchronous (async) functions to emulate multitasking

    # status LED blink function
    async def blink():
        blinkcount=3
        while blinkcount:
            statusLED.value=1
            sleep(.05)
            statusLED.value=0
            sleep(.05)
            blinkcount-=1

    # keyboard typing function
    async def keyboardWrite():
        layout.write(fileContents)

    # combined function emulating multitasking
    async def writeAndBlink():
        await asyncio.gather(
            asyncio.create_task(blink()),
            asyncio.create_task(keyboardWrite())
        )

    # main loop

    while True:
        if not actionButton.value:
            # button pressed, write and blink
            asyncio.run(writeAndBlink())
            while not actionButton.value:
                # sleep for 0.01 second if button not released, then loop and check again
                sleep(.01)
            sleep(1)
