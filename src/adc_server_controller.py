from hal import hal_adc as adc
from hal import hal_servo as servo
import time
import math

def main():
    adc.init()
    servo.init()
    while True:
        temp = (adc.get_adc_value(1) / (341 / 60))
        servo.set_servo_position(temp)
        time.sleep(0.1)

if __name__ == "__main__":
    main()