import pygame

pygame.init()

TELA_LARGURA = 800
TELA_ALTURA = int(TELA_LARGURA * 0.8)

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("JOGO EM PYGAME")

class Soldado(pygame.sprite.Sprite):
    def __init__(self, x,y,scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/jogador/jogador_img/0.png')
        self.img = pygame.transform.scale(img, int((img.get_width() * scale, img.get_height()*scale)))
        self.rect = img.get_rect()
        self.rect.center = (x, y)

jogador = Soldado(200, 200, 3)

jogador = Soldado(500, 200, 3)



run = True

while run:
    tela.blit(jogador.img, jogador.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.QUIT