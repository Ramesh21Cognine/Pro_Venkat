import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
LED1 = 32
LED2 = 36
switch_input1 = 29
switch_input2 = 40
GPIO.setwarnings(True)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(switch_input2, GPIO.IN, initial=GPIO.HIGH, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_input2, GPIO.IN, initial=GPIO.HIGH, pull_up_down=GPIO.PUD_UP)
while True:
    if(GPIO.input(switch_input1)):
        GPIO.output(LED, GPIO.LOW)
    else:
        GPIO.output(LED, GPIO.HIGH)
    if(GPIO.input(switch_input2)):
        GPIO.output(LED, GPIO.LOW)
    else:
        GPIO.output(LED, GPIO.HIGH)
