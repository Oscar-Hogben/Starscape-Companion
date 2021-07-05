from Clear import clear

green = "\033[1;32;40m"
red = "\033[0;31;40m"
orange = "\033[0;33;40m"
white = "\033[0;37;40m"
blank = "\033[0;37;12m"

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

    ores = ["korrelite", "reknite", "gellium", "axnit", "narcor", "red narcor", "vexnium", "water"]

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
    ores = ["korrelite", "reknite", "gellium", "axnit", "narcor", "red narcor", "vexnium", "water"]

    for ore in ores:
      print(f"How much {ore} do you need?")
      oreAmount = input("[enter the number here]: ")

      file = open(f"TargetOreAmounts/{ore}", "w")

      file.write(oreAmount)

      file.close()

      clear()