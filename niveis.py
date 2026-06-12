#primeiro passo
class Niveis:
    def __init__(self):
        self.nivel_atual = 1

    def proximo_nivel(self):
        self.nivel_atual += 1

    def get_nivel(self):
        return self.nivel_atual