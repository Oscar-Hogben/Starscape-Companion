
green = "\033[1;32;40m"
red = "\033[0;31;40m"
orange = "\033[0;33;40m"
white = "\033[0;37;40m"
blank = "\033[0;37;12m"

class log:
  def kill(username):
    file = open("PlayerLogs/Kills", "r")
    read = file.read()
    file.close

    file = open("PlayerLogs/Kills", "w")
    file.write(f"{read}\n{username}")
    file.close()

  def veiwKills():
    file = open("PlayerLogs/Kills", "r")
    print(f"{red}Player Kills:")
    print(f"{file.read()}{blank}")
    file.close()
    print()
    input("[press enter to continue]")

  def pirate(username):
    file = open("PlayerLogs/Pirates", "r")
    read = file.read()
    file.close

    file = open("PlayerLogs/Pirates", "w")
    file.write(f"{read}\n{username}")
    file.close()

  def veiwPirates():
    file = open("PlayerLogs/Pirates", "r")
    print(f"{red}Pirates:")
    print(f"{file.read()}{blank}")
    file.close()
    print()
    input("[press enter to continue]")

  def resetKills():
    file = open("PlayerLogs/Kills", "w")
    file.write("")
    file.close()

  def resetPirates():
    file = open("PlayerLogs/Pirates", "w")
    file.write("")
    file.close()
