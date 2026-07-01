from login.login import login
from bootloader.grub.grub import bootloader
from application_run import run_application
import os
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
bootloader()
login()
while True:
 main_terminal_shell = input("admin@arch ~ # ")
 if main_terminal_shell == "exit":
  break
 elif main_terminal_shell == "clear":
  if os.name == "nt":
   os.system("cls")
  else:
   os.system("clear")
 elif main_terminal_shell == "whoami":
  with open(os.path.join(script_dir, "files/username.txt"), "r") as username:
   username_list = username.read()
  print(username_list)
 elif main_terminal_shell == "sudo pacman -Syu":
  print("Updating Core Repository ##### 100%") 
  time.sleep(0.5)
  print("Updating Extra Repository ##### 100%")
  time.sleep(0.5)
  print("Starting Full System Upgrade")
 elif main_terminal_shell == "run-app":
   run_app = input("Enter Application Name : ")
   run_application(run_app)
  