from Clear import clear
import time

green = "\033[1;32;40m"
red = "\033[0;31;40m"
orange = "\033[0;33;40m"
white = "\033[0;37;40m"
blank = "\033[0;37;12m"

ores = ["korrelite", "reknite", "gellium", "axnit", "narcor", "red narcor", "vexnium", "water"]

class OreManager:
  def AddOre(ore, amount):
    fileR = open("CurrentOreAmounts/{}".format(ore), "r")
    currentAmount = fileR.read()
    fileR.close()

    fileW = open("CurrentOreAmounts/{}".format(ore), "w")
    fileW.write(str(int(currentAmount)+int(amount)))
    fileW.close()
  
  def TakeOre(ore, amount):
    fileR = open("CurrentOreAmounts/{}".format(ore), "r")
    currentAmount = fileR.read()
    fileR.close()

    fileW = open("CurrentOreAmounts/{}".format(ore), "w")
    fileW.write(str(int(currentAmount)-int(amount)))
    fileW.close()

  def ResetOres():
    ores = ["korrelite", "reknite", "gellium", "axnit", "narcor", "red narcor", "vexnium", "water"]

    for ore in ores:
      oreFile = open("CurrentOreAmounts/{}".format(ore), "w")
      oreFile.write("0")
      oreFile.close()

  def ResetTargets():
    ores = ["korrelite", "reknite", "gellium", "axnit", "narcor", "red narcor", "vexnium", "water"]

    for ore in ores:
      oreFile = open("TargetOreAmounts/{}".format(ore), "w")
      oreFile.write("0")
      oreFile.close()

  def VeiwOres():

    totalCredits = 0

    for ore in ores:
      CurrentOres = open("CurrentOreAmounts/{}".format(ore), "r")
      oreAmount = str(CurrentOres.read())
      CurrentOres.close()
      
      TargetOres = open("TargetOreAmounts/{}".format(ore))
      oreTarget = str(TargetOres.read())
      TargetOres.close()

      Prices = open("Prices/{}".format(ore), "r")
      orePrice = str(Prices.read())
      Prices.close()

      if int(oreAmount) >= int(oreTarget):
        print(f"{green}{ore}: {oreAmount}/{oreTarget}{red} -- {int(oreAmount) - int(oreTarget)} extra {orange}-- {(int(oreAmount) - int(oreTarget)) * int(orePrice)} C")
      else:
        print(f"{white}{ore}: {oreAmount}/{oreTarget}{red} -- {int(oreTarget) - int(oreAmount)} needed {orange}-- {(int(oreTarget) - int(oreAmount)) * int(orePrice)} C")

      totalCredits += (int(oreAmount) - int(oreTarget)) * int(orePrice)
    
    print()

    if totalCredits < 0:
      print(f"--Credits needed: {-totalCredits}")
    else:
      print(f"--Credits extra: {totalCredits}")

    print(blank)

  def SetTargets():
    failed = False
    ores = ["korrelite", "reknite", "gellium", "axnit", "narcor", "red narcor", "vexnium", "water"]

    for ore in ores:
      try:
        if failed == True:
          return False
          break
        print(f"How much {ore} do you need?")
        oreAmount = str(int(input("[enter the number here]: ")))

        file = open(f"TargetOreAmounts/{ore}", "w")

        file.write(oreAmount)

        file.close()

        clear()
      except:
        for ore in ores:
          file = open(f"TargetOreAmounts/{ore}", "w")
          file.write("0")
          file.close()

        clear()

        print(f"{red}Please enter a number!{blank}")
        time.sleep(2)
        clear()
        failed = True
      
    if failed == False:
      return True
        
