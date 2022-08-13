import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI

class Game:
	def __init__(self):

		# game attributes
		self.max_level = 1
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0
		
		# audio 
		self.level_bg_music = pygame.mixer.Sound('../audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('../audio/overworld_music.wav')

		# overworld creation
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)

		# user interface 
		self.ui = UI(screen)


	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health)
		self.status = 'level'
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops = -1)

	def create_overworld(self,current_level,new_max_level):  # Graphical user interface
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)
		self.level_bg_music.stop()

	def change_coins(self,amount):   # To add coins
		self.coins += amount

	def change_health(self,amount): # To decrease health
		self.cur_health += amount

	def check_game_over(self):    
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.max_level,screen,self.create_level)
			self.status = 'overworld'
			self.level_bg_music.stop()
			self.overworld_bg_music.play(loops = -1)  # Music is palyed in loops

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()

# Pygame setup
pygame.init()  # initialize all imported pygame module
screen = pygame.display.set_mode((screen_width,screen_height))  #To set the width and height of the display screen
clock = pygame.time.Clock()  # This is used to create a clock onject which can be used to keep track of time
game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() 
			sys.exit()
	
	screen.fill('grey')  # Fill the backscreen gray while there is no backgrouynd
	game.run()

	pygame.display.update()
	clock.tick(60)  # Help limit the runtime speed of the game