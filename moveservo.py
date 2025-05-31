from gpiozero import Servo
from flask import Flask, render_template, request, redirect
from time import sleep
import time

app=Flask(__name__)

# servo_pin= 13
# servo = Servo(servo_pin)

# servo.value = 1
# sleep(2)
@app.route('/home/', methods=['GET','POST'])
def hello():
    times= input("Please enter the time you want to wake up: ")
    print("Ok we will wake you up at " + times +"!" )

#gets the local time
    local_time_string = time.ctime()
    print("local time: " + local_time_string)

    servo_pin=13
    servo= Servo(servo_pin)
    if times==local_time_string:
        servo.value=-1
    #add a way for the servo to move back and forth so more motion
        #sleep(2)
    else:
        servo.value=1
        #sleep(2)
#next set of tasks:
#servo move back and forth, so loop?
#webpage display??
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)


