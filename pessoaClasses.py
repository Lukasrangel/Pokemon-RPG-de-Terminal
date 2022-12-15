import random
from pokemonClasses import *


NOMES = ['Alan', 'Alex' ,'Bruno', 'Bruna', 'Chris', 'Carmen','Carmelo','Crudemiro',
    'Cleiton','Diego', 'Jonas','Lukas','Luan','Darvin','Marvin']

POKEMONS = [PokemonAgua('Squirtle'),
    PokemonAgua('Aguasaaur'), 
    PokemonAgua('Magicarp'),
    PokemonAgua('Psyduck'),
    PokemonAgua('Poliwag'),
    PokemonAgua('Krabby'),
    PokemonAgua('Piplup'),
    PokemonFogo('Vermilion'),
    PokemonFogo('Charizard'),
    PokemonFogo('Tepig'),
    PokemonFogo('Magby'),
    PokemonFogo('Chimchar'),
    PokemonFogo('Flareon'),
    PokemonEletrico('Raichu'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Emolga'),
    PokemonEletrico('Tynamo'),
    PokemonEletrico('Electricke'),
    PokemonEletrico('Pichu'),
    PokemonPlanta('Plantoyde'),
    PokemonPedra('Geodude'),
    PokemonPedra('Golem'),
    PokemonPedra('Onyx'),
    PokemonPedra('Kabuto'),
    PokemonPedra('Ominyte'),
    
    ]


class Pessoa:

    
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrarPokemons(self):
        if self.pokemons:
            print("---------------------------------------")
            for indice, pokemon in enumerate(self.pokemons):
                print("{} - {} {}".format(indice, pokemon, pokemon.status) )
            print("-------------------------------------------")
        else:
            print("{} não possui nenhum Pokemon".format(self))
    
    def escolherPokemon(self):
        if self.pokemons:
            self.mostrarPokemons()
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}!!".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Este personagem não possui pokemons para batalhar!")

    def batalhar(self, pessoa):
        print("{} iniciu um batalha com {}".format(self,pessoa))
        print("(Para fugir aperte CRTL + C)")

        try:
            pokemon_inimigo = pessoa.escolherPokemon()
            pokemon_inimigo.aprenderMagia(levelUp=False)
            pokemon = self.escolherPokemon()
        except:
            print("Esta batalha não pode ocorrer!")
            return 0

        while True:
            print("{} HP {}".format(pokemon_inimigo, pokemon_inimigo.vida))
            print("{} HP {} MP {}".format(pokemon, pokemon.vida, pokemon.mp))

            print("0 - Ataque Comum")
            print("1 - Ataques especias")
            print("3 - Item")

            acao = input("Sua ação: ")

            if acao == '0':
                #ataque comum
                vitoria = pokemon.atacar(pokemon_inimigo)
            elif acao == '1':
                #ataques especiais
                for indice, magia in enumerate(pokemon.magias):
                    print("{} - {}".format(indice, magia))

                acao = input("Sua ação: ")

                try:
                    magia = pokemon.magias[int(acao)]

                    if acao == '0':
                        vitoria = pokemon.especial1(pokemon_inimigo)
                    elif acao == '1':
                        vitoria = pokemon.especial2(pokemon_inimigo)
                    elif acao == '2':
                        vitoria = pokemon.especial3(pokemon_inimigo)
                    elif acao == '3':
                        vitoria = pokemon.especial4(pokemon_inimigo)
                    elif acao == '4':
                        vitoria = pokemon.especial5(pokemon_inimigo)
                    elif acao == '5':
                        vitoria = pokemon.especial6(pokemon_inimigo)
                    elif acao == '6':
                        vitoria = pokemon.especial7(pokemon_inimigo)
                    elif acao == '7':
                        vitoria = pokemon.especial8(pokemon_inimigo)
                    elif acao == '8':
                        vitoria = pokemon.especial9(pokemon_inimigo)

                except:
                    print("Ação inválida, você perdeu o turno!")
                    vitoria = False
            elif acao == '3':
                #item!
                pass
            else:
                print("Acão inválida, você perdeu este turno!")
                vitoria = False

            if vitoria:
                print("{} venceu a batalha!".format(pokemon))
                xp = int(pokemon_inimigo.level * 2.3)
                levelup = pokemon.proximoLevel(xp)
                if levelup:
                    pokemon.aprenderMagia()

                pokemon.recuperar()
                dinheiro = pokemon_inimigo.level * 25
                self.ganharDinheiro(dinheiro) 
                print("------------------------------------------")
                break

            if random.random() > 0.6:
                magias = int(len(pokemon_inimigo.magias) - 1)
                sorteio = str(random.randint(0,magias))
                if sorteio == '0':
                    vitoria_inimiga = pokemon_inimigo.especial1(pokemon)
                elif sorteio == '1':
                    vitoria_inimiga = pokemon_inimigo.especial2(pokemon)
                elif sorteio == '2':
                    vitoria_inimiga = pokemon_inimigo.especial3(pokemon)
                elif sorteio == '3':
                    vitoria_inimiga = pokemon_inimigo.especial4(pokemon)
                elif sorteio == '4':
                    vitoria_inimiga = pokemon_inimigo.especial5(pokemon)
                elif sorteio == '5':
                    vitoria_inimiga = pokemon_inimigo.especial6(pokemon)
                elif sorteio == '6':
                    vitoria_inimiga = pokemon_inimigo.especial7(pokemon)
                elif sorteio == '7':
                    vitoria_inimiga = pokemon_inimigo.especial8(pokemon)
                elif sorteio == '8':
                    vitoria_inimiga = pokemon_inimigo.especial9(pokemon)
                
            else:
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)

            if vitoria_inimiga:
                pokemon.vida = 0
                print("{} foi derrotado!".format(pokemon))
                dinheiro = pokemon.level * 25
                self.perderDinheiro(dinheiro)
                pokemon.status = ' - X derrotado X'
                print("------------------------------------------")
                break

   

class Player(Pessoa):
    tipo = 'Player'
    
    dinheiro = 100

    def mostrarDinheiro(self):
        print("Você possui ${}".format(self.dinheiro))

    def ganharDinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou ${}".format(quantidade))
        self.mostrarDinheiro()

    def perderDinheiro(self, quantidade):
        self.dinheiro -= quantidade
        if self.dinheiro < 0:
            self.dinheiro = 0
        print("Você perdeu ${}".format(quantidade))
        self.mostrarDinheiro()


    def capturar(self, Pokemon):
            Pokemon.aprenderMagia(levelUp=False)
            Pokemon.xp = (Pokemon.level - 1) * 6 * (Pokemon.level - 1)
            self.pokemons.append(Pokemon)
            print("Pokemon {} capturado!".format(Pokemon))
            
        

    def escolherPokemon(self):
        if self.pokemons:
            while True:
                print("\nSeus Pokemons:")
                self.mostrarPokemons()
                escolha = input("Escolha o pokemon para a batalha: ")
                try:
                    escolha = int(escolha)
                    if self.pokemons[escolha].status != " - X derrotado X":
                        pokemon_escolhido = self.pokemons[escolha]
                        print("{} eu escolho voce!!".format(pokemon_escolhido))
                        return pokemon_escolhido
                    else: 
                        print("Este pokemon não está pronto para lutar!")
                except:
                    print("Escolha inválida!")
        else:
            print("Sem pokemons a escolher!")

    
    def explorar(self):
        print("Explorando a floresta!")

        if(random.random() < 0.3):
            pokemon = random.choice(POKEMONS)
            print("Um {} selvagem apareceu!!".format(pokemon))
            escolha = input("Deseja tentar capturálo (s/n)? ")
            if escolha == "n":
                print("Ok, passando...")
                return 0
            if escolha == "s":
                if random.random() < 0.3:
                    self.capturar(pokemon)
                else:
                    print("{} fugiu!".format(pokemon))
        else:
            print("Nenhum pokemon encontrado...")

class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self,nome=None,pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(3):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)
             


    
    

        



