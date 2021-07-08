print("Loading")

import threading, itertools, sys, time, os

done = False

os.system('clear')

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
from logs import log
from bookmarks import Bookmark

import os, time

green = "\033[1;32;12m"
red = "\033[0;31;12m"
orange = "\033[0;33;12m"
white = "\033[0;37;12m"
blank = "\033[0;37;12m"

ores = ["korrelite", "reknite", "gellium", "axnit", "narcor", "red narcor", "vexnium", "water"]

files = ["Bookmark/Bookmarks", "CurrentOreAmounts/axnit", "CurrentOreAmounts/gellium", "CurrentOreAmounts/korrelite", "CurrentOreAmounts/narcor", "CurrentOreAmounts/red narcor", "CurrentOreAmounts/reknite", "CurrentOreAmounts/vexnium", "CurrentOreAmounts/water", "PlayerLogs/Kills", "PlayerLogs/Pirates", "Prices/axnit", "Prices/gellium", "Prices/korrelite", "Prices/narcor", "Prices/red narcor", "Prices/reknite", "Prices/vexnium", "Prices/water", "TargetOreAmounts/axnit", "TargetOreAmounts/gellium", "TargetOreAmounts/korrelite", "TargetOreAmounts/narcor", "TargetOreAmounts/red narcor", "TargetOreAmounts/reknite", "TargetOreAmounts/vexnium", "TargetOreAmounts/water"]

missingFiles = []

for fileName in files:
  try:
    file = open(fileName, "r")
    file.read()
    file.close()
  except:
    missingFiles.append(fileName)

if len(missingFiles) != 0:
  done = True
  os.system('clear')
  for file in missingFiles:
    print(f"{red}Fatal: missing {file}")
  exit()

# -- LOADING FINISH --

done = True

clear()


while True:
  print("What would you like to do?")
  mode = input("[type '1' for ores, '2' for player logs or '3' for bookmarks]: ").lower()
  
  clear()

  if mode == "1":
    print("Would you like to add, take away or view your ores?")
    mode = input("[type '1' for add, '2' for take away, '3' for view, '4' to manage targets, or 'r' to reset]: ").lower()

    clear()

    if mode == "1":
      try:
        print("What ore would you like to add to?")
        ore = input("[enter the ore here]: ").lower()

        if ore not in ores:
          clear()
          print(f"{red}Please enter a valid ore!{blank}")
          time.sleep(2)
          clear()
        else:

          clear()

          print("How much would you like to add?")
          amount = str(int(input("[enter the number here]: ")))

          clear()

          OreManager.AddOre(ore,amount)

          print(f"{green}Done!{blank}")
          time.sleep(1)
          clear()
      except:
        clear()
        print(f"{red}Please enter a number!{blank}")
        time.sleep(2)
        clear()
  
    elif mode == "2":
      try:
        print("What ore would you like to take away from?")
        ore = input("[enter the ore here]: ")

        if ore not in ores:
          clear()
          print(f"{red}Please enter a valid ore!{blank}")
          time.sleep(2)
          clear()
        else:
          clear()

          print("How much would you like to take away?")
          amount = str(int(input("[enter the number here]: ")))

          clear()

          OreManager.TakeOre(ore, amount)

          print(f"{green}Done!{blank}")
          time.sleep(1)
          clear()
      except:
        print(f"{red}Please enter a number{blank}")
        time.sleep(2)
        clear()

    elif mode == "3":
      OreManager.VeiwOres()
      input("[press enter to continue]")

      clear()

    elif mode == "4":
      result = OreManager.SetTargets()
      clear()
      
      if result:
        print(f"{green}Done!{blank}")
        time.sleep(1)

      clear()
      1 
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

  elif mode == "2":
    print("What log would you like to manage?")
    mode = input("[enter '1' for player kills, '2' for pirate logs or 'r' for reset]: ").lower()
    clear()

    if mode == "1":
      print("What would you like to do to your kill logs?")
      mode = input("[enter '1' to add a log or '2' to view all logs]: ")
      clear()

      if mode == "1":
        print("What is the username of the player you would like to log?")
        username = input("[enter the username here]: ")
        clear()
        log.kill(username)

        print(f"{green}Done!{blank}")
        time.sleep(1)

        clear()

      elif mode == "2":
        log.veiwKills()
        clear()
    
    elif mode == "2":
      print("What would you like to do to your pirate logs?")
      mode = input("[enter '1' to add a log or '2' to view all logs]: ")
      clear()

      if mode == "1":
        print("What is the username of the player you would like to log?")
        username = input("[enter the username here]: ")
        clear()
        log.pirate(username)
        
        print(f"{green}Done!{blank}")
        time.sleep(1)

        clear()

      elif mode == "2":
        log.veiwPirates()
        clear()

    if mode == "r":
      print("What would you like to reset?")
      mode = input("[enter '1' for Kills or '2' for Pirates]: ").lower()
      clear()

      if mode == "1":
        print("Are you sure you would like to reset your kill logs?")
        mode = input("[Type 'y' for yes and 'n' for no]:")
        clear()

        if mode == "y":
          print("Type 'CONFIRM' to confirm, or type nothing to stop")

          mode = input("[please type here]: ")
          clear()

          if mode == "CONFIRM":
            log.resetKills()
            print(f"{green}Done!{blank}")
            time.sleep(1)
            clear()

          else:
            print(f"{red}Kill logs not reset!{blank}")
            time.sleep(1)
            clear()

        else:
          print(f"{red}Kill logs not reset!{blank}")
          time.sleep(1)
          clear()
          
      elif mode == "2":
        print("Are you sure you would like to reset your pirate logs?")
        mode = input("[Type 'y' for yes and 'n' for no]:")
        clear()

        if mode == "y":
          print("Type 'CONFIRM' to confirm, or type nothing to stop")

          mode = input("[please type here]: ")
          clear()

          if mode == "CONFIRM":
            log.resetPirates()
            print(f"{green}Done!{blank}")
            time.sleep(1)
            clear()

          else:
            print(f"{red}Pirate logs not reset!{blank}")
            time.sleep(1)
            clear()

        else:
          print(f"{red}Pirate logs not reset!{blank}")
          time.sleep(1)
          clear()

  elif mode == "3":
    print("What would you like to do to your bookmarks?")
    mode = input("[enter '1' to add a bookmarks, '2' to remove bookmarks, '3' to view bookmarks or 'r' to reset]: ")

    clear()

    if mode == "1":
      Bookmark.SystemBookmark()

      clear()

      print(f"{green}Done!{blank}")
      time.sleep(1)

      clear()

    elif mode == "2":
      Bookmark.RemoveBookmark()
    
    elif mode == "3":
      Bookmark.VeiwBookmarks()
      clear()

    elif mode == "r":
      print("Are you sure you would like to reset your Bookmarks?")
      mode = input("[Type 'y' for yes and 'n' for no]:")
      clear()

      if mode == "y":
        print("Type 'CONFIRM' to confirm, or type nothing to stop")

        mode = input("[please type here]: ")
        clear()

        if mode == "CONFIRM":
          Bookmark.Reset()
          print(f"{green}Done!{blank}")
          time.sleep(1)
          clear()

        else:
          print(f"{red}Bookmarks not reset!{blank}")
          time.sleep(1)
          clear()

      else:
        print(f"{red}Bookmarks not reset!{blank}")
        time.sleep(1)
        clear()

