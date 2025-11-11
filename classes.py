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
    def attack(self, annan_karaktär):
         skada = self.kraft + 5 
         print(f"{self.namn} svingar sitt svärd mot {annan_karaktär}")


