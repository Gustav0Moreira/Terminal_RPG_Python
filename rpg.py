import random
import time
import math


class Player(object):
    def __init__(self, name, attack, hp_base, defense, agil):
        self.name = name
        self.attack = attack
        self.hp_base = hp_base
        self.defense = defense
        self.agil = agil


    def Dano_vida(self, dano):
        atual_hp = dano - self.hp_base
        return atual_hp
        

    def Status(self):
        print("""
              Status do Personagem:
              -----------------
              HP: %s
              Nome: %s
              Ataque: %s
              Defesa: %s
              Agilidade %s
              """ %(self.hp_base, self.name, self.attack, self.defense, self.agil))
    
    def Curar(self, bonus):
        
        if self.hp_base > cura:
            cura = bonus + self.hp
        return cura


    def Atacar(self, bonus):
        dano = bonus + self.attack
        return dano


class Enemy(Player):
    def __init__(self, name, attack, hp_base, defense, agil):
        return super().__init__(name, attack, hp_base, defense, agil)
        

def Dado():
    valor = random.randint(1,6)
    return valor

def Criar_Personagem():
    def Nome():

        control_menu = True
        main_nome = None
        lista_nome = ["Ronaldo", "Marculino", "Jonesys", "Astrogilda", "Leticia", "Rafaelo", "Luatico", "Linque", "Met", "Wickedy", "Nomono", "Bubu", "Finn", "Jaquilon", "Joann'na", "Marry", "Moray"]
        lista_sobrenome = ["Don II", "Caçadará", "Imperios", "Iconbus", "Amoreira", "Pau Ferro", "Terere", "Desconcos", "Bayano", "Pitiro", "Encorus", "Def's", "Oxrius", "Dedede", "O'lladel", "Parokus", "Ultimos"]
        lista_vulgos = ["Chanceler do Governo", "Pé de Ganso", "Sulista Amador(a)", "Imperador(a) de Nulo", "Guerreiro(a) Teimoso", "Destruidor(a) de Esperança", "Criador(a) de Mundos", "Desbravador(a) de Lagos", "Peixe do Mar", "Arauto(a) de Somnus", "Ancião do Desconhecido", "Titulo de Nepotismo", "Anarquista Institucional", "Escriba de Cobra", "Lobo(a) Amigável", "Amigo(a) Imaginário(a)", "Negociador(a) Humilde"]
        frase_criador = ["Ei, esse é um bom nome! Já escutei ele em algum lugar", "Não sei se deveriamos usar este...", "Você já leu HP Lovecraft?", "Agora sim! Perfeito! Bravo!", "Eu não sou muito fã deste, mas se você gosta...", "Esse nome é incrível! Tenho certeza que você vai conquistar o mundo!", "Há muito tempo eu não escutava este nome... Bem-vindo de volta!", "Eu não vejo problema neste nome... Só não sai falando alto por aí", "Tente algo mais charmoso!" ,"Ei, acho que somos primos! Você tem uma tia chamada Astrogilda?", "Eu já tive um cachorro com este nome.", "POR FAVOR, troque este nome... Se você quiser..."]

        while control_menu:
            try:
                criar_nome = int(input("1 - Escolher um nome próprio\n2 - Gerar nome aleatório: \n"))
            except ValueError:
                print("Digite um número entre 1 e 2, por gentileza...")
            except Exception as error:
                print(error)
                print("Ação não permitida...")
            else:
                if criar_nome == 1:
                    control_menu2 = True
                    base_nome = input("Nome: ")
                    while control_menu2:
                        try:
                            control_decisao = int(input("Seu nome é '%s'?:\n1 - Sim\n2 - Não\n" %(base_nome)))
                        except ValueError:
                            print("Digite um número entre 1 e 2, por gentileza...")
                        except Exception as error2:
                            print(error2)
                            print("Ação não permitida...")
                        else:
                            if control_decisao ==  1:
                                print("Bem-Vindo ao mundo %s" %(base_nome))
                                control_menu = False
                                control_menu2 = False
                                main_nome = base_nome
                            elif control_decisao == 2:
                                print("Vamos começar de novo!")
                                control_menu2 = False
                            else:
                                print("Digite um número válido")
                elif criar_nome == 2:
                    control_menu3 = True
                    
                    while control_menu3:
                        control_menu4 = True

                        base_nome_aleatorio = lista_nome[random.randint(0,16)]
                        base_sobrenome_aleatorio = lista_sobrenome[random.randint(0,16)]
                        base_vulgo_aleatorio = lista_vulgos[random.randint(0,16)]
                        base_aleatorio = ("%s %s o(a) %s" %(base_nome_aleatorio, base_sobrenome_aleatorio, base_vulgo_aleatorio))
                        print("Seu nome aleatório será gerado, aguarde um momento...")
                        time.sleep(3)
                        print("""
                                            -------------------
                                                SEU NOME É...
                                            -------------------
                                    (%s)
                            
                            Criador: 
                                - %s 
                            
                            """ %(base_aleatorio, frase_criador[random.randint(0, 10)]))
                        
                        while control_menu4:
                            try:
                                decisao_aleatorio = int(input("Está de acordo com seu novo nome?: \n1 - Sim, maravilhoso!\n2 - NÃO, me deixe escolher outro.\n3 - Acho melhor eu escolher um nome próprio...\n"))
                            except ValueError:
                                print("Digite um número entre 1, 2 ou 3, por gentileza...")
                            except Exception as error3:
                                print(error3)
                                print("Ação não permitida...")
                            else:
                                if decisao_aleatorio == 1:
                                    print("Bem-Vindo ao mundo %s" %(base_aleatorio))
                                    main_nome = base_aleatorio
                                    control_menu = False
                                    control_menu3 = False
                                    control_menu4 = False
                                elif decisao_aleatorio == 2:
                                    print("Que pena! Vamos gerar outro nome...")
                                    control_menu4 = False
                                    time.sleep(3)
                                elif decisao_aleatorio == 3:
                                    print("Também acho... Vamos voltar ao menu inicial...")
                                    control_menu3 = False
                                    control_menu4 = False
                                    time.sleep(3)
                                else:
                                    print("Digite um número válido")
        return main_nome                    

    def Skills():
        print("Agora será rolado 3 valores, em seguida, você poderá decidir se manterá o rolamento atual ou se solicitará um novo rolamento.\nOBS: Lembre-se que você ainda terá 6 pontos para distribuir entre estes rolamentos")
        time.sleep(3)
        control_menu = True
        while control_menu:
            control_menu2 = True
            dado1 = Dado()
            dado2 = Dado()
            dado3 = Dado()
            lista_dados = [dado1, dado2, dado3]
            print("Vamos começar os rolamentos")
            for i in lista_dados:
                print("Gerando o dado...")
                time.sleep(1)
                print("""
                        ----------
                        |        |
                        |   %s    |
                        |        |
                        ----------
                      
                      """ %(i))
                time.sleep(1)
            while control_menu2:
                print("""Seus valores gerados: 
                      Dado 1: %s
                      
                      Dado 2: %s

                      Dado 3: %s

                      """ %(dado1, dado2, dado3))
                try:
                    decisao_dado = int(input("Você está de acordo com os valores gerados?:\n1 - Sim, vamos prosseguir!\n2 - Não, quero rolar novamente\n"))
                except ValueError:
                    print("Digite entre 1 ou 2.")
                except Exception as error:
                    print(error)
                    print("Ação inválida.")
                else:
                    if decisao_dado == 1:
                        print("Que bom! Vamos prosseguir com a atribuição dos valores")
                        control_menu = False
                        control_menu2 = False
                        time.sleep(3)
                    elif decisao_dado == 2:
                        print("Sem problema, vamos gerar novamente!")
                        control_menu2 = False
                        time.sleep(1)
                    else:
                        print("Valor inválido, vamos tentar novamente.")
        

    Skills()

    print("""
                                -------------------
                                CRIE SEU PERSONAGEM
                                -------------------
            Seu personagem é constituido de 4 informações, sendo:
            -Pontos de Vida
            -Ataque
            -Defesa
            -Agilidade
            
            Estes atributos são definidos através da rolagem de números
            aleatórios de 1 a 6 e o complemento de 6 pontos divisiveis para agregar no total.
            Antes de começarmos, escolha o nome do seu personagem:
            """)
    
    nome = Nome()

    print("""
                                -------------------
                                 ROLANDO ATRIBUTOS
                                -------------------
            Agora vamos rolar seus 3 atributos de habilidades, sendo eles:
            -Ataque (Será utilizado para definir o valor de seu dano, somando mais ao bonus de armas que você utilizar)
            -Defesa (Será utilizado para definir o valor de sua esquiva ao ser atacado, somando mais ao bonus de armaduras que utilizar)
            -Agilidade (Será utilizado para definir a ordem de ação em combante, somando mais ao bonus de itens que utilizar)
          
            No final, seus Pontos de Vida serão definidos pela média de seus atributos mais 10 pontos.


          """)

        
                
 

    ponto_bonus = 8
    base_ataque = None
    base_defesa = None
    base_agili = None

Criar_Personagem()
    

