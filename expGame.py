import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500)) # Setter skjermen til 500x500 piksler.
clock = pygame.time.Clock()
running = True

class Spiller:
    def __init__(self):
        self.max_hp = 3
        self.hp = self.max_hp
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.size = 25
        self.color = 'darkolivegreen3'
        self.movespeed = 5
        
    def draw(self):
        self.rect = pygame.Rect(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size)
        pygame.draw.rect(screen, self.color, self.rect)



spiller = Spiller()

while running:
    # Avslutter løkken
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fyller skjermen med hvit farge
    screen.fill("white")

    spiller.draw()

    # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()