plik1 = open("slownik.txt");

command = '';

wejscie1 = input("Śmieciarka czeka na Twoje polecenie : ");
wejscie = wejscie1.lower().split();


p1 = plik1.readlines();
slownik = list(map(lambda s: s.split(),p1));


for slowo_wejscie in wejscie:
    for slowo_slownik in slownik:
        if slowo_slownik[0]==slowo_wejscie and slowo_slownik[1]== 'STREETNAME':
            command= command + slowo_slownik[0] + " " + slowo_slownik[1] + " ";
        elif slowo_slownik[0]==slowo_wejscie:
            command = command + slowo_slownik[1] + " ";

command = command + "X";
command = list(command.split());
X="T";
for slowo in command:
    if slowo == 'CLEAN':
        for slowo1 in command:
            if slowo1 == 'ALL':
                print("COMMAND CLEAN ALL")
                X="N";
            elif slowo1 == 'STREET':
                i=0;
                for ulica in command:
                    if ulica == 'STREETNAME':
                        print("COMMAND CLEAN STREET "+ command[i-1])
                        X="N";
                    i=i+1;
                    if ulica == "X" and X=="T":
                        print("Brak nazwy ulicy, sproboj ponownie")
                        X="N";
            elif slowo1 == "X" and X=="T":
                print("smieciarka nie wie co ma wyczyscic, sproboj ponownie")
                X="N";
    elif slowo== "X" and X=="T":
        print("smieciarka nie obsługuje podanego czasownika, lub go brakuje, sproboj jeszcze raz")

plik1.close
