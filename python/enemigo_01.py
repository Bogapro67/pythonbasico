class Enemigo:
    tipo_enemigo: str
    puntos_energia: int = 10
    ataque = 1

    def _init_(self, tipo_enemigo, puntos_energia=10, ataque=1):
        self._tipo_enemigo = tipo_enemigo
        self.puntos_energia = puntos_energia
        self.ataque = ataque

    def get_tipo_enemigo(self):
        return self._tipo_enemigo

    def habla(self):
        print(f"yo soy {self._tipo_enemigo}. preparado para pelear!!!")

    def camina(self):
        print(f"{self._tipo_enemigo} se mueve cerca de ti!!!")

    def atacar(self):
        print(f"{self._tipo_enemigo} ataca con un {self.ataque} ")   

























        