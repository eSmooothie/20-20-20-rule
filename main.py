import os
import time

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('BREAK!!')
    os.system("shutdown -l")

if __name__ == "__main__":
    minute = 20
    min_in_sec = minute * 60

    countdown(min_in_sec)
    
   