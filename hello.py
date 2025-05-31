from gpiozero import Servo
from time import sleep
from sshkeyboard import listen_keyboard

servo_pin= 13
servo = Servo(servo_pin)

servo.value = 1
sleep(2)


def on_press(key):
    print(key)
    if key=='a':
        servo.value=-1
    if key=='b':
        servo.value=0.5
    if key=='s':
        servo.value=0.25
    if key=='d':
        servo.value=1

listen_keyboard(on_press=on_press)



while True:
    pass

# servo.min()
# sleep(2)
# servo.max()
# sleep(2)
# servo.min()
# sleep(2)

