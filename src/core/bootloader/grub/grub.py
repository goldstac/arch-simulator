import subprocess
import time
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
    time.sleep(0.3)
    splash_run = subprocess.run("cd .. && go run grub-dependencies/bootloader_splash.go",shell=True, capture_output=True,text=True)
    print(splash_run.stdout)
    print(splash_run.stderr)

    