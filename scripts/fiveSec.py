#!/usr/bin/env python3
from datetime import datetime 
import time

def main():
    pause = 5
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S") 
    print("Current Time =", current_time)
    time.sleep(pause)

if __name__ == "__main__":
    while(1):
        main()