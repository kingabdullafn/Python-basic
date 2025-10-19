import pygame

pygame.init( )
SCREEN_Width, SCREEN_HEIGHT =500, 500

display_surface  = pygame.display.set_mode((SCREEN_Width, SCREEN_HEIGHT))
pygame. display.set_caption('Adding image and background image')
background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(), (SCREEN_Width, SCREEN_HEIGHT)
)

# add image
penguin_image = pygame.transform.scale(pygame.image .load('hello penguin.png').convert_alpha(),(200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_Width//2, SCREEN_HEIGHT//2 - 30))
# add text

text = pygame.font.Font(None, 36).render('Hello penguin', True, pygame. Color('black'))
text_rect = text.get_rect(center=(SCREEN_Width//2, SCREEN_HEIGHT//2 + 110))

def game_Loop():
  clock = pygame.time.Clock()
  running = True # game loop
  while running:
      for event in pygame. event.get():
          if event.type == pygame.QUIT:
              running = False
      display_surface.blit(background_image, (0, 0))
      display_surface.blit(penguin_image, penguin_rect)
      display_surface.blit(text, text_rect)
      pygame. display.flip()
      clock.tick(30)
     
  pygame.quit()
