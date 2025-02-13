
class MusicalInstruments():

    def __init__(self, name, brand, color,):
        self.name = name
        self.brand = brand
        self.color = color

    def info(self):
        print ("Instrument:", self.name, "brand:", self.brand, "Color:", self.color)

    def sound(self):
        print ("*sound11122223334444433333*")

#класс гитара
class Guitar(MusicalInstruments):

    def __init__(self, brand, color, model):
        super().__init__("guitar", brand, color)
        self.model = model
        

    def info(self):
        print ("Instrument:", self.name, "brand:", self.brand, "color:", self.color, "model:",self.model)
    
    def sound(self):
        print ("*guitar sound*")
    
#класс фортепиано
class Piano(MusicalInstruments):

    def __init__(self, brand, color, cost):
        super().__init__("piano", brand, color)
        self.cost = cost

    def info(self):
        print ("Instrument:", self.name, "brand:", self.brand, "color:", self.color,  "Cost:", self.cost)

    def sound(self):
        print ("*piano sound*")

#класс скрипки
class Violin(MusicalInstruments):
    def __init__(self, brand, color, cost):
        super().__init__("violin", brand, color)
        self.cost = cost

    def info(self):
        print ("Instrument:", self.name, "brand:", self.brand, "color", self.color, "Cost:", self.cost)

    def sound(self):
        print ("*violin sound*")

#использование классов
guitar = Guitar("Fender", "red", "mustang")
piano = Piano("Yamaha", "black", 150000)
violin = Violin("Stradivarius", "-", 60000)

guitar.info()
guitar.sound()
piano.info()
piano.sound()
violin.info()
violin.sound()