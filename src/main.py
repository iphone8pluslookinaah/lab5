from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_led as led
import led_control

#Empty list to store sequence of keypad presses
password = []

lcd = LCD.lcd()
lcd.lcd_clear()

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    password.append(key)
    if key == 1:
        lcd.lcd_clear()
        lcd.lcd_display_string("LED control", 1)
        lcd.lcd_display_string("blink LED", 2)
        led_control.led_control_init()
    elif key == 0:
        lcd.lcd_clear()
        lcd.lcd_display_string("LED control", 1)
        lcd.lcd_display_string("off LED", 2)
        led_control.off()
    else:
        print("invalid key")
    print(password)


def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Display something on LCD
    lcd.lcd_display_string("LED control", 1)
    lcd.lcd_display_string("0:off 1:blink", 2)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()


# Main entry point
if __name__ == "__main__":
    main()
