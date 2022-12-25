class Item:
    def __init__(self, nome, level=1):
        self.nome = nome
        self.level = level

        if level > 1:
            self.porcentagem = 45
        elif level > 2:
            self.porcentagem = 60
        else:
            self.porcentagem = 35

class ItemCura(Item):
 
    def __str__(self) :
        return "Potion de cura level {} restaura {}\\%\\ de HP".format(self.level, self.porcentagem)

    def usar(self, pokemon):
        if pokemon.status == ' - X derrotado X':
            print("Não é possível usar item de cura em um pokemon derrotado!")
            return False
        else:
            pokemon_vida = pokemon.level * 10
            hp_a_ganhar = (int(self.porcentagem) * pokemon_vida) / 100
            pokemon.vida += int(hp_a_ganhar)
            print("{} recuperou {} pontos de vida!".format(pokemon, hp_a_ganhar))
            return True


class ItemMana(Item):

    def __str__(self):
        return "Eter de Mana level {} restaura {}\%\ de MP".format(self.level, self.porcentagem)

    def usar(self, pokemon):
        if pokemon.status == ' - X derrotado X':
            print("Não é possível usar item de cura em um pokemon derrotado!")
            return False
        else:
            pokemon_mana = pokemon.level * 3
            mp_a_ganhar = (int(self.porcentagem) * pokemon_mana) / 100
            pokemon.mp += int(mp_a_ganhar)
            print("{} recuperou {} ponts de MP!".format(pokemon, mp_a_ganhar))
            return True

class ItemElixir(Item):

        def __init__(self):
            super().__init__('Fenix Down')

        def __str__(self):
            return "Fenix Down level {} Cura um pokemon derrotado!".format(self.level)

        def usar(self, pokemon):
            if pokemon.status == ' - X derrotado X':
                hp_full = pokemon.level * 10
                hp_a_ganhar = (int(self.porcentagem) * hp_full) / 100
                pokemon.status = ""
                pokemon.vida += int(hp_a_ganhar)
                print("{} Acordou usando {}".format(pokemon, self.nome))
                return True
            else:
                print("{} está bem!".format(pokemon))
                return False
