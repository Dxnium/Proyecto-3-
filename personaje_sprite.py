import pygame
from pygame.locals import *

# Esta clase crea los sprites
class PersonajeSprite(pygame.sprite.Sprite):

	pos_x = 0
	pos_y = 0
	rect = None
	image = None

	def __init__(self, imagen_url):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen_url)
		self.rect = self.image.get_rect()		

	def dibujese(self, surface,x,y):
		self.rect.centerx = x
		self.rect.centery = y
		surface.blit(self.image, self.rect)