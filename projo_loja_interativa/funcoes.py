from time import sleep

def listar(mercadorias):
    for codigo,produto in mercadorias.items():
        print(f"CODIGO       : {codigo}")
        print(f"NOME         : {produto['nome']}")
        print(f"FABRICADO POR: {produto['fabricante']} ")
        print(f"PREÇO        : {produto['v']} R$")
        print('-'*30 )
        sleep(1)

def cadastrar(mercadorias):
        codigo= input('Digite o CODIGO: ').upper()
        nome= input ('Digte o nome do PRODUTO: ')
        fabricante=input("Digite o FABRICANTE do produto: ")
        v=float(input('Digite o PREÇO: '))
        print('-'*42)
        print("\033[1;92mCADASTRADA COM SUCESSO!!!\033[m")
        print('-'*42)
        mercadorias[codigo]= {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'v': v
       }
        sleep(1)

def apagar(codigo,mercadorias):
    if codigo in mercadorias :
        mercadorias.pop(codigo)
        print('-'*42)
        print('\033[1;92mSua mercadoria foi removida com sucesso!\033[m')
        print('-'*42)
        sleep(2)
    else:
        print('-'*42)
        print('\033[1;31mEste codigo não existe!\033[m')
        print('-'*42)
        sleep(2)

def localizar(mercadorias, codigo):
    if codigo in mercadorias:
        print('-'*42)
        print("\033[1;92mSEU PRODUTO FOI LOCALIZADO COM SUCESSO!!!\033[m")
        print('-'*42) 
        print(mercadorias[codigo])
        sleep(1)
        
    else:
        print('-'*42)
        print('\033[1;31mESTE CODIGO NÃO EXISTE!')
        print(          'TENTE NOVAMENTE!\033[m')
        print('-'*42)
        sleep(1)

def alterar(mercadorias, codigo,):
    if codigo in mercadorias :
        novo_nome=input ('Digte o novo NOME do produto: ')
        novo_fabricante=input('Digite o novo FABRICANTE do produto: ')
        novo_v=float(input('Digite o novo PREÇO: '))
        mercadorias[codigo] = {  
        'nome': novo_nome,
        'fabricante': novo_fabricante,
        'v': novo_v
        }  
        print('-'*42)
        print('\033[1;92mSeu PRODUTO foi alterada com sucesso!\033[m')
        print('-'*42)
        sleep(2)
    else:
        print('-'*42)
        print('\033[1;31mEste codigo não existe!\033[m')
        print('-'*42)
        sleep(2)


        
             

    
