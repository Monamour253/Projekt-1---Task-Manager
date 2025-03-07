ukoly = []


def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

       
        try:
            volba = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            print(f"Neplatný vstup. Zadejte číslo mezi 1 a 4.")
            continue
        

        if volba == 1:
            pridat_ukol(ukoly)
            
        elif volba == 2:
            zobrazit_ukoly()

        elif volba == 3:
            if ukoly:
                print("Seznam úkolů: ")
                for i, ukol in enumerate(ukoly, 1):
                    print(f"{i}. {ukol['název']} - {ukol['popis']}")
            else:
                print("Nemáte žádné úkoly.")
            
            
            try:
                index = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
                odstranit_ukol(index)

            except ValueError:
                print("Neplatný vstup. Zadejte platné číslo úkolu!")
                continue

        elif volba == 4:
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zadejte číslo mezi 1 a 4.")


def pridat_ukol(ukol):
    while True:
        nazev = input("Zadejte název úkolu: ")
        if not nazev.strip():
            print("Název úkolu nemůže být prázdny. Zkuste to znovu.")
            continue

        popis = input("Zadejte popis úkolu: ")
        if not popis.strip():
            print("Popis úkolu nemůže být prázdny. Skuste to znovu.")
            continue


        ukoly.append({"název": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break

def zobrazit_ukoly():
    if not ukoly:
        print("Nemáte žádné úkoly.")

    else:
        print("Seznam úkolů: ")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['název']} - {ukol['popis']}")
    

def odstranit_ukol(index):
    if 0 < index <= len(ukoly):
        removed_task = ukoly.pop(index - 1)
        print(f"Úkol '{removed_task['název']}' byl odstraněn.")
    else:
        print("Neplatný index. Zkuste to znovu.")

hlavni_menu()



        




       

