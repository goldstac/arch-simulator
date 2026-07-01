import subprocess
import time
def bootloader():
    print("GRUB")
print("1: Arch Linux")
choose_boot_option_grub = input("Choose Boot Option : ")
if choose_boot_option_grub == "1":
    print("Loading Linux")
    print("Loading Ramdisk")
    time.sleep(0.3)
    print("#########")
    time.sleep(0.3)
    print("#########")
    time.sleep(1.50)
    print("dev/nvme0n1p6 clean 105000 1100000")
    time.sleep(2)
    print(r"""
              /\
             /  \
            / /\ \
           / /  \ \
          /_/____\_\
         /__________\

========================================
        Arch Linux Simulator
========================================
""")