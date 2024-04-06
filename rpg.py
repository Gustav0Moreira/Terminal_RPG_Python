import random
import time
import math


class Player(object):
    def __init__(self, hp_base, name, attack, defense, agil):
        self.hp_base = hp_base
        

        self.name = name
        self.attack = attack
        
        self.defense = defense
        self.agil = agil


    def Dano_vida(self, hp, dano, shield):
        sh_dano = int(dano - shield)
        atual_hp = int(hp - sh_dano )
        return atual_hp
        

    def Status(self, a, hp):
        self.hp = hp

        if a == 1:
            print("""
                Status do Personagem:
                -----------------
                HP: %s/%s
                Nome: %s
                Ataque: %s
                Defesa: %s
                Agilidade %s
                """ %(self.hp, self.hp_base, self.name, self.attack, self.defense, self.agil))
        elif a == 2:
            print("""
                Status do Personagem:
                -----------------
                HP: %s/%s
                Nome: %s
                """ %(self.hp, self.hp_base, self.name))
        else:
            print("Opção inválida")
    
    def Curar(self, bonus):
        
        if self.hp_base > cura:
            cura = bonus + self.hp
        return cura


    def Atacar(self):
        dano = self.attack
        return dano


class Enemy(Player):
    def __init__(self, name, attack, hp_base, defense, agil):
        return super().__init__(name, attack, hp_base, defense, agil)
        

def Dado():
    valor = random.randint(1,6)
    return valor

def Criar_Personagem():
    def Nome():
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
            aleatórios de 1 a 6.
            Antes de começarmos, escolha o nome do seu personagem:
            """)
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
        print("""
                                -------------------
                                 ROLANDO ATRIBUTOS
                                -------------------
            Agora vamos rolar seus 3 atributos de habilidades, sendo eles:
            -Ataque
              (Será utilizado para definir o valor de seu dano, somando mais ao bonus de armas que você utilizar).

            -Defesa 
              (Será utilizado para definir o valor de sua esquiva ao ser atacado, somando mais ao bonus de armaduras que utilizar).

            -Agilidade 
              (Será utilizado para definir a ordem de ação em combante, somando mais ao bonus de itens que utilizar).
          
            No final, seus Pontos de Vida serão definidos pela média de seus atributos mais 10 pontos.


          """)
        print("Agora será rolado 3 valores, em seguida, você poderá decidir se manterá o rolamento atual ou se solicitará um novo rolamento.")
        time.sleep(3)
        control_menu = True
        control_menu3 = True
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
                        -----------
                        |         |
                        |    %s    |
                        |         |
                        -----------
                      
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
        print("Vamos atribuir os valores para seus atributos:")
        while control_menu3:
            lock_test = False
            dic_atributos = {
            "ataque" : None,
            "defesa" : None,
            "agilidade" : None,
            "pontos de vida" : None
            }
            try:
                decisao_atributo = int(input("O primeiro rolamento (%s) vai para qual atributo?: \n1 - Ataque\n2 - Defesa\n3 - Agilidade\n" %(lista_dados[0])))
            except ValueError: 
                print("Digite um número entre 1,2 ou 3")
            except Exception as error2:
                print(error2) 
                print("Ação inválida")
            else:
                if decisao_atributo == 1:
                    dic_atributos["ataque"] = lista_dados[0]
                    print("Ataque = %s" %(dic_atributos["ataque"]))
                    try:
                        decisao_atributo2 = int(input("O segundo rolamento (%s) vai para qual atributo?: \n1 - Defesa\n2 - Agilidade\n"%(lista_dados[1])) )
                    except ValueError: 
                        print("Digite um número entre 1 ou 2")
                    except Exception as error3:
                        print(error3) 
                        print("Ação inválida")
                    else:
                        if decisao_atributo2 == 1:
                            dic_atributos["defesa"] = lista_dados[1]
                            dic_atributos["agilidade"] = lista_dados[2]
                            print("Defesa = %s" %(dic_atributos["defesa"]))
                            time.sleep(1)
                            print("O terceiro dado foi atribuido a Agilidade")
                            print("Agilidade = %s" %(dic_atributos["agilidade"]))
                        elif decisao_atributo2 == 2:
                            dic_atributos["agilidade"] = lista_dados[1]
                            dic_atributos["defesa"] = lista_dados[2]
                            print("Agilidade = %s" %(dic_atributos["agilidade"]))
                            time.sleep(1)
                            print("O terceiro dado foi atribuido a Defesa")
                            print("Defesa = %s" %(dic_atributos["defesa"]))
                        else:
                            print("Valor inválido")
                elif decisao_atributo == 2:
                    dic_atributos["defesa"] = lista_dados[0]
                    print("Defesa = %s" %(dic_atributos["defesa"]))
                    try:
                        decisao_atributo2 = int(input("O segundo rolamento (%s) vai para qual atributo?: \n1 - Ataque\n2 - Agilidade\n" %(lista_dados[1])) )
                    except ValueError: 
                        print("Digite um número entre 1 ou 2")
                    except Exception as error3:
                        print(error3) 
                        print("Ação inválida")
                    else:
                        if decisao_atributo2 == 1:
                            dic_atributos["ataque"] = lista_dados[1]
                            dic_atributos["agilidade"] = lista_dados[2]
                            print("Ataque = %s" %(dic_atributos["ataque"]))
                            time.sleep(1)
                            print("O terceiro dado foi atribuido a Agilidade")
                            print("Agilidade = %s" %(dic_atributos["agilidade"]))

                        elif decisao_atributo2 == 2:
                            dic_atributos["agilidade"] = lista_dados[1]
                            dic_atributos["ataque"] = lista_dados[2]
                            print("Agilidade = %s" %(dic_atributos["agilidade"]))
                            time.sleep(1)
                            print("O terceiro dado foi atribuido a Ataque")
                            print("Ataque = %s" %(dic_atributos["ataque"]))

                        else:
                            print("Valor inválido")
                elif decisao_atributo == 3:
                    dic_atributos["agilidade"] = lista_dados[0]
                    print("Agilidade = %s" %(dic_atributos["agilidade"]))
                    try:
                        decisao_atributo2 = int(input("O segundo rolamento (%s) vai para qual atributo?: \n1 - Ataque\n2 - Defesa\n" %(lista_dados[1])))
                    except ValueError: 
                        print("Digite um número entre 1 ou 2")
                    except Exception as error3:
                        print(error3) 
                        print("Ação inválida")
                    else:
                        if decisao_atributo2 == 1:
                            dic_atributos["ataque"] = lista_dados[1]
                            dic_atributos["defesa"] = lista_dados[2]
                            print("Ataque = %s" %(dic_atributos["ataque"]))
                            time.sleep(1)
                            print("O terceiro dado foi atribuido a Defesa")
                            print("Defesa = %s" %(dic_atributos["defesa"]))

                        elif decisao_atributo2 == 2:
                            dic_atributos["defesa"] = lista_dados[1]
                            dic_atributos["ataque"] = lista_dados[2]
                            print("Defesa = %s" %(dic_atributos["defesa"]))
                            time.sleep(1)
                            print("O terceiro dado foi atribuido a Ataque")
                            print("Ataque = %s" %(dic_atributos["ataque"]))

                        else:
                            print("Valor inválido")
            try:
                total_pontos_vida = ((dic_atributos["agilidade"] + dic_atributos["ataque"] + dic_atributos["defesa"]) / 3 + 10)
            except TypeError:
                print("Valor inoperante!")
            except Exception:
                print("Ação inválida.")
            else:
                dic_atributos["pontos de vida"] = int(total_pontos_vida)
                print("""
                                    -------------------
                                         RESULTADO 
                                    -------------------
                                Ataque = %s
                                Defesa = %s
                                Agilidade = %s
                                Pontos de Vida = %s
                    
                    """ %(dic_atributos["ataque"], dic_atributos["defesa"], dic_atributos["agilidade"], dic_atributos["pontos de vida"]))
                lock_test = True
            while lock_test:    
                try:
                    decisao_resultado = int(input("Está de acordo com o resultado?:\n1 - Sim, estou satisfeito\n2 - Não, me deixe tentar novamente\n"))
                except ValueError:
                    print("Digite um número entre 1 e 2")
                except Exception as error:
                    print(error)
                    print("Ação Inválida.")
                else:
                    if decisao_resultado == 1:
                        control_menu3 = False
                        lock_test = False
                        control_menu = False
                        time.sleep(3)
                    elif decisao_resultado == 2:
                        print("Certo, vamos atribuir novamente!")
                        lock_test = False
                        time.sleep(3)
                    else:
                        print("Digite um número válido.")
        return dic_atributos
   
    nome = Nome()
    atributos = Skills()
    lista_retorno = [atributos["pontos de vida"], nome, atributos["ataque"], atributos["defesa"], atributos["agilidade"]]
    return lista_retorno



def Menu():
    pass

def Batalha():
    control_batalha = True
    #control_turno = True

    #--/--/--/--/--/--/--Jogador
    p1hp, p1d, p1ag = int(p1.hp_base), p1.defense, p1.agil
    
    #--/--/--/--/--/--/--Inimigo
    lista_nome_inimigo = ["Grogs o Goblin", "Ozi o Slime", "Cacaro o Ladrão", "Licandro o Lobisomem"]
    inimigo = Enemy(random.randint(10,20), lista_nome_inimigo[random.randint(0,3)], random.randint(1,6), random.randint(1,6), random.randint(1,6))
    e1hp, e1d, e1ag = int(inimigo.hp_base), inimigo.defense, inimigo.agil
    escudo_p = 0
    escudo_i = 0
    
    p1.Status(1, p1hp)
    inimigo.Status(1, e1hp)

    print("!---!DESAFIO IMINENTE!---!")
    while control_batalha:
        if p1ag > e1ag:
            print("\n/-/-/-/-Turno do Jogador-/-/-/-/\n")
            try:
                decisao = int(input("\nQual ação deseja efetuar?: \n1 - Atacar \n2 - Defender \n3 - Fugir \n4 - Status\n"))
            except ValueError:
                print("Digite um número entre 1,2 e 3")
            except Exception as error:
                print(error)
                print("Ação inválida")
            else:
                if decisao == 1:
                    print("\nVocê ataca o inimigo e...\n")
                    time.sleep(3)
                    acerto_pj = Dado()
                    if acerto_pj >= e1d:
                        print("\n...Você acerta o inimigo!\n")
                        dano = p1.Atacar()
                        print("\nCausou %s de dano!\n" %(dano))
                        cal_dano_i = inimigo.Dano_vida(e1hp, dano, escudo_i)
                        e1hp = cal_dano_i
                        inimigo.Status(2, e1hp)
                        escudo_i = 0
                        time.sleep(3)
                        if e1hp > 0:
                            print("\n/-/-/-/-Turno do Inimigo-/-/-/-/\n")
                            decisao_inimigo = random.randint(1,2)
                            if decisao_inimigo == 1:
                                time.sleep(1)
                                print("\nO Inimigo ataca você...\n")
                                time.sleep(3)
                                acerto_inimigo = Dado()
                                if acerto_inimigo >= p1d:
                                    print("\n...O inimigo te acerta!\n")
                                    dano_inimigo = inimigo.Atacar()
                                    print("\nCausou %s de dano!\n" %(dano_inimigo))
                                    cal_dano_p = p1.Dano_vida(p1hp, dano_inimigo, escudo_p)
                                    p1hp = cal_dano_p
                                    p1.Status(2, p1hp)
                                    escudo_p = 0
                                    if p1hp <= 0:
                                        time.sleep(1)
                                        print("Seu personagem não aguentou...")
                                        control_batalha = False
                                else:
                                    print("\n...O inimigo não te acerta!\n")
                                    time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\n...O inimigo decide se defender...\n")
                                escudo_i = 5
                                time.sleep(3)
                        else:
                            print("\n!---Vitória do jogador---!\n")
                            control_batalha = False
                    else:
                        print("\n...Você erra o golpe...\n")
                        time.sleep(1)
                        if e1hp > 0:
                            print("\n/-/-/-/-Turno do Inimigo-/-/-/-/\n")
                            decisao_inimigo = random.randint(1,2)
                            if decisao_inimigo == 1:
                                time.sleep(1)
                                print("\nO Inimigo ataca você...\n")
                                time.sleep(3)
                                acerto_inimigo = Dado()
                                if acerto_inimigo >= p1d:
                                    print("\n...O inimigo te acerta!\n")
                                    dano_inimigo = inimigo.Atacar()
                                    print("\nCausou %s de dano!\n" %(dano_inimigo))
                                    cal_dano_p = p1.Dano_vida(p1hp, dano_inimigo, escudo_p)
                                    p1hp = cal_dano_p
                                    p1.Status(2, p1hp)
                                    escudo_p = 0
                                    if p1hp <= 0:
                                        time.sleep(1)
                                        print("Seu personagem não aguentou...")
                                        control_batalha = False
                                else:
                                    print("\n...O inimigo não te acerta!\n")
                                    time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\n...O inimigo decide se defender...\n")
                                escudo_i = 5
                                time.sleep(3)
                        else:
                            print("\n!---Vitória do jogador---!\n")
                            control_batalha = False
                
                elif decisao == 2:
                    time.sleep(1)
                    print("Você se defende...")
                    escudo_p = 5
                    if e1hp > 0:
                            print("\n/-/-/-/-Turno do Inimigo-/-/-/-/\n")
                            decisao_inimigo = random.randint(1,2)
                            if decisao_inimigo == 1:
                                time.sleep(1)
                                print("\nO Inimigo ataca você...\n")
                                time.sleep(3)
                                acerto_inimigo = Dado()
                                if acerto_inimigo >= p1d:
                                    print("\n...O inimigo te acerta!\n")
                                    dano_inimigo = inimigo.Atacar()
                                    print("\nCausou %s de dano!\n" %(dano_inimigo))
                                    cal_dano_p = p1.Dano_vida(p1hp, dano_inimigo, escudo_p)
                                    p1hp = cal_dano_p
                                    p1.Status(2, p1hp)
                                    escudo_p = 0
                                    if p1hp <= 0:
                                        time.sleep(1)
                                        print("Seu personagem não aguentou...")
                                        control_batalha = False
                                else:
                                    print("\n...O inimigo não te acerta!\n")
                                    time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\n...O inimigo decide se defender...\n")
                                escudo_i = 5
                                time.sleep(3)
                    else:
                        print("\n!---Vitória do jogador---!\n")
                        control_batalha = False

                elif decisao == 3:
                    time.sleep(1)
                    print("...Você tenta fugir...")
                    time.sleep(3)
                    fuga_dado = Dado()
                    if fuga_dado >= 4:
                        print("...Você escapa!")
                        control_batalha = False
                    else:
                        print("...Sua fuga falha...")
                        time.sleep(1)

                elif decisao == 4:
                    time.sleep(3)
                    p1.Status(2, p1hp)
                
                else:
                    print("Digite uma opção válida")
        else:
            print("\n/-/-/-/-Turno do Inimigo-/-/-/-/\n")
            decisao_inimigo = random.randint(1,2)
            if decisao_inimigo == 1:
                time.sleep(1)
                print("\nO Inimigo ataca você...\n")
                time.sleep(3)
                acerto_inimigo = Dado()
                if acerto_inimigo >= p1d:
                    print("\n...O inimigo te acerta!\n")
                    dano_inimigo = inimigo.Atacar()
                    print("\nCausou %s de dano!\n" %(dano_inimigo))
                    cal_dano_p = p1.Dano_vida(p1hp, dano_inimigo, escudo_p)
                    p1hp = cal_dano_p
                    p1.Status(2, p1hp)
                    escudo_p = 0
                    if p1hp <= 0:
                        time.sleep(1)
                        print("Seu personagem não aguentou...")
                        control_batalha = False
                    else:
                        print("\n/-/-/-/-Turno do Jogador-/-/-/-/\n")
                        try:
                            decisao = int(input("\nQual ação deseja efetuar?: \n1 - Atacar \n2 - Defender \n3 - Fugir \n4 - Status\n"))
                        except ValueError:
                            print("Digite um número entre 1,2 e 3")
                        except Exception as error:
                            print(error)
                            print("Ação inválida")
                        else:
                            if decisao == 1:
                                print("\nVocê ataca o inimigo e...\n")
                                time.sleep(3)
                                acerto_pj = Dado()
                                if acerto_pj >= e1d:
                                    print("\n...Você acerta o inimigo!\n")
                                    dano = p1.Atacar()
                                    print("\nCausou %s de dano!\n" %(dano))
                                    cal_dano_i = inimigo.Dano_vida(e1hp, dano, escudo_i)
                                    e1hp = cal_dano_i
                                    inimigo.Status(2, e1hp)
                                    escudo_i = 0
                                    time.sleep(3)
                                    if e1hp < 0:
                                        print("\n!---Vitória do jogador---!\n")
                                        control_batalha = False
                                else:
                                    print("\n...Você erra o golpe...\n")
                                    time.sleep(1)
                            elif decisao == 2:
                                time.sleep(1)
                                print("Você se defende...")
                                escudo_p = 5
                            elif decisao == 3:
                                time.sleep(1)
                                print("...Você tenta fugir...")
                                time.sleep(3)
                                fuga_dado = Dado()
                                if fuga_dado >= 4:
                                    print("...Você escapa!")
                                    control_batalha = False
                                else:
                                    print("...Sua fuga falha...")
                                    time.sleep(1)

                            elif decisao == 4:
                                time.sleep(3)
                                p1.Status(2, p1hp)
                            
                            else:
                                print("Digite uma opção válida")
                else:
                    print("\n...O inimigo não te acerta!\n")
                    time.sleep(1)
                    print("\n/-/-/-/-Turno do Jogador-/-/-/-/\n")
                    try:
                        decisao = int(input("\nQual ação deseja efetuar?: \n1 - Atacar \n2 - Defender \n3 - Fugir \n4 - Status\n"))
                    except ValueError:
                        print("Digite um número entre 1,2 e 3")
                    except Exception as error:
                        print(error)
                        print("Ação inválida")
                    else:
                        if decisao == 1:
                            print("\nVocê ataca o inimigo e...\n")
                            time.sleep(3)
                            acerto_pj = Dado()
                            if acerto_pj >= e1d:
                                print("\n...Você acerta o inimigo!\n")
                                dano = p1.Atacar()
                                print("\nCausou %s de dano!\n" %(dano))
                                cal_dano_i = inimigo.Dano_vida(e1hp, dano, escudo_i)
                                e1hp = cal_dano_i
                                inimigo.Status(2, e1hp)
                                escudo_i = 0
                                time.sleep(3)
                                if e1hp < 0:
                                    print("\n!---Vitória do jogador---!\n")
                                    control_batalha = False
                            else:
                                print("\n...Você erra o golpe...\n")
                                time.sleep(1)
                        elif decisao == 2:
                            time.sleep(1)
                            print("Você se defende...")
                            escudo_p = 5
                        elif decisao == 3:
                            time.sleep(1)
                            print("...Você tenta fugir...")
                            time.sleep(3)
                            fuga_dado = Dado()
                            if fuga_dado >= 4:
                                print("...Você escapa!")
                                control_batalha = False
                            else:
                                print("...Sua fuga falha...")
                                time.sleep(1)

                        elif decisao == 4:
                            time.sleep(3)
                            p1.Status(2, p1hp)
                            
                        else:
                            print("Digite uma opção válida")
            else:
                time.sleep(1)
                print("\n...O inimigo decide se defender...\n")
                escudo_i = 5
                time.sleep(3)
                print("\n/-/-/-/-Turno do Jogador-/-/-/-/\n")
                try:
                    decisao = int(input("\nQual ação deseja efetuar?: \n1 - Atacar \n2 - Defender \n3 - Fugir \n4 - Status\n"))
                except ValueError:
                    print("Digite um número entre 1,2 e 3")
                except Exception as error:
                    print(error)
                    print("Ação inválida")
                else:
                    if decisao == 1:
                        print("\nVocê ataca o inimigo e...\n")
                        time.sleep(3)
                        acerto_pj = Dado()
                        if acerto_pj >= e1d:
                            print("\n...Você acerta o inimigo!\n")
                            dano = p1.Atacar()
                            print("\nCausou %s de dano!\n" %(dano))
                            cal_dano_i = inimigo.Dano_vida(e1hp, dano, escudo_i)
                            e1hp = cal_dano_i
                            inimigo.Status(2, e1hp)
                            escudo_i = 0
                            time.sleep(3)
                            if e1hp < 0:
                                print("\n!---Vitória do jogador---!\n")
                                control_batalha = False
                        else:
                            print("\n...Você erra o golpe...\n")
                            time.sleep(1)
                    elif decisao == 2:
                        time.sleep(1)
                        print("Você se defende...")
                        escudo_p = 5
                    elif decisao == 3:
                        time.sleep(1)
                        print("...Você tenta fugir...")
                        time.sleep(3)
                        fuga_dado = Dado()
                        if fuga_dado >= 4:
                            print("...Você escapa!")
                            control_batalha = False
                        else:
                            print("...Sua fuga falha...")
                            time.sleep(1)

                    elif decisao == 4:
                        time.sleep(3)
                        p1.Status(2, p1hp)
                            
                    else:
                        print("Digite uma opção válida")



                            


        


#/--/--/--/--/--/-Criação-de-Personagem-/--/--/--/--/--/    
atributo = Criar_Personagem()
p1 = Player(atributo[0], atributo[1], atributo[2], atributo[3], atributo[4])

Batalha()

#Batalha()

