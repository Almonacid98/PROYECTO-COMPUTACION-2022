
def character_view():
    a = {}
    with open("C:/Users/devil/OneDrive/Escritorio/GAME_SYSTEM_COMBAT/archive_consult/character_one.txt") as f:
        for line in f:
            (k, v) = line.split()
            a[int(k)] = v
    print(a)