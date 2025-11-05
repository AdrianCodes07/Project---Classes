class Karaktar:
    def __init__(self, namn, hälsa, kraft):
        self.namn = namn
        self.hälsa = hälsa
        self.kraft = kraft

    def attack(self, annan_karaktär):
        print(f"{self.namn} attackerar {annan_karaktär.namn}!")
        annan_karaktär.hälsa -= self.kraft
        print(f"{annan_karaktär.namn} förlorar {self.kraft} HP och har nu {annan_karaktär.hälsa} HP kvar.")


class Ranger (Karaktar):
        def __init__ (self, namn):
            super().__init__(namn, hälsa=100, kraft=20)
        def attack (self, annan_karaktär):
            import random
            krit = random 
            skada = self.attack * krit
            print(f"{self.namn} skjuter en pil mot {annan_karaktär.namn}!") 
            annan_karaktär.hälsa -= skada
            print(f"{annan_karaktär.namn} förlorar {skada:0f} HP och har nu {annan_karaktär.hälsa:0f} HP kvar.")

class Warrior (Karaktar):
    def __init__(self, namn, hälsa, kraft):
          super().__init__(namn, hälsa=120, kraft=15)
    def attack(self, annan_karaktär):
         skada = self.kraft + 5 
         print(f"{self.namn} svingar sitt svärd mot ")
             


