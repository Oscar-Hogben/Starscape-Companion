import threading, itertools, sys, time

done = False

def loading():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=loading)
t.start()

# -- LOADING START --
from OreFunctions import OreManager
from Clear import clear

import os, time

green = "\033[1;32;12m"
red = "\033[0;31;12m"
orange = "\033[0;33;12m"
white = "\033[0;37;12m"
blank = "\033[0;37;12m"

# -- LOADING FINISH --

done = True

clear()


while True:
  print("What would you like to do?")
  mode = input("[type '1' for ores]: ").lower()
  
  clear()

  if mode == "1":
    print("Would you like to add, take away or veiw your ores?")
    mode = input("[type '1' for add, '2' for take away, '3' for veiw, '4' to manage targets, or 'r' to reset]: ").lower()

    clear()

    if mode == "1":
      print("What ore would you like to add to?")
      ore = input("[enter the ore here]: ").lower()

      clear()

      print("How much would you like to add?")
      amount = input("[enter the number here]: ")

      clear()

      OreManager.AddOre(ore,amount)

      print(f"{green}Done!{blank}")
      time.sleep(1)
      clear()
  
    elif mode == "2":
      print("What ore would you like to take away from?")
      ore = input("[enter the ore here]: ")

      clear()

      print("How much would you like to take away?")
      amount = input("[enter the number here]: ")

      clear()

      OreManager.TakeOre(ore, amount)

      print(f"{green}Done!{blank}")
      time.sleep(1)
      clear()
    
    elif mode == "3":
      OreManager.VeiwOres()
      input("[press enter to continue]")

      clear()

    elif mode == "4":
      OreManager.SetTargets()
      clear()
      
      print(f"{green}Done!{blank}")

      time.sleep(1)

      clear()
      
    elif mode == "r":
      print("Would you like to reset ore amounts or target ore amounts?")
      mode = input("[enter '1' for current ores or '2' for target ores]: ")

      clear()

      if mode == "1":

        print("Are you sure?")
        answer = input("[enter 'y' for yes or 'n' for no]: ").lower()
      
        if answer == "y":
          clear()
          OreManager.ResetOres()
          print(f"{green}Ores reset!{blank}")
          time.sleep(2)
          clear()
        
        else:
          clear()
          print(f"{red}Ores not reset.{blank}")
          time.sleep(2)
          clear()

      elif mode == "2":
          
        print("Are you sure?")
        answer = input("[enter 'y' for yes or 'n' for no]: ").lower()
    
        if answer == "y":
          clear()
          OreManager.ResetTargets()
          print(f"{green}Targets reset!{blank}")
          time.sleep(2)
          clear()
          
        else:
          clear()
          print(f"{red}Targets not reset.{blank}")
          time.sleep(2)
          clear()
      
      else:
        clear()
        print(f"{red}That is not an option!{blank}")
        time.sleep(1)
        clear()

    else:
      clear()
      print(f"{red}That is not an option!{blank}")
      time.sleep(1)
      clear()
