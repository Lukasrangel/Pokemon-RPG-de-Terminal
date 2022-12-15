from pokemonClasses import *
from pessoaClasses import * 


def definirNome():
    print("Olá jogador! Qual o seu nome?")
    nome = input()

    return Player(nome)


def pokemonInicial(player):
    print("Olá {}, escolha o pokemon que irá lhe acompanhar nessa jornada: ".format(player))

    pikachu = PokemonEletrico('Pikachu', level=34)
    charmander = PokemonFogo('Charmander', level=34)
    squirtle = PokemonAgua('Squirtle',level=34)

    while True:
        print('1 - Pikachu')
        print('2 - Charmander')
        print('3 - Squirtle')
        escolha = input('Digite sua escolha:')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print("Opção inválida!")


#def status()

def medico(player, pokemons):
    print("Olá {}, bem vindo ao Hospital de Pokemons!!".format(player))
    while True:
        player.mostrarPokemons()
        try:
            escolha = int(input("Qual pokemon você deseja curar? (-1 para sair) "))
            if escolha != -1:
                try:
                    for indice, pokemon in enumerate(pokemons):
                        print(indice, pokemons[indice])
                        if escolha == indice:
                            if pokemons[indice].status != '':
                                preco = pokemons[indice].level * 75
                                print("O valor para curar este pokemon sai $ {}".format(preco))
                                print("Seu dinheiro: ${}".format(player.dinheiro))
                                pagar = input("Pagar (s/n)?")
                                if pagar == 's':
                                    if preco <= player.dinheiro:
                                        player.dinheiro -= preco
                                        pokemons[indice].status = ''
                                        pokemons[indice].recuperar()
                                        print("{} está curado!!!".format(pokemon))
                                        return 0
                                    else:
                                        print("Você não tem dinheiro suficiente!!")
                                        return 0
                                else:
                                    print("Ok")
                                    return 0 
                            else:
                                print("Este pokemon está bem!!")
                except:
                    break    
            else:
                break     
        except:
            print("Opção inválida")

def menu(player):
    while True:
        print("             MENU             ")
        print("1 - Explorar a floresta")
        print("2 - Ir para o torneio")
        print("3 - Ver seus pokemons")
        print("4 - Ver seu dinheiro")
        print("5 - Ir ao médico")
        print("6 - Batalhar")
        print("0 - Sair")

        opcao = input("Digite sua opção: ")

        if opcao == '1':
            player.explorar()
        elif opcao == '2':
            #criar torneio
            pass
        elif opcao == '3':
            print("Seus Pokemons: ")
            player.mostrarPokemons()
            try:
                indice = int(input("Status Pokemon: "))
                player.pokemons[indice].infos()
            except: 
                pass
            
        elif opcao == '4':
            player.mostrarDinheiro()
            print("________________________________")
        elif opcao == '5':
            #criar médico
            medico(player, player.pokemons)
            pass
        elif opcao == '6':
            inimigo = Inimigo(nome='Almir', pokemons=[PokemonFogo('Totokaie', level=39)])
            player.batalhar(inimigo)
        elif opcao == '0':
            return 0


def main():
    print("________________________________________________________")
    print("Olá, bem vindx ao game Pokemon RPG de Terminal!!")
    print("________________________________________________________")

    nome = input("Qual o seu nome? ")

    player = Player(nome, pokemons=[])
    
    pokemonInicial(player)

    #print("Ei espere ai! Você é o {}, lembra de mim não é? Meu arquirival da academia... Vamos duelar!".format(player))   

    #inimigo1 = Inimigo(nome='Almir', pokemons=[PokemonPlanta('Plantoyde',level=1)])
    #player.batalhar(inimigo1)

    menu(player)


main()

