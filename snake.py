import pygame
pygame.init() 
dt = 0
points = 0
font = pygame.font.SysFont(None, 40)
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1400, 780))
#sets player position to half the height and half the width
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    #REQUIRED for some reason. Fetches all pygame events and loops through them to see if player quited.
    for events in pygame.event.get():
        if events == pygame.QUIT:
            running = False
    screen.fill("green")
    pygame.draw.circle(screen, "blue", position, 20)
    keys = pygame.key.get_pressed()
    #if statements set controls and boundaries
    if keys[pygame.K_w] and position.y - 20 > 0:
        position.y -= 300 * dt
    if keys[pygame.K_s] and position.y + 20 < screen.get_height():
        position.y += 300 * dt
    if keys[pygame.K_d] and position.x + 20 < screen.get_width():
        position.x += 300 * dt
    if keys[pygame.K_a] and position.x - 20 > 0:
        position.x -= 300 * dt
    if keys[pygame.K_x]:
        running = False
    #Rendering score and instructions on screen
    scrtxt = font.render(f"Points: {points}", True, "black")
    txt = font.render("Press X to quit, eat apples and survive", True, "black")
    screen.blit(scrtxt, (10, 10))
    screen.blit(txt, (screen.get_width() // 2, 10))
    #required to show results, if not called screen will be blank
    pygame.display.flip()
    #limits frame rate to 60 fps
    dt = clock.tick(60) / 1000
pygame.quit()
