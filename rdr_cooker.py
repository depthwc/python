import time
from pynput.keyboard import Controller, Key


keyboard = Controller()

time.sleep(3)
try:
    while True:
        # Press Enter

        keyboard.press(Key.enter) 

        keyboard.release(Key.enter)
        print("Pressed Enter")
        # Wait 6 seconds 
        time.sleep(10)

 


        # Press Space

        keyboard.press(Key.space)
        keyboard.release(Key.space) 
        print("Pressed Space")

        # Wait 2 seconds
        time.sleep(2)
except KeyboardInterrupt:
    print("\nScript stopped by user.") 
     
      