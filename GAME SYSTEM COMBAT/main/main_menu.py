from controller_creation.character_controller import *
from main_constants_menu import *
def start_menu():
    while True:
            print("<<<<<GAME SYSTEM COMBAT>>>>>")
            print("1 = Create Character:")
            print("2 = Initialize Enemy:")
            print("3 = Choose Character:")
            print("4 = Delete Character:")
            print("5 = Initiate Combat:")
            print("6 = <<GAME OVER>>")
            choice = input("CHOOSE THE MODE TO START PLAYING[1/2/3/4/5/6]  = ")
            if choice == '1':
                character_creation_menu()
                save_character_files()
            elif choice == '2':
                pass

            elif choice == '3':
                pass

            elif choice == "4":
               delete_character()

            elif choice == "5":
                pass

            elif choice == '6':
                print("¡Thanks For Fighting With The Team!")
                break
            else:
                print("\n WRONG OPTION.... PLEASE AGAIN CHOOSE AN EXISTING OPTION IN THE SYSTEM....")

"""libreria = Library()"""

start_menu()