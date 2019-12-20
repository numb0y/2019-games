import pygame
from random import randint
pygame.init()
x = 300
y = 100
pos_x = 130
pos_y = 800
pos_y_a = 800
pos_y_c = 800
timer = 0
tempo_segundo = 0


velocidade = 15
velocidade_outros = 18
fundo = pygame.image.load('telad.png')
carro = pygame.image.load('personagem.png')
pedra = pygame.image.load('inimigo1.png')
golem = pygame.image.load('inimigo2.png')
leviathan = pygame.image.load('inimigo3.png')

font = pygame.font.SysFont ('arial black',30)
texto = font.render("Score: ",True,(255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Catch the Frog!")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x<= 520:
        x += velocidade
    if comandos[pygame.K_LEFT] and x>= 80:
        x -= velocidade

    if (pos_y <= -180) and (pos_y_a <= -180) and (pos_y_c <= 180):
        pos_y = randint(800,2000)
        pos_y_a = randint(800,2000)
        pos_y_c = randint(800,2000)

    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("Score: "+str(tempo_segundo), True,(255,255,255), (0,0,0))
        tempo = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_c -= velocidade_outros +10

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(pedra,(pos_x,pos_y))
    janela.blit(golem,(pos_x + 170, pos_y_a))
    janela.blit(leviathan,(pos_x +350, pos_y_c))
    janela.blit(texto,pos_texto)
    pygame.display.update()

pygame.quit()