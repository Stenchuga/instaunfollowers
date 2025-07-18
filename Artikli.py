artikli=[]
while True:
    opt = input(
        "Izaberi opciju:\n1 - Dodaj artikal\n2 - Obrisi artikal\n3 - Prikazi listu\n4 - Pretrazi artikal\n5 - Izadji iz programa")

    if opt=="1":
        artikli.append(input("Artikal: "))
        continue

    if opt=="2":
        print("Odaberite artikal:\n")
        for artikal in artikli:
            print(artikal)
        brisanje = input()
        if brisanje in artikli:
            artikli.remove(brisanje)
            print("Artikal izbrisan")
        else:
            print("Pogresan unos\n")
            continue
    if opt=="3":
        for artikal in artikli:
            print(artikli.index(artikal)+1,artikal)
    if opt=="4":
        pretraga=input("Pretrazi artikal: ")
        if pretraga in artikli:
            print("Artikal je u listi\n")
        else:
            print("Artikal nije u listi\n")
    if opt=="5":
        break