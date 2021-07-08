from Clear import clear
import time

green = "\033[1;32;12m"
red = "\033[0;31;12m"
orange = "\033[0;33;12m"
white = "\033[0;37;12m"
blank = "\033[0;37;12m"

class Bookmark:
  def SystemBookmark():
    print("What system would you like to bookmark?")
    system = input("[enter system here]: ")

    clear()

    print("What planet in the system would you like to bookmark?")
    planet = input("[enter planet here - you can leave this blank]: ")

    clear()

    print("What is the description of the system you are bookmarking?")
    desc = input("[enter the description here - you can leave this blank]: ")

    clear()

    file = open("Bookmark/Bookmarks", "r")
    read = file.read()
    file.close()

    file = open("Bookmark/Bookmarks", "w")
    file.write(f"{read}\n-{system}:{planet}:{desc}")
    file.close()
  
  def VeiwBookmarks():

    print(f"{orange}Bookmarks:{blank}")

    file = open("Bookmark/Bookmarks", "r")
    print(f"{orange}{file.read()}{blank}")
    file.close()

    print("\n")

    input("[press enter to continue]: ")

  def RemoveBookmark():

    print("What is the name of the bookmarked system you would like to remove from your bookmarks?")
    system = input("[enter system here]: ")

    clear()

    if system != "":

      file = open("Bookmark/Bookmarks", "r")
      read = file.read()
      file.close()

      find = read.find(f"{system}:")

      if find < 0:
        print(f"{red}That system is not bookmarked!{blank}")
        time.sleep(2)
        clear()
      else:
        firstHalf = read[:find-2]

        read = read[find:]

        find = read.find("-")

        if find < 0:
          file = open("Bookmark/Bookmarks", "w")
          file.write(firstHalf)
          file.close()

        else:
          secondHalf = read[find:]

          file = open("Bookmark/Bookmarks", "w")
          file.write(f"{firstHalf}\n{secondHalf}")

        clear()
        print(f"{green}Done!{blank}")
        time.sleep(1)
        clear()
  
  def Reset():
    file = open("Bookmark/Bookmarks", "w")
    file.write("")
    file.close()