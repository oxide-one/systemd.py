import os
import time
from random import randint
from colored import fg, bg, attr


res = attr('reset')
iso_color = fg('#dd5892') + attr("bold")
systemd_color = fg('#118111') + bg('#000000')
systemd_version = "239"
curdir = os.getcwd()
reset = attr('reset')
clear = lambda: os.system('clear')

def init():
    global units
    global hooks
    global mounts
    hooks = [line.rstrip('\n') for line in open(curdir + '/hooks')]
    units = [line.rstrip('\n') for line in open(curdir + '/units')]

def early_start():
    print(":: running early hook [udev]")
    print(curdir)
    time.sleep(1)
    print("starting version " + systemd_version)
    print(":: running early hook [initiso_system]")
    time.sleep(0.5)
    for idx, hook in enumerate(hooks):
        print(":: running hook [" + hook +"]")
        if idx == 0:
            print(":: Triggering uevents...")
            time.sleep(0.5)
        elif idx == 4:
            print_mounts()
        time.sleep(0.04)
    print(":: running cleanup hook [udev]")
    print("Welcome to " + iso_color + "okami.dev" + res + "!")

def print_mounts():
    print(":: Mounting '/dev/disk/by-label/rootfs' to '/'")
    time.sleep(0.02)
    print(":: Device '/dev/disk/by-label/rootfs' mounted successfully.")
    time.sleep(0.02)
    print(":: Mounting '/dev/disk/by-label/efipart' to '/boot/efi'")
    time.sleep(0.02)
    print(":: Device '/dev/disk/by-label/efipart' mounted successfully.")
    time.sleep(0.02)
    print(":: Mounting (tmpfs) filesystem, size=32m...")


def systemd_start():
    stop_1 = randint(1,len(units))
    stop_2 = randint(1,len(units))
    for idx, unit in enumerate(units):
        if "[  OK  ]" in unit:
            unit = unit.replace("[  OK  ]","")
            print ( "[  " + systemd_color + "OK" + reset + "  ] " + unit)
        else: 
            print(" " + unit)
        if idx == stop_1 or idx == stop_2:
            time.sleep(1)
        time.sleep(0.002)

def main():
    init()
    clear()
    early_start()
    systemd_start()

if __name__== "__main__":
  main()

