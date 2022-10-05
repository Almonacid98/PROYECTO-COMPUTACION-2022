from controller_creation.character_controller.character_controller import save_character_files
list_type = []
def choice():
    choice = input("Enter the type of character, there are only 3 types -----> 1:[WARRIOR] * 2:[Elf] * 3:[Archer]")
    while True:
            if choice == '1':
                type = "WARRIOR"
                list_type.append(type)
                save_character_files()
                break
            elif choice == '2':
                type = "ELF"
                list_type.append(type)
                save_character_files()
                break
            elif choice == '3':
                type = "ARCHER"
                list_type.append(type)
                save_character_files()
                break
            else:
                print("\n WRONG OPTION.... PLEASE AGAIN CHOOSE AN EXISTING OPTION IN THE SYSTEM....")