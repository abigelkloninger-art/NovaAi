def begruessung():
    print("Hallo! Ich bin NovaAI.")
    while True:
        frage = input("Du: ")
        if frage.lower() == "hallo":
            print("NovaAI: Hallo! Schön, dassdu da bist.")
        elif frage.lower() == "wie geht es dir":
            print("NovaAI:Mir geht es super!")
        elif frage.lower() == "wie heißt du":
            print("NovaAI: Ich heiße NobaAI.")
        elif frage.lower() == "tschüss":
            print("NovaAI: Bis bald!")
            break
        else:
            print("NovaAI: Das weiß ich leider noch nicht.")
