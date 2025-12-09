# Skapar klassen Buss 
class Buss():
    # ────Skapar en konstruktor för klassen Buss─────────────────────────────
    # Skapar en lista för passagerare, antal passagerare och max antal passagerare
    def __init__(self):
        self.passagerare = []
        self.antal_passagerare = 0
        self.max_passagerare = 100
    # ────Skapar metoden run─────────────────────────────────────────────────
    # Startar programmet och visar menyn
    def run(self):
    # Skriver ut alternativen från listan meny_namn
        print("\nVälkommen till \033[1mBUSS-SIMULATOR!\033[0m")

        meny_namn = [
            "Lägg till passagerare", "Visa alla passagerare",
            "Beräkna totala åldern", "Beräkna genomsnittlig ålder",
            "Hitta högsta ålder", "Filtrera efter ålder",
            "Sortera passagerare", "Avsluta"
        ]

        # Skriver ut menyalternativ
        print("\nMENYALTERNATIV\n")
        # Använder funktionen enumerate för att iterera över listan meny_namn och skriver ut index position
        # Detta generar en numrerad lista
        for i, namn in enumerate(meny_namn):
            print(f"{i}: {namn}")
        # Visar hur användaren ska navigera sig framåt i programmet
        print("\nTryck ENTER att gå vidare")

        # ────Skapar en while loop ────────────────────────────────────────
        # Loopar tills användaren väljer ett alternativ i menyn
        while True:
            # Använder try-except för att fånga eventuella felaktiga inmatningar 
            try:
                # Avsluta programmet ligger i loopen om användaren inte minns alternativet
                # och har kört programmet flera gånger
                print("\n\033[4mAvsluta med 7\033[0m")
                # Ber användaren att göra ett val 
                meny_val = int(input("\nGör ett av följande val: "))
                print()
                 # Om användaren väljer 0, input av ålder på passagerare
                 # Använder try-except för att fånga eventuella felaktiga inmatningar           
                if meny_val == 0:  
                        try:
                            ålder = int(input("Ange ålder på passagerare: "))
                            # Anropar metoden add_passenger och skickar in ålder som parameter i listan passagerare
                            self.add_passenger(ålder)     
                        except ValueError:
                            print("\nFelaktig inmatning, försök igen.")
                # Om användaren väljer 1 anropas metoden print_buss och skriver ut passagerarna            
                elif meny_val == 1:
                    self.print_buss()
                 # Om användaren väljer 2 anropas metoden calc_total_age och beräknar den totala åldern på passagerarna    
                elif meny_val == 2:
                    self.calc_total_age()
                 # Om användaren väljer 3 anropas metoden calc_average_age och beräknar den genomsnittliga åldern på passagerarna
                elif meny_val == 3:
                    self.calc_average_age()
                 # Om användaren väljer 4 anropas metoden max_age och beräknar den högsta åldern på passagerarna
                elif meny_val == 4:
                    self.max_age()
                 # Om användaren väljer 5 anropas metoden find_age och beräknar åldern på passagerarna
                elif meny_val == 5:
                    self.find_age() 
                 # OM användaren väljer 6 anropas metoden sort_buss och sorterar passagerarna på bussen efter ålder      
                elif meny_val == 6:
                    self.sort_buss()
                 # Om användaren väljer 7 så avslutas programmet   
                elif meny_val == 7:
                    print("Avslutar programmet.")
                    # Loopen bryts och programmet avslutas
                    break
            # Vid fel inmatning skrivs felmeddelande ut och menyn skrivs ut igen
                # Utifall användaren inte minns menyalternativen
            except: 
                print("Fel inmatning. Välj mellan 0-7.\n")
                for i, namn in enumerate(meny_namn):
                    print(f"{i}: {namn}")
                continue 

    # ──Skapar metoden add_passenger────────────────────────────────────────────────────────────────────────────

    def add_passenger(self, passagerare):
         # Om listan passagerare överstiger eller är lika med max_passagerare
        if self.antal_passagerare >= self.max_passagerare:
            print("\nBussen är fullsatt!")
        else:
         # Om bussen inte är full så läggs passageraren till i listan passagerare och antal_passagerare ökar med 1
            self.passagerare.append(passagerare)
            self.antal_passagerare += 1
            print("\nPassagerare tillagd!")

    # ──Skapar metoden print_buss────────────────────────────────────────────────────────────────────────────

    def print_buss(self):
         # Om listan passagerare är tom skrivs meddelande ut 
        if self.passagerare == []:
            print("Det finns inga passagerare på bussen.")
         # Annars skrivs passagerarna ut     
        else:
            print("\nPassagerare på bussen:")
            # Använder en for loop för att gå igenom listan passagerare
            for ålder in self.passagerare:
                print(ålder)

    # ──Skapar metoden calc_total_age──────────────────────────────────────────────────────────────────────────

    def calc_total_age(self):
         # Använder if not för att kolla om listan passagerare är tom om sant skrivs meddelande ut
        if not self.passagerare:
            print("Det finns inga passagerare på bussen.")
         # Annars beräknas den totala åldern på passagerarna i listan passagerare
        else:
            # Skapar en variabel total_ålder och använder funktionen sum för att summera alla åldrar i listan passagerare
            total_ålder = sum(self.passagerare)
            print("Den totala åldern är:", total_ålder)

    # ──Skapar metoden calc_average_age───────────────────────────────────────────────────────────────────────

    def calc_average_age(self):
        # Använder if not för att kolla om listan passagerare är tom om sant skrivs meddelande ut
        if not self.passagerare:
            print("Det finns inga passagerare på bussen.")
            return
        # skapa en variabel total_ålder och använder funktionen sum för att summera alla åldrar i listan passagerare
        total_ålder = sum(self.passagerare)
        # Skapar en variabel räkna och använder funktionen len för att räkna antalet passagerare i listan passagerare
        räkna = len(self.passagerare)
        ## Beräknar den genomsnittliga åldern genom att dela total_ålder med räkna
        genomsnittlig_ålder = total_ålder / räkna
        # Anävnder f sträng för att använda en platshållare för att formatera utskriften
        # Skriver ut den genomsnittliga åldern med 2 decimaler
        print(f"Den genomsnittliga åldern för passagerarna är: {genomsnittlig_ålder:.2f}") 

    # ──Skapar metoden max_age───────────────────────────────────────────────────────────────────────────────

    def max_age(self):
        # Använder if not för att kolla om listan passagerare är tom om sant skrivs meddelande ut
        if not self.passagerare:
            print("Det finns inga passagerare på bussen.")
            return
        # Skapar en variabel max_ålder och använder funktionen max för att hitta den högsta åldern
        max_ålder = max(self.passagerare)
        # Skriver ut den högsta åldern
        print("Den högsta åldern är:", max_ålder)  

    # ──Skapar metoden find_age─────────────────────────────────────────────────────────────────────────────

    def find_age(self):
        # Använder if not för att kolla om listan passagerare är tom, om sant skrivs meddelande ut
        if not self.passagerare:
            print("Det finns inga passagerare på bussen.")
            return
        # Använder en while loop för att be användaren ange ett åldersintervall
        while True:
            # Använder try-except som felhantering
            try:
                # Input från användre för att ange åldersintervall
                print("Ange intervall för ålder:")
                print() # tom rad för att separera utskriften
                min_ålder = int(input("Minsta ålder: "))
                max_ålder = int(input("Högsta ålder: "))
                # Vid korrekt inmatning bryts loopen
                break
            # Om felaktig inmatning skrivs meddelande ut och loopen fortsätter
            except ValueError:
                         print("\nFelaktig inmatning. Skriv endast siffror.")
                         
        # Lista för passagerare inom åldersintervallet
        filtrerade_passagerare = []
        # Använder en for loop för att gå igenom listan passagerare
        for ålder in self.passagerare:
            # Om åldern på passagerare är mellan min_ålder och max_ålder läggs input till i listan filtrerade_passagerare genom funktionen append 
            if min_ålder <= ålder <= max_ålder:
                filtrerade_passagerare.append(ålder)
        # Använder if för att kolla om listan med filtrerade åldrar har något värde, om sant skrivs meddelande ut
        if filtrerade_passagerare:
            print(f"\nPassagerare mellan {min_ålder} och {max_ålder} år:")
            print() # tom rad för att separera utskriften
            # Använder en for loop för att gå igenom listan filtrerade_passagerare
            for ålder in filtrerade_passagerare:
                # Skriver ut åldern på passagerarna i listan med f sträng och platshållare
                print(f"{ålder} år")
        # Om listan filtrerade_passagerare är tom skrivs meddelande ut        
        else:
            print(f"\nInga passagerare mellan {min_ålder} och {max_ålder} år.")   

    # ──Skapar metoden sort_buss─────────────────────────────────────────────────────────────────────────────                 

    def sort_buss(self):
        # Använder if not för att kolla om listan passagerare är tom, om sant skrivs meddelande ut
        if not self.passagerare:
            print("Det finns inga passagerare att sortera.")
            return
        # Bubble Sort-algoritm
        # Skapar variabel a och använder funktion len för att räkna antal passagerare i listan 
        a = len(self.passagerare)
        # Använder en yttre loop som går lika många gånger som det finns passagerare i listan 
        for i in range(a):
            # Den inre loopen går igenom listan och jämför varje element med nästa men subtraherar index från a för att undvika att jämföra med redan sorterade element
            for o in range(0, a - i - 1):
            # Jämför nästliggande passagerare och byter plats om första är större större än den andra
                if self.passagerare[o] > self.passagerare[o + 1]:
                    # Byter plats på passagerarna i listan
                    self.passagerare[o], self.passagerare[o + 1] = self.passagerare[o + 1], self.passagerare[o]
        # Skriver ut meddelande att passagerarna har sorterats 
        print("Passagerarna har sorterats efter ålder:")
        # Anropa print_buss() för att visa den sorterade listan   
        self.print_buss()           

# Startar programmet genom att skapa ett objekt av klassen Buss och anropa metoden run()
if __name__ == "__main__":
    buss = Buss()
    buss.run()
