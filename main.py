import pickle
from pokemonClasses import *
from pessoaClasses import * 
from itensClasses import *


def definirNome():
    print("Olá jogador! Qual o seu nome?")
    nome = input()

    return Player(nome)


def pokemonInicial(player):
    print("Olá {}, escolha o pokemon que irá lhe acompanhar nessa jornada: ".format(player))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle',level=1)

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


def salvar_jogo(player):
    try:
        with open('.pokemon.save', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Algum erro ocorreu, não foi possível salvar")
        print("Erro:", error)

def load_game():
    try:
        with open('.pokemon.save' , 'rb') as arquivo:
            player = pickle.load(arquivo)
            print("Save carregado com sucesso!")
            return player
    except:
        print("Save não encontrado")
        return None


def loja(player):
    print("Olá bem vindo a Loja do Mundo Pokemon! O que você deseja?")

    #Potion cura level 1 preço 120
    Itemcura = ItemCura('Potion')

    #Potionara cura level 2 preço 600
    ItemCura2 = ItemCura('Potionara', level=2)

    #Éter de Mana preço 290
    eter = ItemMana("Éter")

    #Éter level 2 preço 900
    eter2 = ItemMana("Éterara", level=2)

    #Phoenix Down preço 500
    revive = ItemElixir()

    while(True):
        print("#     Loja    #")
        print("1 - Potion $120")
        print("2 - Potionara $600")
        print("3 - Éter $290")
        print("4 - Éterara $900")
        print("5 - Phoenix Down $500")
        print("\n\nSeu $:{}".format(player.dinheiro))

        opcao = input("O que você deseja (q para sair)?")

        if opcao == 'q':
            break
        elif opcao == '1':
            if player.dinheiro >= 100:
                player.dinheiro -= 100
                player.itens.append(Itemcura)
                print("Você adquiriu Potion!")
            else:
                print("Você não tem dinheiro suficiente!")
        elif opcao == '2':
            if player.dinheiro >= 600:
                player.dinheiro -= 600
                player.itens.append(ItemCura2)
                print("Você adquiriu Potionara!")
            else:
                print("Você não tem dinheiro suficiente!")
        elif opcao == '3':
            if player.dinheiro >= 290:
                player.dinheiro -= 290
                player.itens.append(eter)
                print("Você adquiriu Éter!")
            else:
                print("Você não tem dinheiro suficiente!")
        elif opcao == '4':
            if player.dinheiro >= 900:
                player.dinheiro -= 900
                player.itens.append(eter2)
                print("Você adquiriu Éterara!")
            else:
                print("Você não tem dinheiro suficiente!")
        elif opcao == '5':
            if player.dinheiro >= 500:
                player.dinheiro -= 500
                player.itens.append(revive)
                print("Você adquiriu Phoenix Down!")
            else:
                print("Você não tem dinheiro suficiente!")

def menu(player):
    while True:
        print("             MENU             ")
        print("1 - Explorar a floresta")
        print("2 - Ir para o torneio")
        print("3 - Ver seus pokemons")
        print("4 - Ver seu dinheiro")
        print("5 - Ver seus itens")
        print("6 - Ir ao médico")
        print("7 - Ir a Loja")
        print("8 - Batalhar")
        print("9 - Salvar game")
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
            #usar itens
            player.ver_itens()
        elif opcao == '6':
            #médico
            medico(player, player.pokemons)
            pass
        elif opcao == '7':
            #ir a loja
            loja(player)
            pass
        elif opcao == '8':
            inimigo = Inimigo()
            player.batalhar(inimigo)
        elif opcao == '9':
            salvar_jogo(player)
        elif opcao == '0':
            return 0


def main():
    print("________________________________________________________")
    print("Olá, bem vindx ao game Pokemon RPG de Terminal!!")
    print("________________________________________________________")

    print("     1 - Novo Jogo")
    print("     2 - Load Game")
    print("     3 - Sair")

    opcao = input("Sua opção: ")

    if opcao == '3':
        return 0
    elif opcao == '2':
        player = load_game()
        if player != None:
            menu(player)
    elif opcao == '1':
        nome = input("Qual o seu nome? ")

        player = Player(nome, pokemons=[])
    
        pokemonInicial(player)
    
        print("Ei espere ai! Você é o {}, lembra de mim não é? Meu arquirival da academia... Vamos duelar!".format(player))   

        inimigo1 = Inimigo(nome='Almir', pokemons=[PokemonPlanta('Plantoyde',level=1)])
        player.batalhar(inimigo1)


        menu(player)


main()

