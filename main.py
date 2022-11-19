import pygame
from random import randint, choice
from pygame import display
from pygame.transform import scale
from pygame.image import load
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE, K_TAB
from pygame.time import Clock

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
pygame.init()

score = 0
disparoTanque = 1
disparoTanquee = 1
disparo = 0
tamanho = 1280, 800  # variável que absorve o tamanho do plano em X e Y
superficie = display.set_mode((tamanho))  # variável que absorve a contrução do plano.
display.set_caption('The Batman')  # funcão que escreve o nome da janela.
done = False
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
fundo = scale(load('images/cidade.jpg'),
              tamanho)  # como a imagem é maior que o plano, usamos a função SCALE para transformar a imagem no tamanho do plano.

fundo2 = scale(load('images/img.png'),
               tamanho)

fundo3 = scale(load('images/img_1.png'),
               tamanho)


class OBatman(Sprite):  # criamos o primeiro sprint que irá compor o jogo, o objeto principal.
    def __init__(self, Arma):
        super().__init__()  # defino essa função será usada em outras classes como herança.

        self.image = load('images/batman.png')  # carrego a imagem e em seguida tranfiro para uma variável.
        self.rect = self.image.get_rect()  # uso a função get_rect na imagem, onde irá me permitir o movimento no plano.
        self.velocidade = 5
        self.Arma = Arma

    def update(self):
        keys = pygame.key.get_pressed()  # recebe o movimento

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidade

    def jogararma(self):
        if len(self.Arma) < 2:
            self.Arma.add(
                Arma(*self.rect.center)
            )


class CarroBatman(Sprite):  # criamos o primeiro sprint que irá compor o jogo, o objeto principal.
    def __init__(self, Armacarro):
        super().__init__()  # defino essa função será usada em outras classes como herança.

        self.image = load('images/batmancar.png')  # carrego a imagem e em seguida tranfiro para uma variável.
        self.rect = self.image.get_rect()  # uso a função get_rect na imagem, onde irá me permitir o movimento no plano.
        self.velocidade = 8
        self.Armacarro = Armacarro

    def update(self):
        keys = pygame.key.get_pressed()  # recebe o movimento

        if keys[pygame.K_a]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_d]:
            self.rect.x += self.velocidade
        if keys[pygame.K_w]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_s]:
            self.rect.y += self.velocidade

    def atirarcarro(self):
        if len(self.Armacarro) < 15:
            self.Armacarro.add(
                Armacarro(*self.rect.center)
            )


class Armacarro(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self, x, y):
        super().__init__()
        self.image = load('images/armacarro.png')
        self.rect = self.image.get_rect(
            center=(x, y)
        )
        self.image = pygame.transform.scale(self.image, (150, 40))

    def update(self):
        # retorna posição aleatoria.
        self.rect.x += -5
        if self.rect.x > tamanho[0]:
            self.kill()


class Arma(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self, x, y):
        super().__init__()
        self.image = load('images/arma_pequena.png')
        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def update(self):
        self.rect.x += 5
        if self.rect.x > tamanho[0]:
            self.kill()


class Tanque(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self):
        super().__init__()

        self.image = load('images/bane.png')
        self.rect = self.image.get_rect(
            center=(0, 600)
        )

    def update(self):
        if self.image.get_rect(center=(1200, 0)):
            self.rect.x += 1


class Tanquee(Sprite):  # criamos o segundo sprint que irá compor o jogo.
                def __init__(self):
                    super().__init__()

                    self.image = load('images/coringa_2.png')
                    self.rect = self.image.get_rect(
                        center=(000, 300)
                    )
                    self.image = pygame.transform.scale(self.image, (300, 300))

                def update(self):
                    if self.image.get_rect(center=(1200, 0)):
                        self.rect.x += 0.2



class Coringa(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self):
        super().__init__()

        self.image = load('images/coringa.png')
        self.rect = self.image.get_rect(
            center=(1200, randint(10, 500))  # retorna posição aleatoria.
        )

    def update(self):
        self.rect.x -= 2




class Slade(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self):
        super().__init__()

        self.image = load('images/slade.png')
        self.rect = self.image.get_rect(
            center=(800, randint(10, 500))  # retorna posição aleatoria.
        )

    def update(self):
        self.rect.x -= 0.1


# Espaço do display
grupo_coringa2 = Group()
grupo_coringa = Group()
grupo_slade = Group()
grupo_tanque = Group()
grupo_tanquee = Group()
grupo_batman = Group()
grupo_batmancar = Group()
batmancar = CarroBatman(grupo_batmancar)
batman = OBatman(grupo_batman)
grupo_geral = GroupSingle(batman)
grupo_geralc = GroupSingle(batmancar)
grupo_tanque.add(Tanque())
grupo_tanquee.add(Tanquee())
grupo_coringa.add(Coringa())
grupo_slade.add(Slade())
round = 0
morte = 0
clock = Clock()

while not done:

    clock.tick(100)

    if round % 100 == 0:
        grupo_coringa.add(Coringa())

    if (morte < 5):
        superficie.blit(fundo, (
            0,
            0))  # Faço o Bit Blit na imagem no ponto 0,0 do plano definimo, com isso consigo inserir a imagem no jogo.
        prim = my_font.render('Primeira Etapa - O electro está por toda parte', False, (255, 255, 0))
        grupo_coringa.draw(superficie)
        grupo_coringa.update()
        grupo_batman.draw(superficie)
        grupo_batman.update()
        grupo_geral.draw(superficie)
        grupo_geral.update()
        disparo = 1
        disparoTanque = 1
        fundo.blit(prim, (0, 10))
    elif (morte < 8):
        superficie.blit(fundo2, (
            0,
            0))  # Faço o Bit Blit na imagem no ponto 0,0 do plano definimo, com isso consigo inserir a imagem no jogo.
        seg = my_font.render('Segunda Etapa - O Duende Verde apareceu! Pare-o', False,
                             (255, 255, 0))
        grupo_slade.draw(superficie)
        grupo_geral.draw(superficie)
        grupo_batman.draw(superficie)
        grupo_slade.update()
        grupo_geral.update()
        grupo_batman.update()
        fundo2.blit(seg, (0, 10))

    elif (morte < 10):
        superficie.blit(fundo3, (
            0,
            0))  # Faço o Bit Blit na imagem no ponto 0,0 do plano definimo, com isso consigo inserir a imagem no jogo.
        terc = my_font.render('Acabe com o Sandman e o Octopus com a ajuda dos Guardiões', False, (255, 255, 0))
        grupo_batmancar.draw(superficie)
        grupo_batmancar.update()
        grupo_geralc.update()
        grupo_geralc.draw(superficie)
        grupo_tanque.draw(superficie)
        grupo_tanque.update()
        grupo_tanquee.draw(superficie)
        grupo_tanquee.update()
        fundo3.blit(terc, (0, 10))

    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYUP:
            if evento.key == K_SPACE:
                batman.jogararma()
            if evento.key == K_TAB:
                batmancar.atirarcarro()

    if groupcollide(grupo_batman, grupo_coringa, True, True):
        morte += 1

    if disparo == 5:
        resposta = True
    else:
        resposta = False

    if disparoTanque == 5:
        respostaT = True

        quarc = my_font.render('Parabéns, amigo da vizinhança, você salvou Nova York', False, (255, 255, 0))
        fundo3.blit(quarc, (450, 350))
    else:
        respostaT = False

    if disparoTanquee == 5:
        respostaTa = True

    else:
        respostaTa = False

    if groupcollide(grupo_batman, grupo_slade, True, resposta):
        disparo += 1

    if groupcollide(grupo_batmancar, grupo_tanque, True, respostaT):
        disparoTanque += 1

    if groupcollide(grupo_batmancar, grupo_tanquee, True, respostaTa):
        disparoTanquee += 1

    round += 1

    display.update()  # a função update atualiza os frames.

#fiquei doente fazendo, só os loucos sabem
