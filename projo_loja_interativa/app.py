from funcoes import listar
from funcoes import*
print("\033[7;112m""*"*36)
print("*****BEM VINDO AO SHOOP DO JOAO*****")
print("*"*36)

menu = '''\033[m
[1] Lista de produto
[2] Cadastrar produtos
[3] Excluir produtos
[4] Localizar produtos pelo codigo
[5] Alterar produtos

[X] Aperte X para sair do programa.

Qual sua opção: '''
mercadorias = {
'P01'  : {
        'nome':'Pão',              #nome= nome do produto
        'fabricante': "Padeiro",      #data= data de registro do produto
        'v': 0.25,                 #v= variavel declarada para o valor da mercadoria
        
    },
    'ABC':{
        'nome':'Celular',
        'fabricante': "NOKIA",
         'v':100.99,
    }
 }
while True:
    opcao= input(menu).upper() #Criando opção para sair do progama
    if opcao=='X':
        print("\n\033[1;92mVOCÊ SAIU DO PROGAMA, ATÉ MAIS!.\033[m")
        break
    elif opcao == '1': #Criando opção para lista de produtos do progama
        print('='*50)
        print('='*15,"LISTA DE PRODUTOS",'='*16)
        print('='*50)
        listar(mercadorias)

    elif opcao=='2': #Criando opção para adicionar produtos ao progama
        print('='*50)
        print('='*15,"CADASTRAR PRODUTOS",'='*15)
        print('='*50)
        cadastrar(mercadorias)
   
    elif opcao=='3': #Criando opção para remover produtos do progama
        codigo= input('Digite o codigo do PRODUTO voce deseja excluir: ').upper()
        apagar(codigo,mercadorias)

    elif opcao=='4': #Criando opção para localizar produtos do progama
        codigo= input('Digite o codigo do PRODUTO que voce deseja localizar: ').upper()
        localizar(mercadorias, codigo)
  
    elif opcao=='5': #Criando opção para alterar produtos do progama
        codigo = input('Digite o codigo do produto que voce deseja alterar: ').upper()
        alterar(mercadorias, codigo)
    else:
        print('\033[1;31mTente novamente seu comando nao foi reconhecido!\033[m')

        