from Enemigo import

class Ogro(Enemigo):
    def _init_(self, puntos_energia=20, ataque=3):
        super()._init_(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque):

    def habla (self):
        print("Hummm...")

    def propagar_enfermedad(self):
        print("El Zombie esta tratando de propagar la enfermedad!!")
