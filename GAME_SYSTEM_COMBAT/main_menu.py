from controller_creation.character_controller.character_controller import *
from character_and_enemy_factory.enemy_factory.enemy_factory import *
from combat_system.combat.combat import *
from controller_creation.enemy_controller.enemy_controller import *
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
                charac = Contantes()
                charac.character_creation_menu()
                charac.save_character_files()

            elif choice == '2':
                for i in range(10):
                    lista = ['Warrior', 'Elf', 'Archer', 'Wizard', 'Master Swordsman']
                    race = ['Human', 'Inhuman']
                    enemy = Enemy(random.choice(race), random.randint(0, 100), random.randint(0, 5), random.randint(0, 5), random.randint(1, 5), random.choice(lista))
                    enemy.generate()
                    
            elif choice == '3':
                selection = Combat()
                selection.select_character()

            elif choice == "4":
                Contantes.delete_character()

            elif choice == "5":
                save_enemy()
                combat = Combat()
                combat.select_enemy()
                combat.combat()

            elif choice == '6':
                print("¡Thanks For Fighting With The Team!")
                break

            else:
                print("\n WRONG OPTION.... PLEASE AGAIN CHOOSE AN EXISTING OPTION IN THE SYSTEM....")

start_menu()