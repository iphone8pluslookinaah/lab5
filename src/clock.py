from hal import hal_lcd as LCD
import time

def main():
    lcd = LCD.lcd()
    lcd.lcd_clear()

    blink = 0

    while True:
        local_time = time.localtime() # get struct_time
        lcd.lcd_display_string(str(time.strftime("%d:%m:%Y")), 2)
        if blink == 0:
            time_string = time.strftime("%H:%M:%S", local_time)
            lcd.lcd_display_string(str(time_string), 1)
            blink = 1
            time.sleep(1)
        else:
            time_string = time.strftime("%H %M %S", local_time)
            lcd.lcd_display_string(str(time_string), 1)
            blink = 0
            time.sleep(1)

if __name__ == "__main__":
    main()