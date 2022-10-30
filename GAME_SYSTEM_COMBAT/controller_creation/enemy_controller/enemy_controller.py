from character_and_enemy_factory.enemy_factory.enemy_factory import *
def save_enemy():
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_one.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_one.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[0:6]]
            archive.writelines("\n" . join(lst_new))

        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_two.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_two.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[6:12]]
            archive.writelines("\n" . join(lst_new))
        
        
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_tree.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_tree.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[12:18]]
            archive.writelines("\n" . join(lst_new))
        
        
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_four.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_four.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[18:24]]
            archive.writelines("\n" . join(lst_new))
        
        
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_five.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_five.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[24:30]]
            archive.writelines("\n" . join(lst_new))
        
        
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_six.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_six.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[30:36]]
            archive.writelines("\n" . join(lst_new))

        
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_seven.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_seven.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[36:42]]
            archive.writelines("\n" . join(lst_new))

        
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_eight.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_eight.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[42:48]]
            archive.writelines("\n" . join(lst_new))

        
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_nine.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_nine.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[48:54]]
            archive.writelines("\n" . join(lst_new))

        
        open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_ten.txt", "w")
        chosen_file = 'C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_enemy/enemy_ten.txt'
        with open(chosen_file, "w") as archive:
            lst_new = [str(a) for a in lista_enemy[54:61]]
            archive.writelines("\n" . join(lst_new))
