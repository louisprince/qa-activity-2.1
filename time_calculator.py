#!/bin/python3

import subprocess
import time

first_time = input("Please enter a time in the format HH:mm (24 hour format): ")
second_time = input("Please enter a time in the format HH:mm (24 hour format): ")

while True:
    subprocess.run('clear', shell=True)
    print("""Time Calculator\n
    1- Add 2 times
    2- Find the difference between 2 times
    3- Convert to Hours
    4- Convert to Minutes
    5- Convert Minutes to Time
    6- Convert Hours to Time
    7- Convert Days to Time
    8- Exit\n""")

    chosen_option = input("Enter an option: ")
    match chosen_option:
        case 1:
            total = first_time + second_time
            print(f"The 2 times added together is: {total}")
            time.sleep(5)


