import random
import time

#superklass
class Karaktar:
    def __init__(self, namn, hälsa, kraft):
        self.namn = namn
        self.hälsa = hälsa
        self.kraft = kraft

    def attack(self, annan_karaktär):
        print(f"{self.namn} attackerar {annan_karaktär.namn}!")
        annan_karaktär.hälsa -= self.kraft
        if annan_karaktär.hälsa < 0:
            annan_karaktär.hälsa = 0
        print(f"{annan_karaktär.namn} förlorade {self.kraft} HP och har nu {annan_karaktär.hälsa} HP kvar.")

    def är_vid_liv(self):
        return self.hälsa > 0

#subklass, ranger
class Ranger (Karaktar):
        def __init__ (self, namn):
            super().__init__(namn, hälsa=100, kraft=20)
            self.energi = 40 

        def attack (self, annan_karaktär):
            krit_chans = random.randint(1, 6) #slump för kritisk träff
            krit = 2 if krit_chans == 6 else 1 
            skada = self.attack * krit
            if krit == 2:
                print(f"Kritisk träff av {self.namn}!")
            print(f"{self.namn} skjuter en pil mot {annan_karaktär.namn}!") 
            annan_karaktär.hälsa -= skada
            if annan_karaktär.hälsa < 0:
                annan_karaktär.hälsa = 0
            print(f"{annan_karaktär.namn} förlorar {skada:0f} HP och har nu {annan_karaktär.hälsa:0f} HP kvar.")
        
        def specialattack(self, annan_karaktär):
            kostnad = 15 
            if self.energi < kostnad:
                print(f"{self.namn} har inte nog med energi för specialattack!")
                return
            self.energi -= kostnad
            skada = self.kraft + random.randint(16, 25)
            print(f"{self.namn} använder Rain of Arrows på {annan_karaktär.namn} för {skada} skada!")
            annan_karaktär.hälsa -= skada
            if annan_karaktär.hälsa < 0:
                annan_karaktär.hälsa = 0
            print(f"{annan_karaktär.namn} har nu {annan_karaktär.hälsa} HP kvar.")

#subklass, krigare
class Warrior (Karaktar):
    def __init__(self, namn, hälsa, kraft):
          super().__init__(namn, hälsa=120, kraft=15)
          self.stamina = 35


    def attack(self, annan_karaktär):
        skada = self.kraft + random.randint(-3, 4)
        print(f"{self.namn} svingar sitt svärd mot {annan_karaktär}")
        annan_karaktär.hälsa -= skada
        if annan_karaktär.hälsa < 0:
            annan_karaktär.hälsa = 0
        print(f"{annan_karaktär.namn} har nu {annan_karaktär.hälsa} HP kvar.")
    
    def specialattack(self, annan_karaktär):
        kostnad = 18 
        if self.stamina < kostnad: 
            print("f{self.namn} har inte nog stamina ({self.stamina}/{kostnad})!")
            return
        self.stamina -= kostnad 
        skada = self.kraft * 2 + random.randint(5,10)
        print(f"{self.namn} utför Crushing Blow mot {annan_karaktär.namn} för {skada} skada!")
        if annan_karaktär.hälsa < 0:
            annan_karaktär.hälsa = 0 
            print(f"{annan_karaktär.namn} har nu {annan_karaktär.hälsa} HP kvar.")

class Mage(Karaktar):
    def __init__(self, namn):
        super().__init__(namn, hälsa=80, kraft=25)
        self.mana = 50
    
    def attack(self, annan_karaktär):
        skada = self.kraft + random.randint(-5, 5)
        print(f"{self.namn} använder Firestorm och träffar {annan_karaktär.namn} för {skada} skada!")
        annan_karaktär.hälsa -= skada
        if annan_karaktär.hälsa < 0:
            annan_karaktär.hälsa = 0 
        print(f"{annan_karaktär.namn} har nu {annan_karaktär.häksa} HP kvar.")

class Arena:
    def __init__(self):
        self.kar1 = self.välj_karaktär(1)
        self.kar2 = self.välj_karaktär(2)
    
    def välj_karaktär(self, nummer):
        print(f"\nVälj karaktär #{nummer}:")
        print("1) Ranger\n2) Warrior\n3 Mage")
        while True:
            val = input("Skriv numret för din valda karaktär: ").strip()
            namn = input("Ge din karaktär ett namn: ").strip()
            if val == "1":
                return Ranger(namn)
            elif val == "2":
                return Warrior(namn)
            elif val == "3":
                return Mage(namn)
    
    def starta_strid(self):
        print(f"Striden börjar mellan {self.kar1.namn} och {self.kar2.namn}")
        runda = 1 
        while self.kar1.är_vid_liv() and self.kar2.är_vid_liv():
            print(f"Runda")
            self.tur(self.kar1, self.kar2)
            if not self.kar2.är_vid_liv():
                print(f"{self.kar1.namn} vinnner kampen!")
                break


            self.tur(self.kar2, self.kar1)
            if not self.kar1.är_vid_liv():
                print(f"{self.kar2.namn} vinner kampen!")
                break

            runda += 1
            time.sleep(0.7)
    

    def tur(self, attacker, försvarare):
        if hasattr(attacker, "specialattack") and random.choice([True, False]):
            attacker.specialattack(försvarare)
        else: 
            attacker.attack(försvarare)

if __name__ == "__main__":
    arena = Arena()
    arena.starta_strid()