import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self,ai):
		super().__init__()      
		self.screen = ai.screen
		self.settings = ai.settings
		self.screen_rect = ai.screen.get_rect()

		self.image =pygame.image.load('E:/python_work/images/plane.bmp')
		self.rect=self.image.get_rect()

		self.rect.midbottom=self.screen_rect.midbottom

		self.x = float(self.rect.x)

		self.moving_right = False
		self.moving_left = False


	def update(self):

		if self.moving_right == True and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left == True and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		self.rect.x = self.x

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def center_ship(self):

		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

		