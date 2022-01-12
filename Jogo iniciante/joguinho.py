import pygame
pygame.init()
x=100
y=100
velocidade= 15

carro = pygame.image.load("data/carro.PNG")
pista = pygame.image.load("data/pista.PNG")

janela= pygame.display.set_mode((851,700))
pygame.display.set_caption("JOGO EM PYTHON")


janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            janela_aberta = False
        comandos = pygame.key.get_pressed()
    if comandos [pygame.K_UP]:
            y-=velocidade
    if comandos [pygame.K_UP]:
            y-=velocidade
    if comandos[pygame.K_DOWN]:
            y+=velocidade    
    if comandos[pygame.K_RIGHT]:
            x+=velocidade
    if comandos[pygame.K_LEFT]:
            x-=velocidade
      

    janela.blit(pista,(0,0))
    janela.blit(carro,(x,y))
    pygame.display.update()

pygame.quit
    
