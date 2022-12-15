import random
class Pokemon:


    def __init__(self,especie, nome=None, level=None):
        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1,100) 

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.vida = self.level * 10
        self.ataque = self.level * 5
        self.status = ''
        self.xp = 0
        self.mp = self.level * 3

    def __str__(self):
        return "{}({}) ({})".format(self.nome,self.level,self.tipo)

    def aprenderMagia(self,levelUp=True):
        #Tipo Elétrico
        if self.tipo == 'Elétrico' and self.level >= 11:
            self.magias.append('Raio do Trovão(Nivel2)')
            if levelUp == True: 
                print("{} aprendeu Raio do Trovão(Nível 2)!".format(self))
                return None
    
        if self.tipo == 'Elétrico' and self.level >= 20:
            self.magias.append('Cura(Nivel1)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 1)!".format(self))
                return None

        if self.tipo == 'Elétrico' and self.level >= 32:
            self.magias.append('Raio do Trovão(Nivel3)')
            if levelUp == True:
                print("{} aprendeu Raio do Trovão(Nível 3)!".format(self))
                return None

        if self.tipo == 'Elétrico' and self.level >= 47:
            self.magias.append('Raio do Trovão(Nivel4)')
            if levelUp == True:
                print("{} aprendeu Raio do Trovão(Nível 4)!".format(self))
                return None

        if self.tipo == 'Elétrico' and self.level >= 61:
            self.magias.append('Cura(Nivel2)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 2)!".format(self))
                return None

        if self.tipo == 'Elétrico' and self.level >= 79:
            self.magias.append('Raio do Trovão(Nivel5)')
            if levelUp == True:
                print("{} aprendeu Raio do Trovão!(Nivel 5)!".format(self))
                return None

        if self.tipo == 'Elétrico' and self.level >= 94:
            self.magias.append('Cura(Nivel3)')
            if levelUp == True:
                print("{} aprendeu Cura(Nivel 3)!".format(self))
                return None

        #Tipo Água
        if self.tipo == 'Água' and self.level >= 10:
            self.magias.append('Cura(Nivel1)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 1)!".format(self))
                return None

        if self.tipo == 'Água' and self.level >= 19:
            self.magias.append("Jato d'agua(Nivel2)")
            if levelUp == True:
                print("{} aprendeu Jato d'agua(Nível 2)!".format(self))
                return None

        if self.tipo == 'Água' and self.level >= 31:
            self.magias.append("Cura(Nivel2)")
            if levelUp == True:
                print("{} aprendeu Cura(Nível 2)!".format(self))
                return None

        if self.tipo == 'Água' and self.level >= 40:
            self.magias.append("Jato d'agua(Nivel3)")
            if levelUp == True:
                print("{} aprendeu Jato d'agua(Nível 3)!".format(self))
                return None

        if self.tipo == 'Água' and self.level >= 57:
            self.magias.append("Jato d'agua(Nivel4)")
            if levelUp == True:
                print("{} aprendeu Jato d'agua(Nível 4)!".format(self))
                return None

        if self.tipo == 'Água' and self.level >= 72:
            self.magias.append("Cura(Nivel3)")
            if levelUp == True:
                print("{} aprendeu Cura (Nível 3)!".format(self))
                return None

        if self.tipo == 'Água' and self.level >= 91:
            self.magias.append("Jato d'agua(Nivel5)")
            if levelUp == True:
                print("{} aprendeu Jato d'agua(Nível 5)!".format(self))
                return None

        #Tipo Pedra
        if self.tipo == 'Pedra' and self.level >= 11:
            self.magias.append('Avalanche de Pedra(Nível 2)')
            if levelUp == True:
                print("{} aprendeu Avalanche de Pedra(Nível 2)!".format(self))
                return None

        if self.tipo == 'Pedra' and self.level >= 24:
            self.magias.append('Avalanche de Pedra(Nível 3)')
            if levelUp == True:
                print("{} aprendeu Avalanche de Pedra(Nível 3)!".format(self))
                return None

        if self.tipo == 'Pedra' and self.level >= 38:
            self.magias.append('Avalanche de Pedra(Nível 4)')
            if levelUp == True:
                print("{} aprendeu Avalanche de Pedra(Nível 4)!".format(self))
                return None

        if self.tipo == 'Pedra' and self.level >= 45:
            self.magias.append('Cura(Nível 1)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 1)!".format(self))
                return None

        if self.tipo == 'Pedra' and self.level >= 56:
            self.magias.append('Avalanche de Pedra(Nível 5)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 1)!".format(self))
                return None

        if self.tipo == 'Pedra' and self.level >= 78:
            self.magias.append('Cura(Nível 2)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 2)!".format(self))
                return None

        if self.tipo == 'Pedra' and self.level >= 89:
            self.magias.append('Avalanche de Pedra(Nivel 6)')
            if levelUp == True:
                print("{} aprendeu Avalanche de Pedra(Nível 6)!".format(self))
                return None

        #Tipo Fogo         
        if self.tipo == 'Fogo' and self.level >= 22:
            self.magias.append('Bola de Fogo(Nível 2)')
            if levelUp == True:
                print("{} aprendeu Bola de Fogo(Nível 2)!".format(self))
                return None

        if self.tipo == 'Fogo' and self.level >= 34:
            self.magias.append('Cura(Nível 1)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 1)!".format(self))
                return None

        if self.tipo == 'Fogo' and self.level >= 41:
            self.magias.append('Bola de Fogo(Nível 3)')
            if levelUp == True:
                print("{} aprendeu Bola de Fogo(Nível 3)!".format(self))
                return None

        if self.tipo == 'Fogo' and self.level >= 53:
            self.magias.append('Cura(Nível 2)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 2)!".format(self))
                return None

        if self.tipo == 'Fogo' and self.level >= 69:
            self.magias.append('Bola de Fogo(Nível 4)')
            if levelUp == True:
                print("{} aprendeu Bola de Fogo(Nível 4)!".format(self))
            return None

        if self.tipo == 'Fogo' and self.level >= 79:
            self.magias.append('Cura(Nível 3)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 3)!".format(self))
            return None

        if self.tipo == 'Fogo' and self.level >= 87:
            self.magias.append('Bola de Fogo(Nível 5')
            if levelUp == True:
                print("{} aprendeu Bola de Fogo(Nível 5)!".format(self))
            return None

        #Tipo Planta
        if self.tipo == 'Planta' and self.level >= 11:
            self.magias.append('Cura(Nivel1)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível1)!".format(self))
                return None

        if self.tipo == 'Planta' and self.level >= 21:
            self.magias.append('Folhas Cortantes(Nivel 2)')
            if levelUp == True:
                print("{} aprendeu Folhas Cortantes(Nível 2)!".format(self))
                return None

        if self.tipo == 'Planta' and self.level >= 34:
            self.magias.append('Cura(Nivel 2)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 2)!".format(self))
                return None

        if self.tipo == 'Planta' and self.level >= 42:
            self.magias.append('Folhas Cortantes(Nivel 3)')
            if levelUp == True:
                print("{} aprendeu Folhas Cortantes(Nível 3)!".format(self))
                return None

        if self.tipo == 'Planta' and self.level >= 56:
            self.magias.append('Cura(Nivel 3)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 3)!".format(self))
                return None


        if self.tipo == 'Planta' and self.level >= 69:
            self.magias.append('Folhas Cortantes(Nivel 4)')
            if levelUp == True:
                print("{} aprendeu Folhas Cortantes(Nível 4)!".format(self))
                return None


        if self.tipo == 'Planta' and self.level >= 78:
            self.magias.append('Folhas Cortantes(Nivel 5)')
            if levelUp == True:
                print("{} aprendeu Folhas Cortantes(Nível 5)!".format(self))
                return None

        if self.tipo == 'Planta' and self.level >= 78:
            self.magias.append('Cura(Nivel 4)')
            if levelUp == True:
                print("{} aprendeu Cura(Nível 4)!".format(self))
                return None

    def vantagens_e_desvantagens(self, pokemon):
        if self.tipo == 'Elétrico' and pokemon.tipo == 'Pedra':
            ataque_efetivo = int(self.ataque * random.random() * 1.1)
            return ataque_efetivo
        elif self.tipo == 'Elétrico' and pokemon.tipo == 'Água' or pokemon.tipo == 'Planta':
            ataque_efetivo = int(self.ataque * random.random() * 1.5)
            return ataque_efetivo
    
        if self.tipo == 'Fogo' and pokemon.tipo == 'Água':
            ataque_efetivo = int(self.ataque * random.random() * 1.1)
            return ataque_efetivo
        elif self.tipo == 'Fogo' and pokemon.tipo == 'Planta' or pokemon.tipo == 'Elétrico':
            ataque_efetivo = int(self.ataque * random.random() * 1.5)
            return ataque_efetivo

        if self.tipo == 'Água' and pokemon.tipo == 'Elétrico':
            ataque_efetivo = int(self.ataque * random.random() * 1.1)
            return ataque_efetivo
        elif self.tipo == 'Água' and pokemon.tipo == 'Fogo' or pokemon.tipo == 'Pedra':
            ataque_efetivo = int(self.ataque * random.random() * 1.5)
            return ataque_efetivo

        if self.tipo == 'Planta' and pokemon.tipo == 'Elétrico':
            ataque_efetivo = int(self.ataque * random.random() * 1.1)
            return ataque_efetivo
        elif self.tipo == 'Planta' and pokemon.tipo == 'Água' or pokemon.tipo == 'Pedra':
            ataque_efetivo = int(self.ataque * random.random() * 1.5)
            return ataque_efetivo

        if self.tipo == 'Pedra' and pokemon.tipo == 'Água':
            ataque_efetivo = int(self.ataque * random.random() * 1.1)
            return ataque_efetivo
        elif self.tipo == 'Pedra' and pokemon.tipo == 'Fogo' or pokemon.tipo == 'Elétrico':
            ataque_efetivo = int(self.ataque * random.random() * 1.5)
            return ataque_efetivo

        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        return ataque_efetivo

    def atacar(self, pokemon):
        ataque_efetivo = self.vantagens_e_desvantagens(pokemon)
        

        pokemon.vida = pokemon.vida - ataque_efetivo
        print("{} perdeu {} pontos de vida!".format(pokemon, ataque_efetivo))
        

        if pokemon.vida <= 0:
            return True
        

    def proximoLevel(self, xp):
        self.xp += xp;
        proximolevel = self.level * 6 * self.level
        if self.xp >= proximolevel:
            self.level += 1
            print("Pokemon {} subiu para o level {}!!".format(self, self.level))
            return True
        else:
            return False

    def recuperar(self):
        self.mp = self.mp = self.level * 4 - 2
        self.vida = self.level * 10

    def infos(self):
        print("-----------------------------------")
        print("             STATUS              ")
        print("-----------------------------------")
        print(self)
        print("\nTipo: {}".format(self.tipo))
        if self.tipo == 'Elétrico':
            print("Forte contra Água e Planta!")
            print("Fraco contra Pedra")
        elif self.tipo == 'Fogo':
            print("Forte contra Planta e Elétrico")
            print("Fraco contra Água")
        elif self.tipo == "Água":
            print("Forte contra Fogo e Pedra")
            print("Fraco contra Elétrico")
        elif self.tipo == 'Planta':
            print("Forte contra Água e Pedra")
            print("Fraco contra Elétrico")
        elif self.tipo == 'Pedra':
            print("Forte contra Fogo e Elétrico")
            print("Fraco contra Água")
       

        print("\nLevel: {}".format(self.level))
        print("XP: {}".format(self.xp))
        proximolevel = self.level * 6 * self.level
        print("Próximo Level: {}".format(proximolevel))

        print("\nHP Máximo: {}".format(self.vida))
        print("MP Máximo: {}".format(self.level * 4 - 2))

        print("\nMagias")
        for magia in self.magias:
            print("{}".format(magia))

    def especial1(self, pokemon):
        if self.tipo == 'Elétrico':
           self.atacarRaioTrovao(pokemon, 1)
        elif self.tipo == 'Fogo':
            self.atacarBolaFogo(pokemon, 1)
        elif self.tipo == 'Água':
            self.atacarJatoAgua(pokemon, 1)
        elif self.tipo == 'Pedra':
            self.atacarAvalanche(pokemon,1)
        elif self.tipo == 'Planta':
            self.atacarFolhasCortantes(pokemon,1)
        if pokemon.vida <= 0:
            return True
        else:
            return False

    def especial2(self, pokemon):
        if self.tipo == 'Elétrico':
           self.atacarRaioTrovao(pokemon, 2)
        elif self.tipo == 'Fogo':
            self.atacarBolaFogo(pokemon, 2)
        elif self.tipo == 'Água':
            self.cura(1)
        elif self.tipo == 'Pedra':
            self.atacarAvalanche(pokemon,2)
        elif self.tipo == 'Planta':
            self.cura(1)
        if pokemon.vida <= 0:
            return True
        else:
            return False

    def especial3(self, pokemon):
        if self.tipo == 'Elétrico':
           self.cura(2)
        elif self.tipo == 'Fogo':
            self.cura(1)
        elif self.tipo == 'Água':
            self.atacarJatoAgua(pokemon, 2)
        elif self.tipo == 'Pedra':
            self.atacarAvalanche(pokemon,3)
        elif self.tipo == 'Planta':
            self.atacarFolhasCortantes(pokemon, 3)
        if pokemon.vida <= 0:
            return True
        else:
            return False

    def especial4(self, pokemon):
        if self.tipo == 'Elétrico':
           self.atacarRaioTrovao(pokemon, 3)
        elif self.tipo == 'Fogo':
            self.atacarBolaFogo(pokemon, 3)
        elif self.tipo == 'Água':
            self.cura(2)
        elif self.tipo == 'Pedra':
            self.atacarAvalanche(pokemon,4)
        elif self.tipo == 'Planta':
            self.cura(2)
        if pokemon.vida <= 0:
            return True
        else:
            return False

    def especial5(self, pokemon):
        if self.tipo == 'Elétrico':
           self.atacarRaioTrovao(pokemon, 4)
        elif self.tipo == 'Fogo':
            self.cura(2)
        elif self.tipo == 'Água':
            self.atacarJatoAgua(pokemon, 3)
        elif self.tipo == 'Pedra':
            self.cura(1)
        elif self.tipo == 'Planta':
            self.atacarFolhasCortantes(pokemon, 3)
        if pokemon.vida <= 0:
            return True
        else:
            return False
        

    def especial6(self, pokemon):
        if self.tipo == 'Elétrico':
           self.cura(2)
        elif self.tipo == 'Fogo':
            self.atacarBolaFogo(pokemon, 4)
        elif self.tipo == 'Água':
            self.atacarJatoAgua(pokemon, 4)
        elif self.tipo == 'Pedra':
            self.atacarAvalanche(pokemon, 5)
        elif self.tipo == 'Planta':
            self.cura(3)
        if pokemon.vida <= 0:
            return True
        else:
            return False

    def especial7(self, pokemon):
        if self.tipo == 'Elétrico':
           self.atacarRaioTrovao(pokemon,5)
        elif self.tipo == 'Fogo':
            self.cura(3)
        elif self.tipo == 'Água':
            self.cura(3)
        elif self.tipo == 'Pedra':
            self.cura(2)
        elif self.tipo == 'Planta':
            self.atacarFolhasCortantes(pokemon, 4)
        if pokemon.vida <= 0:
            return True
        else:
            return False   

    def especial8(self, pokemon):
        if self.tipo == 'Elétrico':
           self.cura(3)
        elif self.tipo == 'Fogo':
            self.atacarBolaFogo(pokemon, 5)
        elif self.tipo == 'Água':
            self.atacarJatoAgua(pokemon, 5)
        elif self.tipo == 'Pedra':
            self.atacarAvalanche(pokemon, 6)
        elif self.tipo == 'Planta':
            self.atacarFolhasCortantes(pokemon, 5)
        if pokemon.vida <= 0:
            return True
        else:
            return False

    def especial9(self,pokemon):
        self.cura(3)

        return False

class PokemonEletrico(Pokemon):
    tipo = 'Elétrico'

    magias = ['Raio do Trovão']

    def atacar(self, Pokemon):
        print("\n\n{} ({}) atacou com Golpe normal ao {}".format(self.nome, self.tipo, Pokemon))
        return super().atacar(Pokemon)

    def atacarRaioTrovao(self, Pokemon, nivel):
        #especial level 1
        if nivel == 1:
            mp_aperder = 3
            ataque_level = 1.8
        elif nivel == 2:
            mp_aperder = 28
            ataque_level = 2.3
        elif nivel == 3: 
            mp_aperder = 51
            ataque_level = 2.8
        elif nivel == 4:
            mp_aperder = 67
            ataque_level = 3.1
        elif nivel == 5:
            mp_aperder = 79
            ataque_level = 3.4
        
        
        if self.mp >= mp_aperder:
            ataque_efetivo = int(self.ataque * random.random() * ataque_level)
            Pokemon.vida = Pokemon.vida - ataque_efetivo
            print("{} atacou com Raio do Trovão em {}".format(self, Pokemon))
            print("{} perdeu {} pontos de vida!".format(Pokemon, ataque_efetivo))
            self.mp - 2
        else:
            print("MP insuficiente!")

    def cura(self, level):
        if level == 1:
            mp_aperder = 29
            hp_aganhar = self.level * 4
        if level == 2:
            mp_aperder = 91
            hp_aganhar = self.level * 6
        if level == 3:
            mp_aperder = 105
            hp_aganhar = self.level * 8

        if self.mp >= mp_aperder:
            self.mp = self.mp - mp_aperder
            self.vida += hp_aganhar
            print("{} Usou Cura Level {} e recuperou {} pontos de HP!".format(self, level, hp_aganhar))
        else:
            print("MP Insuficiente!")



class PokemonFogo(Pokemon):
    tipo = 'Fogo'

    magias = ['Bola de Fogo']

    def atacar(self, Pokemon):
        print("\n\n{} ({}) atacou com Golpe normal ao {}".format(self.nome, self.tipo, Pokemon))
        return super().atacar(Pokemon)

    def atacarBolaFogo(self, Pokemon, nivel):
        #especial level 1
        if nivel == 1:
            mp_aperder = 3
            ataque_level = 1.8
        elif nivel == 2:
            mp_aperder = 23
            ataque_level = 2.4
        elif nivel == 3:
            mp_aperder = 47
            ataque_level = 2.8
        elif nivel == 4:
            mp_aperder = 59
            ataque_level = 3.1
        elif nivel == 5:
            mp_aperder = 79
            ataque_level = 3.4
       

        if self.mp >= mp_aperder:
            ataque_efetivo = int(self.ataque * random.random() * ataque_level)
            Pokemon.vida = Pokemon.vida - ataque_efetivo
            print("{} atacou com Bola de Fogo em {}".format(self, Pokemon))
            print("{} perdeu {} pontos de vida!".format(Pokemon, ataque_efetivo))
            self.mp - 2
        else:
            print("MP insuficiente!")

    def cura(self, level):
        if level == 1:
            mp_aperder = 38
            hp_aganhar = self.level * 4
        if level == 2:
            mp_aperder = 97
            hp_aganhar = self.level * 6
        if level == 3:
            mp_aperder = 110
            hp_aganhar = self.level * 7
        

        if self.mp >= mp_aperder:
            self.mp = self.mp - mp_aperder
            self.vida += hp_aganhar
            print("{} Usou Cura Level {} e recuperou {} pontos de HP!".format(self, level, hp_aganhar))
        else:
            print("MP Insuficiente!")

class PokemonAgua(Pokemon):
    tipo = 'Água'

    magias = ["Jato d'agua"]

    def atacar(self, Pokemon):
        print("\n\n{} ({}) atacou com Golpe normal ao {}".format(self.nome, self.tipo, Pokemon))
        return super().atacar(Pokemon)

    def atacarJatoAgua(self, Pokemon, nivel):
        #especial level 1
        if nivel == 1:
            mp_aperder = 3
            ataque_level = 1.8
        elif nivel == 2:
            mp_aperder = 23
            ataque_level = 2.3
        elif nivel == 3:
            mp_aperder = 47
            ataque_level = 2.8
        elif nivel == 4:
            mp_aperder = 59
            ataque_level = 3.0
        elif nivel == 5:
            mp_aperder = 101
            ataque_level = 3.4
        

        if self.mp >= mp_aperder:
            ataque_efetivo = int(self.ataque * random.random() * ataque_level)
            Pokemon.vida = Pokemon.vida - ataque_efetivo
            print("{} atacou com Jato d'agua em {}".format(self, Pokemon))
            print("{} perdeu {} pontos de vida!".format(Pokemon, ataque_efetivo))
            self.mp - 2
        else:
            print("MP insuficiente!")

    def cura(self, level):
        if level == 1:
            mp_aperder = 24
            hp_aganhar = self.level * 4
        if level == 2:
            mp_aperder = 44
            hp_aganhar = self.level * 6
        if level == 3:
            mp_aperder = 96
            hp_aganhar = self.level * 8

        if self.mp >= mp_aperder:
            self.mp = self.mp - mp_aperder
            self.vida += hp_aganhar
            print("{} Usou Cura Level {} e recuperou {} pontos de HP!".format(self, level, hp_aganhar))
        else:
            print("MP Insuficiente!")

class PokemonPedra(Pokemon):
    tipo = 'Pedra'

    magias = ['Avalanche de Pedra']

    def atacar(self, Pokemon):
        print("\n\n{} ({}) atacou com Golpe normal ao {}".format(self.nome, self.tipo, Pokemon))
        return super().atacar(Pokemon)

    def atacarAvalanche(self, Pokemon, nivel):
        #especial level 1,2
        if nivel == 1:
            mp_aperder = 3
            ataque_level = 1.8
        elif nivel == 2:
            mp_aperder = 23
            ataque_level = 2.5
        elif nivel == 3:
            mp_aperder = 47
            ataque_level = 2.8
        elif nivel == 4:
            mp_aperder = 59
            ataque_level = 3.1
        elif nivel == 5:
            mp_aperder = 71
            ataque_level = 3.4
        elif nivel == 6:
            mp_aperder = 110
            ataque_level = 3.7
        

        if self.mp >= mp_aperder:
            ataque_efetivo = int(self.ataque * random.random() * ataque_level)
            Pokemon.vida = Pokemon.vida - ataque_efetivo
            print("{} atacou com Avalanche de pedra em {}".format(self, Pokemon))
            print("{} perdeu {} pontos de vida!".format(Pokemon, ataque_efetivo))
            self.mp -= mp_aperder
        else:
            print("MP insuficiente!")


    def cura(self, level):
        if level == 1:
            mp_aperder = 24
            hp_aganhar = self.level * 4
        if level == 2:
            mp_aperder = 41
            hp_aganhar = self.level * 6
        if level == 3:
            mp_aperder = 180
            hp_aganhar = self.level * 8

        if self.mp >= mp_aperder:
            self.mp = self.mp - mp_aperder
            self.vida += hp_aganhar
            print("{} Usou Cura Level {} e recuperou {} pontos de HP!".format(self, level, hp_aganhar))
        else:
            print("MP Insuficiente!")
        

class PokemonPlanta(Pokemon):
    tipo = 'Planta'

    magias = ['Folhas Cortantes']

    def atacar(self, Pokemon):
        print("\n\n{} ({})  {}".format(self.nome, self.tipo, Pokemon))
        return super().atacar(Pokemon)

    def atacarFolhasCortantes(self, Pokemon, nivel):
        #especial level 1,2,3,4,5
        if nivel == 1:
            mp_aperder = 3
            ataque_level = 1.8
        elif nivel == 2:
            mp_aperder = 23
            ataque_level = 2.2
        elif nivel == 3:
            mp_aperder = 47
            ataque_level = 2.4
        elif nivel == 4:
            mp_aperder = 67
            ataque_level = 3.1
        elif nivel == 5:
            mp_aperder = 71
            ataque_level = 3.3
        
            
        if self.mp >= mp_aperder:
            ataque_efetivo = int(self.ataque * random.random() * ataque_level)
            Pokemon.vida = Pokemon.vida - ataque_efetivo
            print("{} atacou com Folhas cortantes em {}".format(self, Pokemon))
            print("{} perdeu {} pontos de vida!".format(Pokemon, ataque_efetivo))
            self.mp - 2
        else:
            print("MP insuficiente!")

    def cura(self, level):
        if level == 1:
            mp_aperder = 21
            hp_aganhar = self.level * 4
        if level == 2:
            mp_aperder = 41
            hp_aganhar = self.level * 6
        if level == 3:
            mp_aperder = 68
            hp_aganhar = self.level * 8
        if level == 4:
            mp_aperder = 140
            hp_aganhar = self.level * 10

        self.mp = self.mp - mp_aperder
        self.vida += hp_aganhar
        print("{} Usou Cura Level {} e recuperou {} pontos de HP!".format(self, level, hp_aganhar))
        