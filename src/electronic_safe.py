from hal import hal_lcd as LCD
from hal import hal_keypad as kypd
from hal import hal_buzzer as bzr
from threading import Thread

history = []
pin = [0, 0, 0, 0]
kypdcount = 0
wrngcount = 0
lcd = LCD.lcd()
lcd.lcd_clear()
bzr.init()

sfl = "Safe Lock"
pstr0 = "Enter PIN:"
pstr1 = "Enter PIN:*"
pstr2 = "Enter PIN:**"
pstr3 = "Enter PIN:***"
pstr4 = "Enter PIN:****"
lcd.lcd_display_string(sfl, 1)
lcd.lcd_display_string(pstr0, 2)

def lockdown():
    lcd.lcd_clear()
    lcd.lcd_display_string("Safe Disabled", 1)
    exit()

def checkpin():
    global kypdcount
    global wrngcount
    global history
    lcd.lcd_clear()
    if history == pin:
        lcd.lcd_display_string("Safe Unlocked", 1)
        exit()
    else:
        lcd.lcd_display_string("Wrong PIN", 1)
        wrngcount += 1
        bzr.turn_on_with_timer(1)
    history = []
    if wrngcount >= 3:
        lockdown()
    kypdcount = 0

def key_pressed(key):
    history.append(key)
    global kypdcount
    kypdcount += 1
    if kypdcount == 1:
        lcd.lcd_display_string(pstr1, 2)
        print("input:", history)
    elif kypdcount == 2:
        lcd.lcd_display_string(pstr2, 2)
        print("input:", history)
    elif kypdcount == 3:
        lcd.lcd_display_string(pstr3, 2)
        print("input:", history)
    else:
        lcd.lcd_display_string(pstr4, 2)
        print("input:", history)
        checkpin()

def main():
    kypd.init(key_pressed)
    keypad_thread = Thread(target=kypd.get_key)
    keypad_thread.start()

if __name__ == "__main__":
    main()